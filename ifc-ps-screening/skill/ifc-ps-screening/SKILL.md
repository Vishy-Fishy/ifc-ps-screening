---
name: ifc-ps-screening
description: First-pass and deeper screening of a project, company or deal against the eight IFC Performance Standards (PS1-PS8), giving trigger verdicts, a provisional E&S category (A/B/C or FI), what the project must do to conform with paragraph citations, an India-law comparison and an escalation list; can also draft an ESAP, write a Word screening memo, or gap-check an uploaded ESIA, ESMP, ESMS or RAP. Continues a case copied from EMC's IFC PS screening checklist, or starts from a project description. Checks the IFC Exclusion List first and handles financial intermediaries (banks, NBFCs, funds). Use whenever someone describes a project (sector, location, land, workforce) and asks which Performance Standards apply, whether it needs ESDD, what the E&S risks or category are, how to become IFC-ready, or what an ESAP should contain; also for fund, bank, DFI or Equator Principles deal triage, even if IFC is not named. Not a substitute for a full ESDD, ESIA or ESMS, and the output says so.
---

# IFC Performance Standards screening

The first read a deal team, lender, developer or E&S consultant needs: which Performance Standards a project triggers, how serious the exposure is, and what the project must put in place to conform. Developed by Environmental Management Centre (EMC), Mumbai, from its ESDD practice, for participants of the masterclass "Both Sides of the Table".

The value of this skill is the judgement it adds on top of a rule set, not the format. A generic checklist clears a solar park on "vacant" government land outside any sanctuary; this method flags the grazing use (PS5) and the Great Indian Bustard habitat (PS6). Every verdict is tied to the project's facts, and every uncertainty names the fact that would resolve it.

## How this fits with the checklist

EMC's work is two-pronged:

1. **The HTML checklist** is the quick first pass. A person answers 33 Yes / No / Not sure questions and gets verdicts for PS1 to PS8, a provisional category and a list of actions, in minutes, offline.
2. **This skill** takes the same case further: it tests the answers against the project facts, adds depth (traps, regional red flags, India law, documents), cites paragraphs, and produces the memo, ESAP or gap check.

Both read one rule set, `references/ifc_ps_rules.json`. The bundled script `scripts/screen.py` applies it exactly as the checklist does, so the skill starts from the same verdicts the user saw. The checklist's "Copy case for Claude" button produces the input.

### The precedence rule

- The engine result is the **baseline**. Report it first and do not restate a baseline verdict from memory.
- You may **raise** a verdict or category when the project facts justify it (NOT TRIGGERED or NEEDS REVIEW to TRIGGERED; C to B; B to A). Label it: "Skill review: raised from B to A because the line route crosses Great Indian Bustard priority habitat."
- You may **never lower** a verdict silently. If the user gives new evidence that a trigger is not met (a negative species survey, a land schedule showing only voluntary purchases), change the answer in the case, re-run the engine, and say which answer changed and on what evidence. The verdict then moves because the answer moved.
- Order of severity: TRIGGERED > NEEDS REVIEW > NOT TRIGGERED > NOT SCREENED; A > B > C.

## Standards and sources

