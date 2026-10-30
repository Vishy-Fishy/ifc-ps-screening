# Worked examples

These show the expected specificity and how the engine baseline and your own review fit together. Every NEEDS REVIEW names a checkable fact and an owner; every verdict is tied to the project's facts. In each example the first block is what the engine returns for the case (so what the checklist shows); the rest is what the skill adds.

## Example 1: 150 MW solar park, Jaisalmer district, Rajasthan

Facts: 300 ha of revenue land allotted by the state; local herders graze it. 33 km 220 kV line to a grid substation. About 600 construction workers, mostly contracted, in a temporary camp. Fund equity, lender applies Equator Principles.

Case: `sector` solar, `stage` greenfield, `country` IN. Yes: workforce, contractors, camps, supply chain, pollution (construction waste), water, communities nearby, heavy traffic, public-safety structures (line), security, labour influx, land, land users, access loss, legacy acquisition, natural habitat (grassland). No: retrenchment, GHG, pesticides, dam, relocation, living resources, critical heritage, commercial use of heritage. Not sure: protected area, species, ecosystem services, Indigenous Peoples, FPIC circumstances, scale of land loss, expropriation, known heritage, excavation.

**Engine baseline:** Category B. PS1 to PS6 TRIGGERED; PS7 and PS8 NEEDS REVIEW. Could move to A, confirm: scale of land loss (land-use survey), species presence (ecologist), customary claims (social specialist). No Environmental Clearance gate applies to solar, so the Performance Standards may be the only E&S assessment requirement.

**Skill review:**

| PS | Verdict | Why | What to do to conform |
|---|---|---|---|
| PS1 | TRIGGERED | Applies to every financed project | ESMS scaled to B (with a view to A); E&S assessment of plant and line; SEP; grievance mechanism |
| PS2 | TRIGGERED | 600 contracted workers in a camp; modules from a global supply chain | PS2 clauses in the EPC contract; camp to IFC/EBRD accommodation guidance (GN2-32); module supply chain traceability for forced labour risk (PS2 paras 27-29) |
| PS3 | TRIGGERED, low intensity | Panel-cleaning water in a water-stressed district; construction waste | Water source and dry or low-water cleaning; waste plan |
| PS4 | TRIGGERED | Heavy traffic on village roads; transmission line safety; labour influx | Traffic plan; line safety and clearances; worker code of conduct and disease-risk measures for the influx |
| PS5 | TRIGGERED | Allotted revenue land is grazed; economic displacement of herders | Livelihood survey with cut-off date; Livelihood Restoration Plan; legacy review of the state allotment; right-of-way compensation for the line |
| PS6 | TRIGGERED, high priority | Grassland is natural habitat; Jaisalmer overlaps Great Indian Bustard habitat and overhead lines are the documented threat | Critical habitat assessment by a specialist ecologist (PS6 paras 16-18); check the current Supreme Court position and the notified priority-area maps (see india-risk-flags.md) before relying on any verdict |
| PS7 | NEEDS REVIEW, low | Not a Scheduled Area; confirm no Scheduled Tribe customary users among the herders | Social specialist to check census data and herder communities |
| PS8 | NEEDS REVIEW | Desert region with scattered shrines and archaeological potential | Heritage walkover with communities; chance-find procedure if the screen says heritage is expected (PS8 para 8) |

The engine kept this at B because species presence is still "Not sure". Say what would change it: if the plant or line is inside a notified Great Indian Bustard priority area, the question is first one of whether the project can be permitted at all, then of categorisation (A). Do not raise to A on suspicion alone; raise when a fact supports it, and label it "Skill review".

**India-law comparison:** Solar PV and transmission lines are outside Environmental Clearance under the EIA Notification 2006, so the Performance Standards, through the lenders, may be the only framework requiring this project to assess grazing livelihoods or bustard habitat. RFCTLARR does not cover the herders' informal use of allotted land; PS5 does (for people with no legal claim: compensation for non-land assets, resettlement and livelihood restoration, not payment for the land).

**Open facts:** livelihood-use survey (social specialist); species presence along plant and line (ecologist); module supply chain traceability (procurement); line route in relation to notified bustard priority areas (developer).

First-pass screening only. It does not replace an ESDD, ESIA or ESMS, and the category is provisional.

## Example 2: IT services company, leased office, Pune

Facts: 800 employees; housekeeping and security outsourced; backup diesel generators; e-waste goes to authorised recyclers; growth equity from a fund.

Case: `sector` services, `stage` existing, `country` IN. Yes: workforce, contractors, pollution (e-waste, generators), security. No: every other question.

**Engine baseline:** Category C ("minimal or no adverse impacts on current answers"). PS1, PS2, PS3 and PS4 TRIGGERED; PS5 to PS8 NOT TRIGGERED. PS3 and PS4 are triggered at low intensity: ordinary e-waste and generator emissions, and outsourced guards. Neither blocks Category C in a low-risk sector.

