# IFC PS screening toolkit: rule set 1.2.0 / engine 1.2.0 (29 October 2026)

Replaces 1.1.0 (issued earlier the same day). One JSON rule set (ifc_ps_rules_v1.2.0.json) drives the HTML checklist
(built by build_html.py from template.html), the Python engine (screen.py) and the Claude Skill.

What changed in 1.2.0 (after reading the IFC Sustainability Policy 2012 and the FI Guidance Note, Sept 2023)
- Category meanings now quoted from Sustainability Policy para 40 (A, B, C, FI-1 to FI-3) and shown with the paragraph.
- FI: PS1 actions rewritten from the FI Guidance Note (ESMS, Exclusion List and national law, PS2 for the FI's own staff,
  Higher Risk Transactions, scope for specified end use or general-purpose funding, reporting, coal restrictions).
- IFC Exclusion List (amended 8 December 2025) added as data: a reminder on every result, with the full list and the
  extra FI exclusions one click away; the Skill gets references/exclusion-list.md and references/fi-screening.md.
- Sector notes from the Policy (paras 49-53) for oil and gas, mining, power distribution and water.
- ESAP wording corrected: Category C projects often have none (Policy fn 10). Broad Community Support (para 30) and the
  FPIC review (para 31) added as investor expectations.
- The high-risk-greenfield A-signal is labelled EMC judgement: Policy paras 42-43 name no sectors.
- 20 reference cases (2 new), 33 checks.

What changed in 1.1.0 (kept)
- 33 questions (3 new), 18 sectors, data-driven Category C, minimum 10 Yes/No answers, sector sanity checks,
  paragraph citation on every action, strict input checking, HTML built from the JSON with full-output parity test.
- Sustainability Framework review: Phase I dialogue to December 2026, consultation on draft proposals from January 2027,
  nothing approved, no effective date. (The earlier "2028" claim was unsupported.)

Checks (run in this folder): python3 -I run_tests.py (33 checks), node parity.js (HTML = Python on 4,000+ generated cases).
To change a rule: edit the rule set, run python3 build_html.py, then run_tests.py and parity.js.

Still open
- Sector risk classes, the answers-to-category rules and the sanity checks are EMC judgement (the Policy gives no sector list or scoring rule).
- Great Indian Bustard Dec 2025 judgment: verified from a news report only.
- India-law comparison lines are general knowledge and need a legal check; the Forest Rights Act / 2022 forest rules point is unverified.
- p5_land "yes" triggers PS5 conservatively; PS5 para 6 excludes voluntary transactions.
- FI-1, FI-2 or FI-3 cannot be chosen without a portfolio breakdown; the checklist does not collect one.