- The **IFC Performance Standards (1 January 2012)** are in force. The **Guidance Notes** are the 2012 edition, updated 14 June 2021; they explain the requirements but do not change them. Two further IFC documents sit behind the categories and the FI rules: the **Policy on Environmental and Social Sustainability (1 January 2012)** and the **Guidance Note on Financial Intermediaries (29 September 2023)**. IFC is reviewing its Sustainability Framework: dialogue runs to December 2026 and public consultation on draft proposals starts in January 2027. Nothing has been approved and no effective date is set. Do not apply draft provisions as requirements.
- **If the IFC documents are available** (uploaded in the chat or in project knowledge), search them before stating a requirement and cite the paragraph from the text. `references/paragraph-map.md` says which paragraph to look in.
- **If they are not available**, use the paragraph numbers carried by the rule set and conformance.md, which were checked against the 2012 text, and say "paragraph numbers per EMC rule set v1.2.0, not re-checked in this chat". If a point is not covered, cite the section heading and write "para to verify". Never guess a paragraph number.
- Keep requirement and guidance apart: Performance Standard text is a requirement; Guidance Notes, EHS Guidelines and good practice handbooks are guidance or benchmarks. Some actions in the rule set are marked as lender practice, not PS text (for example the Voluntary Principles on Security and Human Rights, which the PS4 text does not name). Keep that label.
- The meaning of each category follows the Sustainability Policy (para 40, and paras 42-44 on how to categorise). The sector risk classes, the way answers become a category, the minimum-answers rule and the sanity checks are **EMC judgement**: the Policy defines the categories in words and gives no scoring rule or sector list. Say so if the user asks where the category comes from. Cite the Policy as "Sustainability Policy para x" and the FI note as "FI Guidance Note para x".
- National law points come from `references/india-law.md` or an uploaded legal note. Label them "verify current text"; laws and notifications change.

## Workflow

### 1. Intake

Before anything else, compare the project and its sponsor with the **IFC Exclusion List** (`references/exclusion-list.md`). IFC does not finance listed activities, whatever the Performance Standards say. If one matches, say so first. If the position is uncertain, name the fact that decides it. The engine only reminds you; it cannot tell.

Start from whichever the user gives:

- **A case from the checklist** (JSON starting `{"tool": "EMC IFC PS screening tool", ...}`): save it as `case.json` (keep only `sector`, `stage`, `country`, `answers`; the other fields are for reference) and go to step 2. Read the project facts the user adds in conversation; they may justify raising a verdict in step 3.
- **A description, information memorandum, ESIA, maps or a land schedule**: extract the facts below, then build a case yourself.

| Fact | Drives |
|---|---|
| Sector, core activity, stage (greenfield, expansion, existing, acquisition), size and footprint | Overall risk, PS3 intensity, category |
| Location: country, state, district, land type | PS5, PS6, PS7, PS8 and national law |
| Land route: purchase, lease, government allotment, acquisition, right-of-way; any earlier acquisition | PS5 |
| Workforce: construction and operation, direct and contracted, migrant, accommodation; primary supply chains | PS2 |
| Emissions, effluent, waste, hazardous materials, water source, energy use | PS3 |
| Communities nearby, access roads, security, dams and other structures with public safety risk | PS4 |
| Protected areas, Key Biodiversity Areas, natural habitat, sensitive species | PS6 |
| Indigenous Peoples (India: Scheduled Tribes, Fifth or Sixth Schedule areas) | PS7 |
| Known heritage, excavation scale | PS8 |
| Financing route: IFC or DFI direct, Equator Principles bank, PE or infrastructure fund, FI | Applicability and category type |

Building a case from a description: the case needs a `sector` id, a `stage` id, `country` ("IN" for India, "OTHER" for anywhere else) and `answers` for the 33 question ids (`references/triggers.md` lists them with their wording).

- Answer **"yes"** only where a stated fact supports it. Answer **"no"** only where the user or a document says it is not the case, never because the description is silent. Answer **"unsure"** for anything the description does not settle, so that it surfaces as an open fact.
- Do not hold up the screening for missing facts. If something critical is missing, ask at most three short questions; otherwise screen and carry the gaps as "unsure". For a company or portfolio (not a single site), screen the main operating sites and say so.

### 2. Run the engine

```
python3 scripts/screen.py references/ifc_ps_rules.json case.json
```

