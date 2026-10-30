# IFC Performance Standards screening toolkit

EMC's two-part screening workflow for the IFC Performance Standards: a one-file HTML checklist for the first pass, and a Claude Skill for depth, citations and documents. Both are built from one rule set, so they cannot disagree.

Current: rule set 1.2.0, engine 1.2.0. Built for the masterclass "Both Sides of the Table" (20-21 November 2026).

**Internal to EMC. Keep this repository private.** See "What must never go in this repository" below.

## If you only want to use it

Do not use the source folders. Download the latest package from the Releases page (`IFC-PS-Screening-Package-<version>.zip`) and follow the README inside it. The same guide is in [docs/participant/README.md](docs/participant/README.md).

## If you want to work on it

You need Python 3.9 or later and Node.js 18 or later. Then, in this folder:

```
python make.py all
```

That rebuilds the checklist and the Skill's copies from the rule set, runs every test, and writes the distributable files to `dist/`. Use `python make.py build`, `test` or `package` for one step at a time. On macOS or Linux, use `python3` if `python` is not found.

## What is where

| Path | What it is |
|---|---|
| `toolkit/ifc_ps_rules_v*.json` | **The rule set. The only place rules live.** Edit this |
| `toolkit/screen.py` | The screening engine |
| `toolkit/template.html` | The checklist page, with a placeholder for the rule set. Edit for design or behaviour changes |
| `toolkit/ifc-ps-screening-tool.html` | The built checklist. **Generated, do not edit** |
| `toolkit/build_html.py`, `make_triggers.py`, `make_exclusion.py` | Generators |
| `toolkit/test_cases.json`, `run_tests.py`, `parity.js` | The 20 reference cases, the test runner, and the check that the HTML and the engine give identical output |
| `skill/ifc-ps-screening/` | The Claude Skill, unzipped. `SKILL.md` and `references/*.md` are written by hand (except `triggers.md` and `exclusion-list.md`, which are generated). `scripts/screen.py` and `references/ifc_ps_rules.json` are copies made by `make.py build` |
| `docs/participant/` | The end-to-end guide, setup kits, the Project instructions text, links to the IFC documents |
| `docs/owner/` | The rule-set guide and the connector specification |
| `examples/` | Five ready-made cases to load into the checklist or paste into Claude |
| `CHANGES.md` | What changed in each version, and what is still open |
| `make.py` | Build, test and package |
| `.github/` | The pull request checklist and the automated check |

## How the checks protect the rule set

Every push and pull request runs `.github/workflows/check.yml`. It rebuilds the generated files and fails if they differ from what was committed (so nobody can change the HTML or the Skill's copy of the rules by hand), lints the rule set, runs the 20 reference cases for an exact match, and runs the parity test that compares the checklist and the engine on the complete output for thousands of generated cases.

## Contributing

Read [CONTRIBUTING.md](CONTRIBUTING.md). In short: change the rule set, run `python make.py all`, add a test case, open a pull request, and get an E&S lead's review before merging.

## What must never go in this repository

- Client names, deal details, information memoranda, ESIAs or real project cases. Examples must be invented or fully anonymised.
- Personal data.
- The IFC PDFs (the `.gitignore` blocks PDFs). Download them from ifc.org; links are in `docs/participant/DOWNLOAD_LINKS.md`.
- Passwords, tokens or API keys.

## Licence and terms

No open-source licence is attached. The package is provided for the professional use of masterclass participants and is not for resale or redistribution without EMC's written permission. Decide on a licence before making the repository public, if you ever do.

The Performance Standards, Guidance Notes, Sustainability Policy, FI Guidance Note and Exclusion List are IFC publications.
