#!/usr/bin/env node
'use strict';

// GitHub can expose MathJax's MathML to the browser's native renderer.
// MathML Core does not support the mlabeledtr produced by \tag. A successful
// TeX parse or SVG render therefore does not establish native compatibility.
// See https://github.com/mathjax/MathJax/issues/3270#issuecomment-2274382957
// and https://github.com/orgs/community/discussions/19953.
const assert = require('node:assert/strict');
const crypto = require('node:crypto');
const fs = require('node:fs');
const path = require('node:path');
const {mathjax} = require('mathjax-full/js/mathjax.js');
const {TeX} = require('mathjax-full/js/input/tex.js');
const {SVG} = require('mathjax-full/js/output/svg.js');
const {liteAdaptor} = require('mathjax-full/js/adaptors/liteAdaptor.js');
const {RegisterHTMLHandler} = require('mathjax-full/js/handlers/html.js');
const {SerializedMmlVisitor} = require('mathjax-full/js/core/MmlTree/SerializedMmlVisitor.js');
const {STATE} = require('mathjax-full/js/core/MathItem.js');
require('mathjax-full/js/input/tex/ams/AmsConfiguration.js');
require('mathjax-full/js/input/tex/newcommand/NewcommandConfiguration.js');
require('mathjax-full/js/input/tex/boldsymbol/BoldsymbolConfiguration.js');

const OLD_P71 = String.raw`\mathscr D/(ca)=V(a)\bigl[C_\perp(t,c)/c\bigr]+W(a)C_\parallel(t,c)-P(a)h_2(t). \tag{P7.1}`;
const ROOT = path.resolve(__dirname, '..');
const args = process.argv.slice(2);
let output;
let sourcePath = path.join(ROOT, 'docs/COMPLETE_PROOF.md');
for (let index = 0; index < args.length; index++) {
  const option = args[index];
  const value = args[++index];
  assert(value, `Missing value for ${option}`);
  if (option === '--output') output = path.resolve(value);
  else if (option === '--source') sourcePath = path.resolve(value);
  else throw new Error(`Unknown option: ${option}`);
}
assert(output, 'Usage: node website/mathml_check.cjs --output DIRECTORY [--source PROOF]');

RegisterHTMLHandler(liteAdaptor());
const input = new TeX({
  packages: ['base', 'ams', 'newcommand', 'boldsymbol'],
  formatError: (_, error) => { throw error; },
});
const document = mathjax.document('', {
  InputJax: input,
  OutputJax: new SVG(),
  compileError: (_, __, error) => { throw error; },
});
const visitor = new SerializedMmlVisitor();
function nativeMathML(tex) {
  input.reset();
  // Stop before SVG typesetting: this is the actual native MathML tree.
  return visitor.visitTree(document.convert(tex, {display: true, end: STATE.COMPILED}));
}
const sha256 = value => crypto.createHash('sha256').update(value).digest('hex');
const labeledRows = mml => (mml.match(/<mlabeledtr(?:\s|>)/g) || []).length;
const escapeHtml = value => value.replaceAll('&', '&amp;').replaceAll('<', '&lt;').replaceAll('>', '&gt;');

const source = fs.readFileSync(sourcePath, 'utf8');
const failures = [];
const expressions = [];
for (const match of source.matchAll(/\$\$([\s\S]*?)\$\$/g)) {
  const after = source.slice(match.index + match[0].length);
  const label = after.match(/^\s*\*\*\((P\d+\.\d+)\)\*\*/)?.[1] || null;
  const line = source.slice(0, match.index).split('\n').length;
  const entry = {index: expressions.length + 1, label, line, tex: match[1].trim()};
  try {
    entry.mathml = nativeMathML(entry.tex);
    entry.mlabeledtr_count = labeledRows(entry.mathml);
    if (entry.mlabeledtr_count) failures.push(`Line ${line}: unsupported mlabeledtr in ${label || 'display math'}`);
    if (/<merror(?:\s|>)/.test(entry.mathml)) failures.push(`Line ${line}: MathJax emitted merror`);
  } catch (error) {
    failures.push(`Line ${line}: ${error.message}`);
  }
  expressions.push(entry);
}
assert(expressions.length > 0, 'No proof display expressions found');

const control = nativeMathML(OLD_P71);
assert.equal(labeledRows(control), 1, 'The old tagged P7.1 must exercise the unsupported-row detector');
const matches = expressions.filter(entry => entry.label === 'P7.1');
if (matches.length !== 1) failures.push('Expected one P7.1 identified by its following Markdown label');
const current = matches[0];
if (current && current.tex !== OLD_P71.replace(/\s*\\tag\{P7\.1\}$/, '')) {
  failures.push('P7.1 must retain the exact expression from the tagged control, with only its label moved');
}

const report = {
  schema_version: 1,
  source: path.relative(ROOT, sourcePath).split(path.sep).join('/'),
  source_sha256: sha256(source),
  mathjax_version: require('mathjax-full/package.json').version,
  display_count: expressions.length,
  labeled_equation_count: expressions.filter(entry => entry.label).length,
  negative_control: {label: 'P7.1', mlabeledtr_count: labeledRows(control)},
  results: expressions.map(({index, label, line, mathml, mlabeledtr_count}) => ({
    index, label, line, mlabeledtr_count,
    mathml_sha256: mathml ? sha256(mathml) : null,
  })),
  failures,
};
fs.mkdirSync(output, {recursive: true});
fs.writeFileSync(path.join(output, 'report.json'), JSON.stringify(report, null, 2) + '\n');
// Review artifact only. Deliberately no MathJax JavaScript, polyfills, or CSS
// targeting MathML descendants: Chromium must display these trees natively.
const html = `<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Native MathML regression</title>
<style>
body { margin: 0; padding: 24px; font: 16px/1.5 system-ui, sans-serif; }
main { max-width: 1100px; margin: auto; }
section { margin: 24px 0; }
.formula { overflow-x: auto; padding: 16px 0; }
pre { white-space: pre-wrap; overflow-wrap: anywhere; }
</style>
</head>
<body><main>
<h1>Native MathML regression</h1>
<section id="current-p71" data-equation="P7.1">
<h2>Current P7.1</h2>
<div class="formula">${current?.mathml || '<p>Current P7.1 failed compilation.</p>'}</div>
<p><strong>(P7.1)</strong></p>
</section>
<section id="tagged-p71-control" data-equation="P7.1">
<h2>Previous tagged P7.1: failure control</h2>
<div class="formula">${control}</div>
</section>
<details><summary>Regression result</summary><pre>${escapeHtml(JSON.stringify({display_count: expressions.length, failures}, null, 2))}</pre></details>
</main></body></html>
`;
fs.writeFileSync(path.join(output, 'index.html'), html);
console.log(JSON.stringify({display_count: expressions.length, negative_control_detected: true, failures, output}, null, 2));
process.exitCode = failures.length ? 1 : 0;
