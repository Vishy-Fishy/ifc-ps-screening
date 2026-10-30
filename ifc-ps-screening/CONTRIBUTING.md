# Contributing

## The rules of the repository

1. **The rule set is the single source of truth.** Questions, actions, citations, sector risk classes, category rules, sanity checks, the Exclusion List text and the India-law lines all live in `toolkit/ifc_ps_rules_v*.json`. Never edit `toolkit/ifc-ps-screening-tool.html`, `skill/ifc-ps-screening/scripts/screen.py`, `skill/ifc-ps-screening/references/ifc_ps_rules.json`, `triggers.md` or `exclusion-list.md` by hand. `python make.py build` overwrites them, and the automated check fails if they are out of date.
2. **No change merges without review.** The rules decide what participants and funds are told about a project. An E&S lead reviews every rule change, and the reason is recorded in the pull request.
3. **Cite or label.** Every action needs a paragraph citation (`PSn para x`, `Sustainability Policy para x`, `FI Guidance Note para x`, `GNn-m`). If a rule is EMC's own judgement, label it as such (the question field `basis` is `EMC`, not `PS`). Do not present guidance or lender practice as a Performance Standard requirement.
4. **Nothing confidential.** No client names, real deals, personal data, or IFC PDFs.

## Making a change

1. Create a branch from `main` (for example `rules/add-psx-question`).
2. Edit the rule set JSON. For design or behaviour of the page, edit `toolkit/template.html`. For the Skill's method, edit `skill/ifc-ps-screening/SKILL.md` or the hand-written files in `references/`.
3. Raise the version inside the JSON and rename the file to match: patch (1.2.1) for wording, minor (1.3.0) for new questions or flags, major (2.0.0) for a new framework such as revised IFC Performance Standards. Update `CHANGES.md` and `skill/ifc-ps-screening/NOTICE.txt`.
4. Add a case to `toolkit/test_cases.json` for the change, with the exact expected result.
5. Run `python make.py all`. Fix anything that fails. Commit the files it changed, including the rebuilt HTML.
6. Open a pull request. The automated check must pass. Ask an E&S lead to review it, and tag a second person for any India-law line.
7. After merge, publish a release (below).

## Releasing

Run `python make.py package` on `main` (or download the `ifc-ps-screening-dist` artifact from the automated check). On GitHub, create a Release with the tag `v<rule set version>`, and attach `IFC-PS-Screening-Package-<version>.zip`, `ifc-ps-screening.zip` and `ifc-ps-screening-tool.html`. Participants download from the Release, not from the source folders.

## Reporting a wrong result

Open an issue. Say which example or case produced the result (paste the case from "Copy case for Claude"), what you expected, and why, with the paragraph if you know it. Do not include client details.

## Suggested GitHub settings (an admin does this once)

- Keep the repository **private**.
- Protect `main`: require a pull request, require the `check` workflow to pass, require at least one approval.
- Add a `CODEOWNERS` file naming the E&S lead for `toolkit/ifc_ps_rules_v*.json` and `skill/`, so GitHub requests their review automatically.
- Give non-technical reviewers read or triage access: they can review and comment in the browser.

## Things that are not code, and where to keep them

The Word documents in `docs/` are stored here for convenience, but Git cannot show what changed inside a Word file. If several people edit them, keep the working copy in your usual shared drive and commit the final version.
