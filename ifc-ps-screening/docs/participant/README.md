# IFC Performance Standards Screening Toolkit

Rule set 1.2.0, engine 1.2.0. Environmental Management Centre (EMC), Mumbai. October 2026.
Built for the masterclass "Both Sides of the Table: Masterclass on IFC Performance Standards" (20–21 November 2026), with Ekonnect Knowledge Foundation.

This is the start-to-finish guide. Read sections 1 to 5 to set up and use the toolkit. Sections 6 and 7 explain how the two tools work. Section 9 is for whoever owns and maintains the rules.

---

## 1. What this is

A project, company or deal can be screened against the eight IFC Performance Standards (PS1 to PS8) in two steps, using two tools that always agree with each other.

**Step 1: the HTML checklist.** One web page that works offline in any browser. You choose a sector, stage and country, then answer 33 Yes / No / Not sure questions. In seconds it shows which of PS1 to PS8 are triggered, a provisional environmental and social category (A, B, C or FI), the actions needed to conform with paragraph citations, the documents normally expected, and what still has to be confirmed.

**Step 2: the Claude Skill.** A package you add to your own Claude account. Give it the checklist result (one button copies it) plus whatever you know about the project. It starts from exactly the checklist's verdicts, then adds depth: traps and regional red flags, India-law comparison, citations, open facts with owners, and finished documents (a screening memo, an ESAP draft, or a gap check of an ESIA, ESMP or RAP).

**Why they always agree.** Both are built from one rule set file, `ifc_ps_rules_v1.2.0.json`. The HTML page is generated from it, and the Skill carries a copy and runs the same screening script. A test (the parity test) checks that the HTML and the script give identical output on thousands of generated cases.

**What it is not.** It is a first-pass screening aid. It does not replace an ESDD, ESIA or ESMS, the category is provisional, and it does not give legal advice.

---

## 2. What is in this package

| Folder / file | What it is |
|---|---|
| `README.md`, `README.docx` | This guide (the Word file has the same text) |
| `1_Quick_Checklist/ifc-ps-screening-tool.html` | The checklist: open it in a browser |
| `2_Claude_Skill/ifc-ps-screening.zip` | Upload this to Claude as a Skill (do not unzip it) |
| `2_Claude_Skill/IFC_PS_Skill_Setup_Kit.docx` | Participant guide for installing and using the Skill |
| `3_Optional_Claude_Project/IFC_PS_Assistant_Setup_Kit.docx` | Guide to building a Claude Project with the IFC PDFs |
| `3_Optional_Claude_Project/IFC_PS_Assistant_Instructions.txt` | The instructions to paste into that Project |
| `4_Official_IFC_Documents/DOWNLOAD_LINKS.md` | Where to download each IFC document yourself |
| `5_Example_Cases/` | Five ready-made cases (.json) to load into the checklist or paste into Claude |
| `6_For_The_Rule_Set_Owner/ifc_ps_rules_v1.2.0.json` | The rule set: the single source of truth |
| `6_For_The_Rule_Set_Owner/screen.py` | The screening engine (Python) |
| `6_For_The_Rule_Set_Owner/template.html`, `build_html.py` | Build the checklist from the rule set |
| `6_For_The_Rule_Set_Owner/make_triggers.py`, `make_exclusion.py` | Regenerate the Skill's `triggers.md` and `exclusion-list.md` from the rule set |
| `6_For_The_Rule_Set_Owner/ifc-ps-screening-tool.html` | The built checklist (same as folder 1) |
| `6_For_The_Rule_Set_Owner/test_cases.json`, `run_tests.py` | 20 reference cases and the test runner |
| `6_For_The_Rule_Set_Owner/parity.js` | Checks that the HTML and the engine agree |
| `6_For_The_Rule_Set_Owner/CHANGES.md` | What changed in 1.2.0 and what is still open |
| `6_For_The_Rule_Set_Owner/IFC_PS_Rule_Set_Guide.docx` | Explains the rule set, test results and change control |
| `6_For_The_Rule_Set_Owner/IFC_PS_Connector_Specification.docx` | The plan for a later hosted connector (Step 3) |