**Skill review:**
- PS1: proportionate ESMS (policy, HR, OHS, grievance).
- PS2: direct staff; outsourced housekeeping and security workers are third-party workers (PS2 paras 24-26); POSH compliance.
- PS3 (low): authorised e-waste recyclers; generator emissions against consent conditions.
- PS4 (low): outsourced guards need conduct and training standards (PS4 para 12), through the security contractor's contract.
- PS5 to PS7 NOT TRIGGERED: leased office, no land acquisition, no community exposure beyond the building. PS8 NOT TRIGGERED: no excavation; a chance-find clause is only good practice if the company later builds.

Moves to B if the company operates its own data centre or campus construction (water, land, structural safety, and so on). If the user says the office has no guards or no generators, change those answers and re-run; PS3 and PS4 then show NOT TRIGGERED, still C.

## Example 3: 120 MW run-of-river hydropower, Kinnaur district, Himachal Pradesh

Facts: diversion weir, 10 km headrace tunnel, muck disposal on slopes, mix of private and forest land; Kinnaur is a Scheduled Area.

Case: `sector` hydro, `stage` greenfield, `country` IN. Yes: workforce, contractors, camps, pollution, communities nearby, public-safety structures, a dam whose failure could threaten communities, land, land users, natural habitat, Indigenous Peoples present, FPIC circumstances (customary forest use), known heritage, excavation. Not sure: relocation, species.

**Engine baseline:** Category A. Drivers: a dam whose failure could threaten communities (PS4 para 6); circumstances that require FPIC (PS7); a high-risk sector on a greenfield site. All eight standards TRIGGERED.

**Skill review:** key items are dam safety, glacial lake outburst and landslide risk with external expert review (PS4 para 6); land and forest-use livelihoods (PS5); river habitat, environmental flows and fish, with a critical habitat assessment (PS6 paras 16-18); FPIC given customary forest use, and how it relates to the Forest Rights Act gram sabha process (PS7 paras 13-17; check the current position on forest diversion); village deities and sacred sites (PS8 paras 6-10, and PS7 where they are Indigenous Peoples' heritage); cumulative impact assessment for the basin (PS1 para 8). Relocation is "Not sure": if any household has to move, a Resettlement Action Plan is added (PS5 paras 18-22).

## Example 4: new evidence arrives (changing an answer, not overriding a verdict)

After Example 1, the developer sends a species survey that finds no Great Indian Bustard, vultures or other qualifying species on the plant footprint or line route.

Do not simply write "PS6 not triggered". Change `p6_species` from "unsure" to "no", re-run the engine, and report what moved: the species watch item drops off the could-move-to-A list; PS6 stays TRIGGERED because grassland is natural habitat (PS6 paras 13-15); the category stays B. Say which answer changed, and cite the survey (author, date, method) as the evidence. If the survey is thin (one season, no line route), say that the answer is "no" on weak evidence and keep it on the open-facts list.

## Example 5: an infrastructure fund (financial intermediary)

Facts: a fund investing equity in Indian renewable energy, logistics and water companies; IFC is asked to commit general-purpose equity. A pipeline of projects, no portfolio breakdown yet.

Case: `sector` fi, `stage` existing, `country` IN. Answer the questions for a representative higher-risk investee: here a hydro or logistics-park developer, so land, workforce and contractors are "yes" and the rest "unsure".

**Engine baseline:** Category FI. The category line says IFC sets FI-1, FI-2 or FI-3 from the portfolio, which the checklist does not collect. PS1 lists the FI actions: ESMS fitting the portfolio, Exclusion List and national law screening, PS2 for the fund manager's own staff, Performance Standards applied to Higher Risk Transactions, the scope of application, annual reporting, and coal restrictions. PS3 to PS8 show what the representative investee would trigger.

**Skill review:**
- Exclusion List first: check each pipeline company and the fund's own sponsor for listed activities and the FI additions (forced and harmful child labour; logging in primary tropical moist forest; forestry products not from sustainably managed forests). Equity in a fund with general-purpose support: the scope is the whole portfolio originated after IFC's investment (Policy para 37; FI GN para 4). Existing investments are outside it (FI GN fn 5).
- Provisional sub-category: FI-1 if the pipeline holds substantial hydro, mining or similar exposure, FI-2 if it is mostly renewables, logistics and water with limited site-specific impacts and a very limited number of significant ones. State which and what would change it (Policy para 40).
- Higher Risk Transactions: equity into a hydro developer is one (resettlement, Indigenous Peoples, biodiversity). It must apply the relevant Performance Standards, with an ESAP; the fund manager needs the skills to screen and monitor them (FI GN paras 9, 34-35, 38, 49).
- Ask for: the portfolio and pipeline by sector, any coal exposure, the manager's existing E&S policy and ESMS. Gap-check them against FI GN paras 23-31.

