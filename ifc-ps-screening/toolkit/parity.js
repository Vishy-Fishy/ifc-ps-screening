// Checks that the HTML tool and the Python engine give identical results.
//
// Usage:  node parity.js [tool.html] [cases]
//   tool.html  default: ifc-ps-screening-tool.html next to this script
//   cases      number of random cases (default 4000)
//
// What it does:
//   1. pulls the embedded rule set and engine out of the built HTML;
//   2. checks the embedded rule set is exactly the JSON file next to this script;
//   3. runs the reference cases, a deterministic random set and a set of invalid
//      inputs through both the HTML engine and screen.py;
//   4. compares the complete output (not just statuses), error messages included.
// Exits 1 on any difference, on a missing piece, or if the random set fails to
// reach every category and status (which would make the comparison weak).
"use strict";
const fs = require("fs");
const os = require("os");
const path = require("path");
const { execFileSync } = require("child_process");

const here = __dirname;
const htmlPath = process.argv[2] || path.join(here, "ifc-ps-screening-tool.html");
const N = parseInt(process.argv[3] || "4000", 10);
const rulesPath = fs.readdirSync(here).filter(f => /^ifc_ps_rules_v.*\.json$/.test(f)).map(f => path.join(here, f))[0];
if (!rulesPath) { console.error("no ifc_ps_rules_v*.json next to parity.js"); process.exit(1); }
const rulesFile = JSON.parse(fs.readFileSync(rulesPath, "utf8"));

// ---- 1. extract the engine from the HTML
const html = fs.readFileSync(htmlPath, "utf8");
const a = html.indexOf("/* @@DATA_START */"), b = html.indexOf("/* @@ENGINE_END */");
if (a < 0 || b < 0 || b < a) { console.error("engine markers not found in " + htmlPath); process.exit(1); }
const code = html.slice(a, b);
const eng = new Function(code + "\n;return {RULES: RULES, screen: screen, ENGINE_VERSION: ENGINE_VERSION, CaseError: CaseError};")();

const canon = v => JSON.stringify(v, (k, x) => (x && typeof x === "object" && !Array.isArray(x))
  ? Object.keys(x).sort().reduce((o, key) => (o[key] = x[key], o), {}) : x);
let problems = 0;
const fail = msg => { problems++; if (problems <= 8) console.log("DIFF  " + msg); };

// ---- 2. the page carries exactly this rule set
if (canon(eng.RULES) !== canon(rulesFile)) { console.log("DIFF  the rule set embedded in the HTML is not the JSON file; rebuild the HTML"); problems++; }

// ---- 3. build the case list
let seed = 20261029;
const rnd = () => { seed |= 0; seed = seed + 0x6D2B79F5 | 0; let t = Math.imul(seed ^ seed >>> 15, 1 | seed); t = t + Math.imul(t ^ t >>> 7, 61 | t) ^ t; return ((t ^ t >>> 14) >>> 0) / 4294967296; };
const pick = arr => arr[Math.floor(rnd() * arr.length)];
const qids = rulesFile.questions.map(q => q.id);
const sectors = rulesFile.sectors.map(s => s.id), stages = rulesFile.stages.map(s => s.id);

const cases = [];
const ref = JSON.parse(fs.readFileSync(path.join(here, "test_cases.json"), "utf8"));
ref.forEach(c => cases.push({sector: c.sector, stage: c.stage, country: c.country, answers: c.answers}));
const profiles = [
  {yes: .05, no: .85, unsure: .05},   // mostly No
  {yes: .30, no: .30, unsure: .20},   // mixed
  {yes: .10, no: .30, unsure: .10},   // mostly unanswered
  {yes: .02, no: .50, unsure: .02},   // sparse, low risk
];
for (let i = 0; i < N; i++) {
  const p = pick(profiles), answers = {};
  qids.forEach(id => {
    const r = rnd();
    let v = r < p.yes ? "yes" : r < p.yes + p.no ? "no" : r < p.yes + p.no + p.unsure ? "unsure" : null;
    if (v === null) { if (rnd() < .5) return; v = ""; }
    if (v && rnd() < .05) v = " " + v.toUpperCase() + " ";
    answers[id] = v;
  });
  const c = {answers};
  if (rnd() > .03) c.sector = pick(sectors); else c.sector = pick(["", null]);
  if (rnd() > .1) c.stage = pick(stages.concat([""]));
  const r = rnd(); if (r < .8) c.country = "IN"; else if (r < .95) c.country = "OTHER"; else if (r < .98) c.country = ""; // else absent
  cases.push(c);
}
const validCount = cases.length;
const invalid = [
  {sector: "Solar PV"}, {stage: "build"}, {country: "India"}, {answers: {p5_land: true}}, {answers: {p5_land: "Yes please"}},
  {answers: {zz: "yes"}}, {answers: ["yes"]}, {answers: {p5_land: 1}}, {answers: {p5_land: {a: 1}}}, {sector: 5}, {stage: ["x"]},
  {country: 7}, {sector: "nope", stage: "nope", country: "nope", answers: {p5_land: 1, zz: "no"}}, [], "solar", 42,
  {answers: {p5_land: "maybe", p5_users: false}}, {sector: "solar", answers: {p2_workers: "yes", p9: "no"}},
];
invalid.forEach(c => cases.push(c));