### What is inside the Claude Skill (`ifc-ps-screening.zip`)

| File | What it contains |
|---|---|
| `SKILL.md` | The method: intake, run the engine, deepen and challenge, categorise, conformance, national law, outputs, conduct rules, and the precedence rule |
| `scripts/screen.py` | The engine. Applies the rule set to a case and returns verdicts, category, actions with citations, warnings |
| `references/ifc_ps_rules.json` | The rule set (same file as in folder 6) |
| `references/triggers.md` | The 33 trigger questions with ids, paragraph references, common traps, sector intensity guide (generated from the rule set) |
| `references/categorisation.md` | What categories A, B, C and FI-1 to FI-3 mean (Sustainability Policy para 40), how IFC categorises, the signals that push towards A, rules for stating a category |
| `references/conformance.md` | For each Performance Standard: paragraphs to cite, core requirements, documents expected, typical ESAP actions |
| `references/paragraph-map.md` | Where each topic sits in the Performance Standards, the Sustainability Policy and the FI Guidance Note |
| `references/exclusion-list.md` | The IFC Exclusion List (amended 8 December 2025) and the extra exclusions for financial intermediaries |
| `references/fi-screening.md` | Banks, NBFCs, funds and insurers: FI-1 to FI-3, Higher Risk Transactions, scope, reporting |
| `references/india-law.md` | Indian instruments compared with each Performance Standard; the Environmental Clearance gap |
| `references/india-risk-flags.md` | Regional red flags: species, Scheduled Areas, land, water, supply chain labour |
| `references/output-templates.md` | Quick screen, Word screening memo, ESAP table, gap check table |
| `references/worked-examples.md` | Five worked examples, including a new-evidence case and a fund |
| `NOTICE.txt` | Version, terms of use, limitations |

---

## 3. What you need

**To use the checklist:** a computer, tablet or phone with any modern browser. No account, no internet, no installation.

**To use the Skill:** a Claude account (Free, Pro, Max, Team or Enterprise; Pro or higher is recommended for long documents), with code execution turned on, because the Skill runs its screening script. Skills you upload are private to your account.

**Optional, for the Claude Project:** the official IFC documents downloaded from ifc.org (section 4, step D). A Claude Project is a separate, optional layer that lets Claude quote exact paragraphs from the PDFs.

**To maintain the rule set (owners only):** Python 3 and Node.js 18 or later. The checklist itself needs neither.

**Facts about the project.** The minimum is a sector, a stage and country, and answers to the questions. Section 5 lists what to gather and who usually holds it.

---

## 4. Set up (about 30 minutes)

**A. Unzip this package** to a folder on your computer.

**B. Checklist.** Double-click `1_Quick_Checklist/ifc-ps-screening-tool.html`. It opens in your browser. There is nothing to install. You can email or share the single file. Answers are saved in your browser on that device only; they are not sent anywhere.

**C. Claude Skill.**
1. In Claude (desktop app or claude.ai), check that code execution is enabled in your settings.
2. Open Customize, then Skills.
3. Choose + (Create skill), then Upload a skill, and select `2_Claude_Skill/ifc-ps-screening.zip` exactly as supplied. Do not unzip or rename it: the folder name inside must match the skill name.
4. Check the Skill appears in your list and is switched on.
5. Test: start a new chat and type *Screen this project against the IFC Performance Standards: a 150 MW solar park in Jaisalmer on grazed revenue land, with a 33 km 220 kV line.* If Claude does not seem to use the Skill, say "Use the IFC PS screening skill."

To update later, delete the old Skill and upload the new zip. (Menu names may change as Claude is updated; `IFC_PS_Skill_Setup_Kit.docx` has the same steps.)

**D. Download the official IFC documents (optional but recommended).** The links are in `4_Official_IFC_Documents/DOWNLOAD_LINKS.md`. Download them yourself so you always have current versions. They are IFC publications and are not included here.

