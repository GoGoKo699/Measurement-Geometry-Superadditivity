'use strict';
// No network requests. Search data is generated locally and loaded as a script.
const menuButton = document.querySelector('.menu-open');
const sidebar = document.querySelector('.sidebar');
if (menuButton && sidebar) {
  menuButton.addEventListener('click', () => {
    const open = sidebar.classList.toggle('open');
    menuButton.setAttribute('aria-expanded', String(open));
  });
  document.addEventListener('keydown', e => {
    if (e.key === 'Escape') { sidebar.classList.remove('open'); menuButton.setAttribute('aria-expanded', 'false'); }
  });
}
const dialog = document.querySelector('.search-dialog');
const input = document.querySelector('.search-input');
const results = document.querySelector('.search-results');
const message = document.querySelector('.search-message');
function search() {
  const q = input.value.trim().toLowerCase();
  results.replaceChildren();
  if (!q) { message.textContent = 'Search the explanations, proof sections, and figure captions.'; return; }
  const terms = q.split(/\s+/).filter(Boolean);
  const matches = (window.PROJECT_SEARCH || []).map(row => {
    const text = (row.title + ' ' + row.text).toLowerCase();
    return {row, score: terms.every(t => text.includes(t)) ? terms.reduce((v,t) => v + (row.title.toLowerCase().includes(t) ? 6 : 1), 0) : 0};
  }).filter(x => x.score > 0).sort((a,b) => b.score-a.score).slice(0,15);
  message.textContent = matches.length ? `${matches.length} result${matches.length === 1 ? '' : 's'} shown. Search runs only on this device.` : 'No match. Try a quantity, a figure number, or a proof section.';
  matches.forEach(({row}) => {
    const li=document.createElement('li'), a=document.createElement('a'), title=document.createElement('strong'), desc=document.createElement('small');
    a.href=row.url;title.textContent=row.title;
    const lower=row.text.toLowerCase();let pos=lower.indexOf(terms[0]);pos=Math.max(0,pos-65);
    desc.textContent=(pos ? '…' : '')+row.text.slice(pos,pos+170)+(row.text.length>pos+170?'…':'');
    a.append(title,desc);li.append(a);results.append(li);
  });
}
document.querySelector('.search-open')?.addEventListener('click', () => { dialog.showModal(); input.focus(); });
document.querySelector('.search-close')?.addEventListener('click', () => dialog.close());
input?.addEventListener('input',search);
document.addEventListener('keydown', e => {
  if (e.key === 'Escape' && dialog.open) { e.preventDefault(); dialog.close(); return; }
  if (e.key==='/' && !/INPUT|TEXTAREA/.test(document.activeElement.tagName)) {e.preventDefault();dialog.showModal();input.focus();}
});
document.querySelectorAll('[data-figure-toggle]').forEach(button => {
  button.addEventListener('click', () => {
    const img=document.getElementById(button.dataset.figureToggle);
    const original=button.getAttribute('aria-pressed')==='true';
    img.src=original ? img.dataset.themed : img.dataset.original;
    button.setAttribute('aria-pressed', String(!original));
    button.textContent=original ? 'Show approved colors' : 'Show accepted figure palette';
    document.getElementById(img.id+'-status').textContent=original ? 'Accepted figure palette; scientific content unchanged.' : 'Approved original colors; protected export.';
  });
});
document.querySelectorAll('pre').forEach(pre => {
  if (!pre.querySelector('code')) return;
  const button=document.createElement('button');button.type='button';button.className='copy-button';button.textContent='Copy';button.setAttribute('aria-label','Copy code block');
  button.addEventListener('click', async () => {
    const text=pre.querySelector('code').textContent;
    try {await navigator.clipboard.writeText(text);button.textContent='Copied';}
    catch {const selection=window.getSelection(),range=document.createRange();range.selectNodeContents(pre.querySelector('code'));selection.removeAllRanges();selection.addRange(range);button.textContent='Selected';}
    setTimeout(()=>button.textContent='Copy',2000);
  });pre.append(button);
});