// ---- 4. run both engines
const tmp = fs.mkdtempSync(path.join(os.tmpdir(), "ifcps-parity-"));
const casesFile = path.join(tmp, "cases.json");
fs.writeFileSync(casesFile, JSON.stringify(cases));
const py = process.env.PYTHON || (process.platform === "win32" ? "python" : "python3");
let pyOut;
try {
  pyOut = JSON.parse(execFileSync(py, ["-I", path.join(here, "screen.py"), "--batch", rulesPath, casesFile], {maxBuffer: 1 << 30}).toString("utf8"));
} finally { fs.rmSync(tmp, {recursive: true, force: true}); }
if (pyOut.length !== cases.length) { console.error("python returned " + pyOut.length + " results for " + cases.length + " cases"); process.exit(1); }

const seen = {cat: {}, status: {}, errors: 0, warnings: 0, gate: 0};
cases.forEach((c, i) => {
  let js;
  try { js = {ok: eng.screen(eng.RULES, c)}; } catch (e) {
    if (!(e instanceof eng.CaseError)) { fail("case " + i + ": JS threw " + e); return; }
    js = {error: e.errors};
  }
  const p = pyOut[i];
  if (p.error) {
    seen.errors++;
    if (!js.error) return fail("case " + i + ": python rejected the case, JS accepted it " + JSON.stringify(c));
    if (canon(js.error) !== canon(p.error)) fail("case " + i + ": error messages differ\n   js: " + JSON.stringify(js.error) + "\n   py: " + JSON.stringify(p.error));
    return;
  }
  if (js.error) return fail("case " + i + ": JS rejected the case, python accepted it: " + JSON.stringify(js.error));
  if (canon(js.ok) !== canon(p)) {
    const ja = js.ok, k = Object.keys(p).find(key => canon(ja[key]) !== canon(p[key]));
    fail("case " + i + ": outputs differ in '" + k + "'\n   js: " + canon(ja[k]).slice(0, 300) + "\n   py: " + canon(p[k]).slice(0, 300));
    return;
  }
  seen.cat[p.category.value] = (seen.cat[p.category.value] || 0) + 1;
  p.standards.forEach(s => { seen.status[s.status] = (seen.status[s.status] || 0) + 1; });
  if (p.warnings.length) seen.warnings++;
  if (p.india_ec_gate) seen.gate++;
});

// ---- 5. the comparison must have been able to catch things
const need = ["A", "B", "C", "FI", "-"];
need.forEach(c => { if (!seen.cat[c]) { console.log("DIFF  random set never produced category " + c + ", comparison too weak"); problems++; } });
["trig", "review", "clear", "open"].forEach(s => { if (!seen.status[s]) { console.log("DIFF  random set never produced status " + s); problems++; } });
if (!seen.errors) { console.log("DIFF  no invalid case was rejected"); problems++; }

console.log("valid cases compared: " + validCount + " | invalid cases: " + invalid.length + " (" + seen.errors + " rejected by both)");
console.log("categories: " + JSON.stringify(seen.cat) + " | statuses: " + JSON.stringify(seen.status));
console.log("cases with sanity warnings: " + seen.warnings + " | with EC gate note: " + seen.gate);
console.log(problems ? "PARITY FAILED: " + problems + " problem(s)" : "PARITY OK: HTML and Python outputs are identical");
process.exit(problems ? 1 : 0);