**E. Claude Project (optional).** Follow `3_Optional_Claude_Project/IFC_PS_Assistant_Setup_Kit.docx`: create a Project named *IFC PS Screening Assistant*, paste in the text of `IFC_PS_Assistant_Instructions.txt`, and upload the IFC documents from step D. Then start your screening chats inside that Project. The Skill gives the method; the Project gives the exact paragraph text. Used without the Project, the Skill still screens, but marks paragraph numbers as "per EMC rule set, not re-checked in this chat".

**F. Try the examples.** Open the checklist, open "Load a saved case" under the buttons, paste the contents of any file in `5_Example_Cases/`, and press Load. The result should match what is written in section 8.

---

## 5. Using it, start to finish

1. **Gather the facts** (table below). Do not wait for everything; the tool is built to show what is missing.
2. **Check the Exclusion List first.** Is the project, or its sponsor, engaged in any activity IFC does not finance (illegal products, weapons, most alcohol, tobacco, gambling, unbonded asbestos, drift-net fishing, and for FIs extra exclusions)? The checklist shows a reminder on every result with the full list one click away. The tool cannot judge this for you.
3. **Fill in the checklist.** Project name, sector, stage, location, then the questions. Answer Yes only where a fact supports it. Answer No only where you know it is not the case. Answer Not sure for everything else: it then appears as an open fact. Never answer No just because nothing was said.
4. **Read the result.** The strip at the top shows PS1 to PS8. The category card shows what drives it and what could move it to Category A. Read any "Check these answers" warnings: they mean an answer looks implausible for the sector.
5. **Hand it to Claude.** Press **Copy case for Claude**. Open a chat with the Skill on (inside the Project if you set one up) and paste. Add what you know: an information memorandum, a project summary, a land schedule, an ESIA, a map.
6. **Let Claude deepen it.** It runs the same rules, reports the checklist baseline first, then adds depth. If it raises a verdict it says why, for example "Skill review: raised from B to A because the line route crosses priority bustard habitat".
7. **Close the open facts.** The result lists each open fact and who normally gets it (site team, land records, specialist ecologist, social specialist). When new evidence arrives, change the answer in the checklist (or tell Claude which answer changed), and re-run. The verdict moves because the answer moved.
8. **Produce the output.** Ask for what you need: a quick screen (the default), a Word screening memo, an ESAP draft with owners and timing, or a gap check of an uploaded ESIA, ESMP, ESMS manual, RAP or policy.
9. **Verify before relying on it.** Open the source for any citation you will rely on. Have a lawyer check the India-law lines. The category is a hypothesis for the deal team, not a determination.

### What to have ready

| Fact | Why it matters | Who usually has it |
|---|---|---|
| Sector, core activity, size and footprint, stage (greenfield, expansion, existing, acquisition) | Sector risk, category, PS3 intensity | Developer, information memorandum |
| Country, state, district, land type | PS5 to PS8 and national law | Developer, project summary |
| How land is secured (purchase, lease, government allotment, acquisition, right-of-way) and any earlier acquisition | PS5 | Land records, developer, legal |
| Who uses the land (farming, grazing, fuelwood, fishing), including government or "vacant" land | PS5 | Social specialist, land-use survey |
| Workforce: construction and operation, direct and contracted, migrants, camps; key supply chains | PS2 | Developer, EPC contractor, procurement |
| Emissions, effluent, waste, hazardous materials, water source and demand, energy use | PS3 | Process engineer, developer |
| Nearby settlements, access roads, heavy traffic, security guards, dams, tailings, ash ponds or other structures whose failure could harm the public | PS4 | Site team, design engineer |
| Protected areas, Key Biodiversity Areas, natural habitat, sensitive species | PS6 | Specialist ecologist (IBAT or equivalent screen) |
| Indigenous Peoples present (in India: Scheduled Tribes, Fifth or Sixth Schedule areas), customary use, forest rights | PS7 | Social specialist, census data |
| Known heritage near the site, scale of excavation | PS8 | Heritage specialist, site team |
| Financing route (IFC or DFI direct, Equator Principles bank, fund) | Which rules apply | Deal team |
| For a bank, NBFC, fund or insurer: use of proceeds, sector and product breakdown of the portfolio, any coal exposure, existing E&S policy and ESMS | FI category and scope | The FI |

