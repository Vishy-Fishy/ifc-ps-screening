# Categorisation

The categories are those of the IFC Policy on Environmental and Social Sustainability (1 January 2012), paragraph 40 (FI-1 to FI-3 and their treatment: paragraphs 35 and 44), also used by Equator Principles financial institutions and many funds. The definitions below follow that text. The Policy defines the categories in words; the rules that turn checklist answers into a category are **EMC judgement**, and so are the sector risk classes.

| Category | Meaning | What it usually requires |
|---|---|---|
| A | Potential significant adverse E&S risks or impacts that are diverse, irreversible or unprecedented | Full ESIA prepared by competent professionals with external experts for significant or technically complex issues, informed consultation and participation (PS1 paras 19, 31), independent review, detailed ESAP |
| B | Limited adverse risks or impacts, few in number, generally site-specific, largely reversible and readily addressed through mitigation | Focused assessment, ESMP, ESAP |
| C | Minimal or no adverse risks or impacts | ESMS proportionate to operations; often policy, labour and OHS only |
| FI-1 | FI portfolio with significant existing or proposed exposure to business activities with potential significant adverse risks (Category A-type sub-projects) | FI ESMS applying the Performance Standards to higher-risk sub-projects |
| FI-2 | Limited exposure (Category B-type), or a very small number of A-type activities | FI ESMS with sub-project screening and categorisation |
| FI-3 | Minimal or no adverse risks | Exclusion list and national law screening (a simple screening procedure counts as the ESMS) |

The engine returns the single value `FI` for a financial intermediary. Choosing FI-1, FI-2 or FI-3 needs the portfolio (type, size, sector exposure, tenor; Policy para 44), which the checklist does not collect: ask for it, or give a provisional sub-category labelled "Skill review" and say what would change it. See `fi-screening.md`.

How IFC categorises (Policy paras 41-44):

- **Use of proceeds known** (typical project finance): the category rests on the potential risks and impacts of the financed activity, including its known operational impacts for an existing operation, and also on the inherent risk of the sector and the setting (para 42). "Inherent" means before any management or mitigation (Policy fn 9), so do not lower a category because mitigation is planned.
- **Use of proceeds not fully specified, or a pre-development investment** (working capital, some equity): the category rests on the risks inherent in the sector and the setting (para 43), and IFC completes its due diligence after Board approval once the footprint is known. Where this is the case, say that the category is a sector-and-setting view.
- **FI with a specified end use**: the risk of that end use; **FI with general support**: the whole portfolio (para 44).

## How the engine reaches a category (rule set v1.2.0)

Rules are applied in this order; the first that matches wins.

1. **FI**: the sector is a financial intermediary.
2. **A**: any Category A signal (below).
3. **Not yet categorised**: no sector chosen, or fewer than 10 questions answered Yes or No ("Not sure" does not count). This stops a near-blank form from producing a confident B or C.
4. **C**: the sector is low risk (healthcare or education; services, IT or retail) and no "blocks C" question is answered Yes. Healthcare also loses C if the pollution question is Yes, because of medical waste. If any blocking question is still open or Not sure, the result says so.
5. **B**: everything else.

"Blocks C" questions are those where a Yes means more than ordinary office-type impacts: worker camps, forced-labour-risk supply chains, water-stress, high GHG, pesticides, heavy traffic, labour influx, all land and displacement questions, all biodiversity questions, Indigenous Peoples, and all heritage questions. Questions that do not block C because they are common in ordinary offices: workforce, contractors, retrenchment, ordinary waste and e-waste, nearby communities, building safety, security guards.

A solar park, wind farm or transmission line is a medium-risk sector, so it can only be B or A. Heavy, extractive, port, oil and gas, thermal, hydro and forestry sectors are high risk: greenfield projects start at A.

## Signals that push towards A

Any one of these, if confirmed, makes the engine return A. They are signals, not a definition: a project can still be A without them.

- Physical displacement of households (PS5), or displacement likely to affect many people or the main livelihood of many users (the last is EMC judgement)
- Habitat that may be critical habitat: Critically Endangered or Endangered species, endemic or restricted-range species, globally significant migratory or congregatory species, highly threatened ecosystems (PS6 para 16)
- Significant conversion of natural habitat near a legally protected or internationally recognised area (PS6)
- Circumstances requiring Free, Prior and Informed Consent of Indigenous Peoples (PS7 paras 13-16), including commercial use of their cultural heritage (PS7 para 17)
- A dam, tailings dam or ash pond in a location where failure could threaten communities (PS4 para 6)
- Critical cultural heritage that could be significantly damaged or removed (PS8 paras 13-14)
- A high-risk sector on a greenfield site, especially with cumulative impacts in the same basin or landscape

## Rules for stating the category

- Always call it provisional.
- Name the open fact that could move it. The engine's watch items are exactly these (for example "B, moves to A if the species presence check confirms Great Indian Bustard use of the line route").
- Do not downgrade because mitigation is planned. Categorise on potential impacts before mitigation.
- You may raise the engine's category if the facts justify it, and label it "Skill review". Never lower it without changing an answer and saying why (see SKILL.md).
- Where the use of proceeds is defined, categorise the financed activity (Policy para 42). Where it is not, categorise on the inherent risk of the sector and the setting (para 43), and say that IFC's due diligence may extend to the client's other business activities (para 26). If you categorise a corporate on its riskiest material operations, say that this is your approach.
- If asked where the rules come from, say: the category meanings are the Sustainability Policy's (para 40); the way checklist answers and sector classes are turned into a category is EMC judgement; the signals that cite paragraphs rest on Performance Standard text. The high-risk-greenfield signal is EMC's reading of Policy paras 42-43, which do not name sectors.
