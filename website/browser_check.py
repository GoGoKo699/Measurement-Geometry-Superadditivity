#!/usr/bin/env python3
"""Check reader controls through loopback HTTP or an in-memory file mirror.

The HTTP mode tests actual navigation and source downloads. The mirror does
not test HTTP or file navigation. Both modes preserve the built site bytes.
"""
from pathlib import Path
from bs4 import BeautifulSoup
import argparse
import base64
import hashlib
import json
import mimetypes
import shutil
from urllib.parse import unquote, urlsplit
from playwright.sync_api import sync_playwright


def mirrored(site, name):
    soup = BeautifulSoup((site / (name + '.html')).read_text(), 'html.parser')
    for css in soup.find_all('link', rel='stylesheet'):
        style = soup.new_tag('style')
        style.string = (site / css['href']).read_text()
        css.replace_with(style)
    scripts = []
    for script in list(soup.find_all('script', src=True)):
        scripts.append((site / script['src']).read_text())
        script.decompose()
    for script in scripts:
        tag = soup.new_tag('script')
        tag.string = script
        soup.body.append(tag)
    for img in soup.find_all('img'):
        for key in ('src', 'data-original', 'data-themed'):
            if img.get(key):
                path = site / img[key]
                mime = mimetypes.guess_type(str(path))[0] or 'application/octet-stream'
                img[key] = 'data:' + mime + ';base64,' + base64.b64encode(path.read_bytes()).decode()
    return str(soup)


def configured_pages(site):
    config = json.loads(Path(__file__).with_name('site.json').read_text())
    pages = config['pages']
    names = [p['slug'] for p in pages]
    required = {'index', 'channel', 'proof-guide', 'figures', 'limits', 'model',
                'proof', 'verification', 'reproduce', 'references', 'materials'}
    assert required <= set(names), 'Missing learning or expert route'
    assert len(names) == len(set(names)), 'Duplicate configured route'
    built = json.loads((site / 'files/BUILD_RECORD.json').read_text())['pages']
    assert {p['page'] for p in built} == {name + '.html' for name in names}, 'Build/configuration route mismatch'
    return pages