---

## 6. How the checklist works

**Inputs.** Project name (optional), sector (18 to choose from), stage (greenfield, expansion, existing operations, acquisition of a company), location (India or another country), and 33 questions across PS2 to PS8: five on labour (PS2), four on pollution and resources (PS3), six on community health, safety and security (PS4), seven on land (PS5), five on biodiversity (PS6), two on Indigenous Peoples (PS7) and four on heritage (PS8). PS1 has no questions: it applies to every project.

**Verdict for each standard.**
- Triggered: at least one question for that standard is answered Yes.
- Not triggered: every question for that standard is answered No.
- Not screened: none of its questions has an answer yet.
- Needs review: anything else (Not sure, or a mix of No and unanswered). Each one names the fact that would settle it and who gets it.
- PS1 is always Triggered; its actions are scaled to the category.

Triggered standards show why (with the paragraph), what to do to conform, and the documents normally expected. Needs-review standards show what to confirm and what would follow if triggered. For India, each standard also shows one line comparing Indian law with the Performance Standard, and for solar, wind and transmission it flags that these sit outside India's Environmental Clearance, so the financier's Performance Standards may be the only E&S gate.

**Provisional category.** The first rule that matches wins:
1. Sector is a financial intermediary: **FI**.
2. Any A-signal: **A**.
3. No sector, or fewer than 10 Yes or No answers ("Not sure" does not count): **not yet categorised**.
4. Low-risk sector (healthcare or education; services, IT or retail) and no question that "blocks C" answered Yes: **C**.
5. Everything else: **B**.

A-signals are: relocation of households; large-scale loss of land or livelihoods; possible critical habitat (species); circumstances requiring Free, Prior and Informed Consent; a dam, tailings dam or ash pond whose failure could threaten communities; critical cultural heritage; natural habitat altered near a protected area; commercial use of Indigenous Peoples' heritage; and a high-risk sector on a greenfield site. For B and C results, any of these questions not yet answered No appears as "Could move to Category A. Confirm:".

The meaning of each category is IFC's (Sustainability Policy para 40). How answers become a category, and the sector risk classes, are EMC judgement: the Policy has no sector list or scoring rule.

**Warnings.** If an answer looks implausible for the sector (for example No to land for a solar park, No to a dam for hydropower, No to pollution for thermal power), the page says "Check these answers".

**Buttons.**
- Copy summary: plain text of the result, with all answers, to paste into an email or note.
- Copy case for Claude: a JSON block with your answers and the checklist result, for step 5 above.
- See actions: jumps to the cards for each standard.
- Clear answers: press twice to wipe the form.
- Load a saved case: paste a case copied earlier (or from `5_Example_Cases`) and press Load. An invalid case is refused with a message.

**Privacy.** Everything runs in your browser. Nothing is sent over the internet. Answers are kept in your browser's local storage only, and the page works if storage is blocked.

---

## 7. How the Skill works

**What it adds.** The checklist is deliberately simple. The Skill adds judgement: it tests the answers against the project facts, spots traps the checklist cannot (for example that "vacant" government land is often grazed, or that species habitat extends beyond notified boundaries), adds India regional red flags and India law, cites paragraphs, and writes documents.

**The workflow it follows** (from `SKILL.md`):
1. Intake. From a pasted checklist case, or from a description or document, it extracts the facts and, if starting from a description, builds a case itself. It answers Yes only where a fact supports it, No only where it is ruled out, and Not sure otherwise. It asks at most three short questions.
2. It checks the IFC Exclusion List.
3. It runs the bundled engine `scripts/screen.py` on the case. This gives the baseline: category, verdicts, actions with citations, open facts, warnings.
4. It deepens and challenges each standard, using the traps in `triggers.md` and the red flags in `india-risk-flags.md`.
5. It categorises, reading `categorisation.md` (and `fi-screening.md` for banks and funds).
6. It sets out what is needed to conform, using `conformance.md`.
7. It adds the national-law comparison.
8. It produces the output you asked for, using `output-templates.md`.