(Paths are relative to this skill's folder.) The output is the baseline: category with its signals and watch items, a status for each standard with the reasons, actions (each with its citation), documents, open facts with owners, national-law lines, sanity warnings, the Environmental Clearance gate note, a sector note from the Sustainability Policy where one applies (oil, gas and mining; power distribution; water), and an `exclusion_check` reminder.

- If it prints "Case rejected", the message says which value is wrong (an unknown sector id, an answer that is not yes, no or unsure). Fix the case and run again.
- **Sanity warnings** mean an answer looks implausible for the sector (for example "No" to land for a solar park). Raise them with the user before relying on the verdict.
- If code cannot be run in this session, work through `references/triggers.md` and `references/categorisation.md` by hand, and say the verdicts were not machine-checked.

### 3. Deepen and challenge

For each standard, test the baseline verdict against the facts, using `references/triggers.md` (traps and sector intensity) and, for India, `references/india-risk-flags.md`. Where a trap or red flag applies and the baseline did not catch it, raise the verdict under the precedence rule. Give each verdict one line of reasoning tied to the project, never a restatement of the standard.

- **TRIGGERED**: a fact in hand brings the standard into play.
- **NEEDS REVIEW**: the facts cannot rule it in or out. Name the exact fact that would resolve it and who normally gets it (site team, land records, specialist ecologist, social specialist).
- **NOT TRIGGERED**: the facts rule it out. Say which facts.
- **NOT SCREENED**: no questions answered yet.

PS1 is always triggered. For PS8, a chance-find procedure is required where heritage is expected to be found (PS8 para 8); where there is ground disturbance but no indication, recommend one as good practice and say it is not a requirement.

### 4. Categorise

Read `references/categorisation.md`. State the engine's provisional category and the open item that could change it (the watch items). For a financial intermediary (bank, NBFC, fund, insurer) read `references/fi-screening.md`: the category is FI, FI-1 to FI-3 needs the portfolio, and the sub-project screen is the Performance Standards applied to Higher Risk Transactions. Physical displacement, critical habitat, circumstances requiring Free, Prior and Informed Consent, dams, tailings and ash ponds whose failure could threaten communities, critical cultural heritage, or a high-risk sector on a greenfield site push towards A.

### 5. Set out what is needed to conform

Use the engine's actions and documents, then read `references/conformance.md` for the full requirement set behind each standard. For each triggered standard give: the requirements that apply (with citations), the documents normally expected, and the actions for an Environmental and Social Action Plan. Scale to the category: do not ask a Category C office for a Biodiversity Action Plan.

### 6. National law comparison

For projects in India, add one line per relevant standard from `references/india-law.md` (the engine also returns a short line per standard): does domestic law already require an equivalent, or do the Performance Standards impose something it does not? State prominently, not in a footnote, when the sector is outside Environmental Clearance (solar, wind, transmission lines): the Performance Standards, through the financier, may then be the only E&S gate. For other countries, say that the national comparison has not been done unless the user supplies the law.

### 7. Produce the output

Templates are in `references/output-templates.md`. Choose by what the user asked:

- **Quick screen** (default in chat): category line, PS table, escalation list, national law comparison, open facts, limitations.
- **Screening memo** (when the user wants a report, a Word file or something to share or file): a Word document following the memo template. Use the docx skill if available.
- **ESAP draft**: action table with deliverable, owner, timing and acceptance criterion. Offer it as Word or Excel.
- **Gap check** (when the user uploads an ESIA, ESMP, ESMS manual, RAP, SEP or policy): requirement, what the document provides, gap, suggested fix.

Always show which verdicts came from the engine and which you raised. After a quick screen, offer the memo, an ESAP draft, or a gap check of any document the user has.

`references/worked-examples.md` shows the expected level of specificity. Read it before the first screening in a conversation.

## Conduct

- Do not invent project facts, species records, legal provisions or paragraph numbers.
- Be direct about risk. If the activity appears on the IFC Exclusion List (`references/exclusion-list.md`), say so first. The list changed on 8 December 2025 (radioactive materials removed); use the version in the reference.
- Do not give legal opinions; say where legal advice is needed.
- A narrative that fills gaps with confident prose is worse than a table that shows them. Keep unknowns visible in every output.
- Never lower an engine verdict without changing an answer and saying why.
- End every screening with: "First-pass screening only. It does not replace an ESDD, ESIA or ESMS, and the category is provisional."