def run(site, out, executable, base_url=None, native_mathml=False):
    site = site.resolve()
    out.mkdir(parents=True, exist_ok=True)
    errors, external, failed, records, sources, navigation = [], [], [], [], [], []
    result = {
        'passed': False,
        'mode': 'local HTTP navigation' if base_url else 'in-memory local-file mirror; HTTP and file navigation not tested',
        'desktop_viewport': [1440, 1000], 'mobile_viewport': [390, 844],
        'external_requests': external, 'failed_requests': failed, 'console_page_errors': errors,
        'page_records': records, 'source_downloads': sources, 'navigation_records': navigation,
        'real_link_navigation_tested': False,
        'accessibility_scope': 'Keyboard controls, native mathematics and responsive navigation; not a full WCAG audit.',
    }
    try:
        pages = configured_pages(site)
        names = [p['slug'] for p in pages]
        nav_targets = {name + '.html' for name in names}
        with sync_playwright() as pw:
            browser = pw.chromium.launch(executable_path=executable, headless=True, args=['--no-sandbox'])
            result['browser'] = 'Chromium'
            result['browser_version'] = browser.version
            ctx = browser.new_context(viewport={'width': 1440, 'height': 1000}, device_scale_factor=1)

            def route_handler(route):
                if base_url and route.request.url.startswith(base_url.rstrip('/') + '/'):
                    route.continue_()
                else:
                    external.append(route.request.url)
                    route.abort()

            ctx.route('**/*', route_handler)
            page = None
            viewport = {'width': 1440, 'height': 1000}

            def load(name):
                nonlocal page
                if page is not None:
                    page.close()
                page = ctx.new_page()
                page.set_viewport_size(viewport)
                page.on('pageerror', lambda e: errors.append(str(e)))
                page.on('requestfailed', lambda request: failed.append({'url': request.url, 'error': request.failure}))
                if base_url:
                    response = page.goto(base_url.rstrip('/') + '/' + name + '.html', wait_until='networkidle')
                    assert response.ok, (name, 'HTTP navigation failed', response.status)
                else:
                    page.set_content(mirrored(site, name), wait_until='load')
                page.evaluate('document.fonts.ready')

            def check_navigation():
                actual = set(page.locator('#site-navigation a.nav-link').evaluate_all('(links)=>links.map(x=>x.getAttribute("href"))'))
                assert actual == nav_targets, ('Navigation does not cover configured routes', actual ^ nav_targets)

            if native_mathml:
                fixture = site / 'mathml-regression/index.html'
                assert fixture.is_file(), 'Generate the native MathML regression fixture first'
                native = ctx.new_page()
                native.on('pageerror', lambda e: errors.append(str(e)))
                native.on('requestfailed', lambda request: failed.append({'url': request.url, 'error': request.failure}))
                result['native_mathml_layout'] = []
                for view, size in [('desktop', {'width': 1440, 'height': 1000}),
                                   ('mobile', {'width': 390, 'height': 844})]:
                    native.set_viewport_size(size)
                    if base_url:
                        response = native.goto(base_url.rstrip('/') + '/mathml-regression/index.html', wait_until='networkidle')
                        assert response.ok, 'Native MathML fixture failed to load'
                    else:
                        native.set_content(fixture.read_text(), wait_until='load')
                    native.evaluate('document.fonts.ready')
                    current = native.locator('#current-p71 .formula math')
                    control = native.locator('#tagged-p71-control .formula math')
                    assert current.count() == control.count() == 1
                    assert current.locator('mlabeledtr, mtable, merror').count() == 0
                    assert control.locator('mlabeledtr').count() == 1, 'Failure control does not exercise equation numbering'
                    bounds, old_bounds = current.bounding_box(), control.bounding_box()
                    font_size = current.evaluate('(x)=>parseFloat(getComputedStyle(x).fontSize)')
                    assert bounds and 0 < bounds['height'] <= 2 * font_size, ('Vertical native MathML layout', view, bounds)
                    wrapper = native.locator('#current-p71 .formula')
                    metrics = wrapper.evaluate('(x)=>({width:x.clientWidth, content_width:x.scrollWidth, overflow:getComputedStyle(x).overflowX})')
                    if metrics['content_width'] > metrics['width'] + 2:
                        assert metrics['overflow'] in ('auto', 'scroll')
                        wrapper.evaluate('(x)=>{x.scrollLeft=x.scrollWidth}')
                        assert wrapper.evaluate('(x)=>x.scrollLeft') > 0
                        wrapper.evaluate('(x)=>{x.scrollLeft=0}')
                    assert native.evaluate('document.documentElement.scrollWidth <= innerWidth+2')
                    native.screenshot(path=str(out / ('native-mathml-' + view + '.png')), full_page=True)
                    result['native_mathml_layout'].append({
                        'viewport': view, 'current_height': bounds['height'],
                        'tagged_control_height': old_bounds['height'],
                        'tagged_vertical_failure_reproduced': old_bounds['height'] > 2 * bounds['height'],
                        'current_has_no_labeled_rows': True, 'horizontal_access': True, **metrics,
                    })
                native.close()

            def check_proof_math(view):
                targets = [
                    ('normalized-deficit', r'\mathscr D/(ca)', 1),
                    ('lower-input-tail', r'B_d(c)&:=', 3),
                    ('geometric-inequality', r'P(a)-\frac{\arcsin', 1),
                    ('reported-records', r'\mathsf p_\pm(\omega)', 4),
                    ('block-information', r'\mathcal I_n&:=', 2),
                    ('polynomial-bounds', r'\frac{c_A}{(m+1)^J}', 2),
                    ('eight-use-rate', r'\frac{\mathcal I_8}{8}', 2),
                ]
                for key, marker, expected_rows in targets:
                    expression = page.locator('math').filter(
                        has=page.locator('annotation', has_text=marker))
                    assert expression.count() == 1, ('Missing or repeated proof equation', key)
                    assert expression.locator('mlabeledtr').count() == 0, (key, 'Unsupported native equation label')
                    table = expression.locator('mtable').first
                    if expected_rows == 1:
                        assert table.count() == 0, (key, 'Unexpected multiline layout')
                        layout = expression
                    else:
                        assert table.locator(':scope > mtr').count() == expected_rows, (key, 'Missing mathematical rows')
                        layout = table
                    bounds = layout.bounding_box()
                    assert bounds and bounds['width'] > 0 and bounds['height'] > 0, (key, 'Invisible mathematics')
                    if key == 'normalized-deficit':
                        assert expression.locator('mfrac').count() == 0, (key, 'Stacked fraction returned')
                        font_size = expression.evaluate('(x)=>parseFloat(getComputedStyle(x).fontSize)')
                        assert bounds['height'] <= 2 * font_size, (key, 'Unexpected vertical expansion', bounds)
                    wrapper = expression.locator('xpath=..')
                    assert 'display' in wrapper.get_attribute('class').split()
                    if key == 'normalized-deficit':
                        label = wrapper.locator('xpath=../following-sibling::p[1]')
                        assert label.inner_text() == '(P7.1)', 'Missing external equation number'
                    wrapper.scroll_into_view_if_needed()
                    metrics = wrapper.evaluate('(x)=>({width:x.clientWidth, content_width:x.scrollWidth, overflow:getComputedStyle(x).overflowX})')
                    if metrics['content_width'] > metrics['width'] + 2:
                        assert metrics['overflow'] in ('auto', 'scroll'), (key, 'Clipped equation')
                        wrapper.evaluate('(x)=>{x.scrollLeft=x.scrollWidth}')
                        assert wrapper.evaluate('(x)=>x.scrollLeft') > 0, (key, 'Equation cannot scroll')
                        wrapper.evaluate('(x)=>{x.scrollLeft=0}')
                    wrapper.screenshot(path=str(out / ('proof-' + key + '-' + view + '.png')))
                    result.setdefault('proof_math_layout', []).append({
                        'equation': key, 'viewport': view, 'rows': expected_rows,
                        'height': bounds['height'],
                        'visible': True, 'horizontal_access': True, **metrics,
                    })

            for name in names:
                load(name)
                assert page.evaluate('document.documentElement.scrollWidth <= innerWidth+2'), (name, 'desktop page overflow')
                assert page.locator('img').evaluate_all('(imgs)=>imgs.filter(x=>!x.complete || x.naturalWidth===0).length') == 0, (name, 'image failed')
                check_navigation()
                if name == 'proof':
                    check_proof_math('desktop')
                records.append({'page': name, 'desktop_no_page_overflow': True, 'images_loaded': True, 'configured_navigation_complete': True})
                if name in ('index', 'background', 'channel', 'figures', 'proof-guide', 'visual-design'):
                    page.screenshot(path=str(out / (name + '-desktop.png')), full_page=True)
                if base_url:
                    href = page.locator('.page-meta a').first.get_attribute('href')
                    local = (site / unquote(urlsplit(href).path)).resolve()
                    assert local.is_relative_to(site) and local.is_file(), (name, 'source link escapes or is absent')
                    response = ctx.request.get(base_url.rstrip('/') + '/' + href)
                    body = response.body()
                    assert response.ok and body == local.read_bytes(), (name, 'source download differs')
                    sources.append({'page': name, 'href': href, 'status': response.status, 'sha256': hashlib.sha256(body).hexdigest(), 'matches_local_source': True})

            load('index')
            page.keyboard.press('Tab')
            assert page.locator('.skip').evaluate('(x)=>x===document.activeElement')
            page.keyboard.press('/')
            assert page.locator('.search-input').evaluate('(x)=>x===document.activeElement')
            search_results = {}
            for query in ['all-measured'] + (['Preskill'] if 'background' in names else []):
                page.locator('.search-input').fill(query)
                targets = page.locator('.search-results a').evaluate_all('(links)=>links.map(x=>x.getAttribute("href"))')
                assert targets, ('No local search result', query)
                if query == 'Preskill':
                    assert any(urlsplit(href).path == 'background.html' for href in targets), 'Selected tutorial absent from search'
                search_results[query] = targets
            page.keyboard.press('Escape')
            assert not page.locator('dialog').is_visible()

            load('figures')
            for number in (1, 2, 3):
                figure = page.locator('#fig-' + str(number))
                button = page.locator('[data-figure-toggle="fig-' + str(number) + '"]')
                before = figure.get_attribute('src')
                button.click()
                assert figure.get_attribute('src') != before and figure.get_attribute('src') == figure.get_attribute('data-original')
                button.click()
                assert figure.get_attribute('src') == before
            page.wait_for_function('Array.from(document.images).every(x=>x.complete && x.naturalWidth>0)')

            if base_url:
                for item in pages:
                    load(item['slug'])
                    destination = item.get('next') or 'index'
                    page.locator('.next-link').click()
                    assert urlsplit(page.url).path.endswith('/' + destination + '.html'), (item['slug'], 'next route mismatch')
                    navigation.append({'from': item['slug'], 'to': destination, 'control': 'next-link'})
                    if item.get('previous'):
                        load(item['slug'])
                        page.locator('a[rel=prev]').click()
                        assert urlsplit(page.url).path.endswith('/' + item['previous'] + '.html'), (item['slug'], 'previous route mismatch')
                        navigation.append({'from': item['slug'], 'to': item['previous'], 'control': 'previous-link'})
                if 'background' in names:
                    load('background')
                    links = page.locator('article a[href]').evaluate_all('(links)=>links.map(x=>x.getAttribute("href"))')
                    tutorial_links = {href for href in links if urlsplit(href).hostname == 'arxiv.org'}
                    assert {'https://arxiv.org/abs/1604.07450v5', 'https://arxiv.org/pdf/1604.07450v5'} <= tutorial_links, 'Pinned tutorial links absent'
                    assert all('1604.07450v5' in href for href in tutorial_links), 'Unpinned or additional tutorial link'
                    result['pinned_tutorial_links_present_without_fetch'] = sorted(tutorial_links)
                    bridge_links = sorted({href for href in links if urlsplit(href).path in nav_targets})
                    assert any(urlsplit(href).path == 'channel.html' for href in bridge_links), 'Missing tutorial-to-channel return link'
                    for href in bridge_links:
                        load('background')
                        page.locator('article a[href=' + json.dumps(href) + ']').first.click()
                        assert page.url == base_url.rstrip('/') + '/' + href, ('Bridge navigation mismatch', href)
                        fragment = unquote(urlsplit(href).fragment)
                        if fragment:
                            anchors = page.locator('[id=' + json.dumps(fragment) + '], a[name=' + json.dumps(fragment) + ']')
                            anchors.first.wait_for(state='attached')
                            assert anchors.count() > 0, ('Bridge anchor absent', href)
                        navigation.append({'from': 'background', 'to': href, 'control': 'bridge-link'})
                result['real_link_navigation_tested'] = True

            viewport = {'width': 390, 'height': 844}
            for name, record in zip(names, records):
                load(name)
                assert page.evaluate('document.documentElement.scrollWidth <= innerWidth+2'), (name, 'mobile page overflow')
                assert page.locator('.menu-open').is_visible()
                page.locator('.menu-open').click()
                assert page.locator('.sidebar').is_visible()
                check_navigation()
                if base_url:
                    destination = next(p for p in pages if p['slug'] == name).get('next') or 'index'
                    page.locator('#site-navigation a[href="' + destination + '.html"]').click()
                    assert urlsplit(page.url).path.endswith('/' + destination + '.html'), (name, 'mobile route mismatch')
                    navigation.append({'from': name, 'to': destination, 'control': 'mobile-menu-link'})
                    load(name)
                    page.locator('.menu-open').click()
                page.keyboard.press('Escape')
                assert not page.locator('.sidebar').is_visible()
                record['mobile_no_page_overflow'] = True
                record['mobile_menu_keyboard_controls'] = True
                if name == 'proof':
                    check_proof_math('mobile')
                if name in ('index', 'background', 'channel', 'proof-guide', 'model', 'proof', 'figures', 'materials', 'visual-design'):
                    page.screenshot(path=str(out / (name + '-mobile.png')), full_page=name in ('index', 'background', 'channel', 'proof-guide', 'figures', 'visual-design'))

            nojs = browser.new_context(java_script_enabled=False, viewport={'width': 1280, 'height': 900})
            nojs.route('**/*', route_handler)
            p = nojs.new_page()
            p.on('pageerror', lambda e: errors.append(str(e)))
            p.on('requestfailed', lambda request: failed.append({'url': request.url, 'error': request.failure}))
            nojs_records = []
            for name in ['proof', 'figures'] + (['background', 'channel'] if 'background' in names else []):
                p.set_viewport_size({'width': 1280, 'height': 900})
                if base_url:
                    response = p.goto(base_url.rstrip('/') + '/' + name + '.html', wait_until='networkidle')
                    assert response.ok
                else:
                    p.set_content(mirrored(site, name), wait_until='domcontentloaded')
                actual = set(p.locator('#site-navigation a.nav-link').evaluate_all('(links)=>links.map(x=>x.getAttribute("href"))'))
                assert actual == nav_targets
                if name == 'proof':
                    assert p.locator('math').count() > 100
                    assert p.locator('math').first.evaluate('(x)=>x.getBoundingClientRect().width>0 && x.getBoundingClientRect().height>0')
                if name == 'figures':
                    assert p.locator('img').count() == 3
                if name == 'background':
                    assert 'Preskill' in p.locator('article').inner_text()
                p.set_viewport_size({'width': 390, 'height': 844})
                assert p.locator('.sidebar').is_visible()
                assert not p.locator('.menu-open').is_visible() and not p.locator('.search-open').is_visible()
                assert p.evaluate('document.documentElement.scrollWidth <= innerWidth+2'), (name, 'no-JavaScript mobile overflow')
                nojs_record = {'page': name, 'configured_navigation_complete': True, 'mobile_reading': True}
                if base_url and name == 'background':
                    p.locator('article a[href^="channel.html"]').first.click()
                    assert urlsplit(p.url).path.endswith('/channel.html'), 'No-JavaScript bridge return failed'
                    nojs_record['actual_channel_return_navigation'] = True
                nojs_records.append(nojs_record)
            nojs.close()
            ctx.close()
            browser.close()
        assert not errors, errors
        assert not external, external
        assert not failed, failed
        result.update({'passed': True, 'pages_checked': len(records), 'required_and_configured_routes_checked': names,
                       'search_results': search_results, 'search_results_for_all_measured': len(search_results['all-measured']),
                       'keyboard_skip_link_focus': True,
                       'keyboard_opens_search': True, 'escape_closes_search_and_mobile_nav': True,
                       'all_three_figure_color_toggles': True, 'figure_theme_toggle': True,
                       'no_javascript_math_and_navigation': True,
                       'no_javascript_mobile_navigation': True, 'no_javascript_records': nojs_records})
    except Exception as error:
        result['failure'] = {'type': type(error).__name__, 'message': str(error)}
        raise
    finally:
        (out / 'BROWSER_CHECK.json').write_text(json.dumps(result, indent=2) + '\n')
    return result


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--site', type=Path, required=True)
    ap.add_argument('--output', type=Path, required=True)
    ap.add_argument('--chromium', default=shutil.which('chromium') or None)
    ap.add_argument('--base-url', help='Optional loopback HTTP server for actual navigation tests.')
    ap.add_argument('--native-mathml', action='store_true', help='Also check the generated native MathJax MathML regression fixture.')
    args = ap.parse_args()
    if args.base_url and (urlsplit(args.base_url).scheme != 'http' or urlsplit(args.base_url).hostname != '127.0.0.1'):
        ap.error('Use an HTTP review server bound to 127.0.0.1, not a public site.')
    print(json.dumps(run(args.site, args.output, args.chromium, args.base_url, args.native_mathml), indent=2))