**The precedence rule.** The engine result is the baseline and is reported first. The Skill may raise a verdict or category when the facts justify it, and must label it ("Skill review: raised from B to A because ..."). It never lowers one silently. If you give it evidence that a trigger is not met, such as a negative species survey, it changes that answer in the case, re-runs the engine, and says which answer changed and on what evidence. The order of severity is Triggered above Needs review above Not triggered above Not screened, and A above B above C.

**Where its citations come from.** If the IFC documents are in the chat or the Project, it searches them and cites the paragraph from the text. If not, it uses the paragraph numbers carried by the rule set (checked against the 2012 text) and says they were not re-checked in this chat. It keeps requirement (Performance Standard text) apart from guidance (Guidance Notes, EHS Guidelines) and lender practice, and labels each.

**Outputs.**
- Quick screen (default in chat): category line, a table of PS | verdict | why | what to do | source, escalation list, national-law comparison, open facts, limitations.
- Screening memo: a Word document (executive summary, project description, standard-by-standard assessment, categorisation rationale, ESAP summary).
- ESAP draft: actions with deliverable, owner, timing and acceptance criterion.
- Gap check: requirement, what your document provides, gap, suggested fix.

It always ends with: *First-pass screening only. It does not replace an ESDD, ESIA or ESMS, and the category is provisional.*

**If code cannot be run** in a session, the Skill works through `triggers.md` and `categorisation.md` by hand and says the verdicts were not machine-checked.

**What you can paste.** The simplest input is the JSON from Copy case for Claude. A case needs `sector`, `stage`, `country` ("IN" or "OTHER") and `answers`, with each answer "yes", "no" or "unsure". Anything else is rejected with a message saying which value is wrong; it is never silently misread. Example:

```json
{
 "tool": "EMC IFC PS screening tool",
 "rule_set_version": "1.2.0",
 "project": "150 MW solar park, Jaisalmer",
 "sector": "solar",
 "stage": "greenfield",
 "country": "IN",
 "answers": { "p5_land": "yes", "p5_users": "yes", "p6_species": "unsure" },
 "html_result": { "category": "B", "statuses": { "1": "trig", "5": "trig", "6": "review" } }
}
```

You can also run the engine yourself on any computer with Python 3: `python3 screen.py ifc_ps_rules_v1.2.0.json case.json`.

---

## 8. Check your setup with the example cases

Load each file in `5_Example_Cases/` into the checklist ("Load a saved case") and compare.

| Example | Expected result |
|---|---|
| 1. 150 MW solar park, Jaisalmer, grazed revenue land | Category B, with Category A watch items (scale of land loss, species, FPIC). PS1 to PS6 triggered, PS7 and PS8 need review. Flags that solar is outside Environmental Clearance |
| 2. IT company, leased office, Pune | Category C. PS1 to PS4 triggered (PS3 and PS4 at low intensity: e-waste and security guards); PS5 to PS8 not triggered |
| 3. 120 MW run-of-river hydropower, Kinnaur | Category A (dam, FPIC and high-risk greenfield). All eight standards triggered |
| 4. Example 1 after a negative species survey | The species item is answered No. The species watch item drops off the list; PS6 stays triggered because grassland is natural habitat; category stays B |
| 5. Infrastructure fund (FI) | Category FI, with the FI actions under PS1 and the FI wording of the Exclusion List check. FI-1, FI-2 or FI-3 needs the portfolio |

In the Skill, paste the same case and ask it to screen further; it should report the same checklist result first.

---

## 9. For whoever owns the rule set

**The rule of one.** The rule set JSON is the only place rules live. Never edit the HTML or the Skill's copy of the rules by hand. EMC keeps the source in a Git repository, where one command (`python make.py all`) does steps 2 to 3 and 5 below and builds a new package; ask EMC for access, or to raise a change.

