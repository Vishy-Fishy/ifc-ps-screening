## What changed and why

<!-- One or two sentences. For a rule change, say what the IFC source says (document and paragraph) or that this is EMC judgement. -->

## Checklist

- [ ] I changed `toolkit/ifc_ps_rules_v*.json` (and not the built HTML or `skill/` copies by hand)
- [ ] I ran `python make.py all` and committed the files it changed
- [ ] I added or updated a case in `toolkit/test_cases.json` for the change
- [ ] Every new action has a paragraph citation, and anything that is EMC judgement is labelled as such
- [ ] I raised the version number (patch for wording, minor for new questions or flags, major for a new framework) and updated `CHANGES.md` and `skill/ifc-ps-screening/NOTICE.txt`
- [ ] An E&S lead has reviewed the change (name in the comments)
- [ ] No client names, deal details, personal data or IFC PDFs are included