**To change a rule** (folder `6_For_The_Rule_Set_Owner`, needs Python 3 and Node.js 18+):
1. Edit `ifc_ps_rules_v1.2.0.json` (question wording, actions and citations, sector risk class, category rules, sanity checks, the Exclusion List text, India-law lines). Raise the version number inside the file, and rename the file to match.
2. Run `python3 -I build_html.py` to rebuild the checklist.
3. Run `python3 -I run_tests.py` (lints the rule set, runs the 20 reference cases for exact match, and checks input handling) and `node parity.js` (checks that the HTML and the engine agree on the complete output).
4. Add a test case for every rule change to `test_cases.json`.
5. Copy the new rule set to the Skill as `references/ifc_ps_rules.json` and the new `screen.py` to `scripts/`, regenerate `references/triggers.md` and `references/exclusion-list.md` with `python3 make_triggers.py <rules> <output>` and `python3 make_exclusion.py <rules> <output>`, update `NOTICE.txt`, re-zip the Skill with the folder name `ifc-ps-screening`, and redistribute.
6. An EMC E&S lead approves each change and records the reason.

**Version numbers.** Patch for wording (1.2.1), minor for new questions or flags (1.3.0), major for a new framework such as revised IFC Performance Standards (2.0.0). `IFC_PS_Rule_Set_Guide.docx` has the structure of the rule set, the test results and the change-control process.

**Keep watching IFC.** IFC is reviewing its Sustainability Framework. Phase I dialogue runs to December 2026, and public consultation on draft proposals starts in January 2027. Nothing is approved and no effective date is set. The 2012 Performance Standards remain in force and draft provisions are not applied. The IFC Exclusion List was amended on 8 December 2025 (radioactive materials removed) and applies to transactions mandated after 31 December 2025; check the page from time to time.

---

## 10. Troubleshooting

| Problem | What to do |
|---|---|
| Claude does not use the Skill | Say "Use the IFC PS screening skill." Check the Skill is switched on and code execution is enabled |
| Upload of the Skill fails | Upload the zip as supplied. Do not unzip or rename it |
| "Case rejected" | The message names the bad value: an unknown sector or stage id, or an answer that is not yes, no or unsure. Fix it and run again |
| Category shows "Not yet categorised" | Choose a sector and answer at least 10 questions with Yes or No ("Not sure" does not count) |
| "Check these answers" warning | An answer looks implausible for the sector. Check it with the project team before relying on the verdict |
| Paragraph numbers marked "not re-checked" | The IFC documents are not in the chat. Add them (Project knowledge) and ask again, or open the source yourself |
| The checklist lost my answers | They are stored in that browser on that device only. Use Copy case for Claude to save a case to a file |
| A PS shows Triggered when you think it should not | Check the question: a Yes on the land question triggers PS5 conservatively, although voluntary purchases are outside PS5 (para 6). The action asks you to show each parcel was voluntary |

---

## 11. Limits and what is still open

- First-pass screening only. Not a substitute for an ESDD, ESIA or ESMS. The category is provisional.
- The meaning of the categories follows IFC's Sustainability Policy. The sector risk classes, the way answers become a category, the minimum of 10 answers and the sanity checks are EMC judgement.
- India-law lines are general knowledge as of October 2026 and need a legal check. The Forest Rights Act and 2022 forest rules point is unverified.
- The December 2025 Great Indian Bustard judgment is known only from a news report. Check it against the order.
- FI-1, FI-2 or FI-3 cannot be chosen without a portfolio breakdown, which the checklist does not collect.
- The rules have not yet been tested against EMC's past ESDD verdicts. This is the most valuable next step.

---

## 12. Sources and terms

Rules and citations were checked against: IFC Performance Standards on Environmental and Social Sustainability (1 January 2012); Guidance Notes (2012, updated 14 June 2021); IFC Policy on Environmental and Social Sustainability (1 January 2012); IFC Guidance Note on Financial Intermediaries (29 September 2023); the IFC Exclusion List (as amended 8 December 2025, text supplied by EMC from ifc.org). The IFC documents are IFC publications; download them from ifc.org.

Provided for the professional use of masterclass participants. Not for resale or redistribution without EMC's written permission.
