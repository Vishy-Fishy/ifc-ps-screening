# Trigger questions, traps and intensity

Generated from rule set v1.2.0. These are the same 33 questions, in the same words, as EMC's HTML checklist, so a screen done in chat and one done with the checklist reach the same verdicts. Each line gives the question id (use it as the key in a case file), the Performance Standard paragraphs it rests on, and flags: **A** = a Yes is a Category A signal; **blocks C** = a Yes rules out Category C; **EMC** = EMC practice or judgement rather than Performance Standard text.

## How answers become verdicts

- Any **Yes** in a standard triggers it. All **No** clears it. No answers at all leaves it **not screened**. Anything else (Not sure, or a mix of No and unanswered) is **needs review** and becomes an open fact.
- PS1 is always triggered.
- A category is given only when a sector is chosen and at least 10 questions are answered Yes or No (Not sure does not count). A Category A signal can show earlier.
- Category order: FI sector first; then A if any A signal; then "not yet categorised" if the sector is missing or there are too few answers; then C if the sector is low risk and no "blocks C" question is answered Yes; otherwise B.
- Every A-signal question not answered No becomes a "could move to A" item on a B or C result.
- Sanity checks: if an answer looks implausible for the sector (for example No to land for a solar park), the engine returns a warning. Raise it with the user.

## PS1 Assessment and management of environmental and social risks and impacts

Always triggered for a project financed under the Performance Standards. The question is how substantial the ESMS must be, which follows the category.

## PS2 Labour and working conditions

- `p2_workers` (PS2 paras 5–7) Will the project employ workers, directly or through contractors, during construction or operation?
- `p2_contract` (PS2 paras 11, 24–26; GN2-71 to GN2-73) Will a large share of the work be done by contractors, subcontractors or migrant workers?
- `p2_camps` (PS2 para 12; GN2-32) [blocks C] Will workers live in camps or project-provided accommodation?
- `p2_supply` (PS2 paras 27–29) [blocks C] Do primary suppliers come from sectors with known forced labour, child labour or serious safety risks (for example polysilicon, cotton, bricks, mica, seafood)?
- `p2_retrench` (PS2 paras 18–19) Are layoffs or collective retrenchment planned, for example after an acquisition or restructuring?

Trap: screening only direct employees. PS2 reaches workers engaged by third parties (paras 24-26) and, where risks are known, the primary supply chain (paras 27-29). For acquisitions, retrenchment is often the main PS2 issue.
Camps: the IFC/EBRD Workers' Accommodation guidance is referred to in Guidance Note 2 (GN2-32). Migrant workers: the Guidance Note says clients may not retain workers' identity documents (GN2-71) and should avoid practices that create unpayable debt (GN2-72).

## PS3 Resource efficiency and pollution prevention

- `p3_pollution` (PS3 paras 10–13) Will the project release air emissions, wastewater or waste, or use or store hazardous materials?
- `p3_water` (PS3 para 9) [blocks C] Will the project draw significant amounts of water, or is it in a water-stressed area?
- `p3_ghg` (PS3 paras 7–8) [blocks C] Are direct emissions plus emissions from purchased energy likely to exceed 25,000 tonnes CO₂-equivalent a year?
- `p3_pest` (PS3 paras 14–17) [blocks C] Will pesticides or other agrochemicals be used?

Trap: treating PS3 as triggered or not. It applies to almost every physical project; what matters is intensity. State it.
GHG: PS3 para 8 asks the client to quantify emissions annually where the project is expected to produce more than 25,000 tCO2e a year. It does not itself require public reporting.
Pesticides: WHO Class Ia and Ib products are not to be purchased, stored, used, manufactured or traded; Class II only where there are controls and trained handlers (para 17).

## PS4 Community health, safety and security

- `p4_near` (PS4 paras 5, 9–10) Do communities live close to the site or along its access roads?
- `p4_traffic` (PS4 paras 6–7) [blocks C] Will heavy vehicles use public roads, or will hazardous materials be transported?
- `p4_infra` (PS4 para 6) Does the project include structures or buildings the public will use, or whose failure could endanger the public (tanks, pipelines, transmission lines, bridges, tall buildings)? Dams, tailings dams and ash ponds are asked separately.
- `p4_dam` (PS4 para 6) [A, blocks C] Does the project include a dam, tailings dam or ash pond in a location where its failure could threaten communities (settlements downstream, steep terrain, seismic zone)?
- `p4_security` (PS4 paras 12–14) Will private security guards or public security forces protect the site?
- `p4_influx` (PS4 para 10; GN4-18 to GN4-20) [blocks C] Will many outside workers arrive compared with the local population?

NOT TRIGGERED is defensible only for sites with no community proximity, no public road use, no security and no public-safety structures. Say why.
Dams, tailings dams and ash ponds in high-risk locations need review by external experts separate from the designers, from early design through decommissioning (para 6). This is a Category A signal in this rule set.
Labour influx: the PS4 text (para 10) covers communicable disease. Controls on gender-based violence and sexual exploitation are lender practice; label them that way.
Security: PS4 paras 12-14 set the requirements (proportionality, vetting, training, grievance mechanism). The Voluntary Principles are a common benchmark but the PS text does not name them.

## PS5 Land acquisition and involuntary resettlement

- `p5_land` (PS5 paras 5–6) [blocks C] Does the project need land that is not already built-up premises leased on the open market: new land, a purchase, a long lease, a right-of-way or an easement?
- `p5_users` (PS5 paras 5, 17, 23; PS5 fn 8) [blocks C] Do people live on, farm, graze or collect resources from that land, including government or ‘vacant’ land?
- `p5_relocate` (PS5 paras 18–22) [A, blocks C] Will any households have to move their homes or structures?
- `p5_scale` (PS5 paras 25–29) [A, blocks C, EMC] Is the loss of land or land access likely to affect many people, whole communities, or the main livelihood of many users?
- `p5_expro` (PS5 paras 5, 30–31) [blocks C] Is the government acquiring the land, or could it expropriate if negotiations fail?
- `p5_access` (PS5 para 5) [blocks C] Will people lose access to grazing land, forests, fishing grounds or other natural resources?
- `p5_legacy` (PS1 para 9; PS5 paras 30–31) [blocks C, EMC] Was land for this project acquired earlier by the government or a previous owner?

Traps:
- "The land is government wasteland" does not clear PS5. Revenue, gauchar (grazing) and common land is often used informally. Ask for a land-use and livelihood survey.
- PS5 does not apply to voluntary transactions: the seller is not obliged to sell and the buyer cannot resort to expropriation if talks fail (para 6). It also does not apply where land use is not changing. The checklist therefore asks you to show voluntariness parcel by parcel; where expropriation powers stand behind the negotiation (para 5), treat it as involuntary.
- People with no legal right or recognisable claim are not paid for the land, but are offered resettlement with security of tenure, compensation for non-land assets owned before the cut-off date, and help to restore livelihoods (para 22 and footnote 8). People who arrive after a published cut-off date need not be compensated (para 23).
- Linear projects (transmission, roads, pipelines) create many small impacts: right-of-way, tower footprints, crop damage, access restrictions.
- Legacy acquisition by a state agency (industrial parks, solar parks) needs a legacy review and, where there are gaps, a corrective action plan. This is lender practice anchored in PS1 para 9 (third-party risks) and PS5 paras 30-31.

## PS6 Biodiversity conservation and sustainable management of living natural resources

- `p6_protected` (PS6 para 20 and fn 17) [blocks C] Is the site within or near a legally protected area or an internationally recognised area (UNESCO Natural World Heritage Site, Man and the Biosphere reserve, Key Biodiversity Area, Ramsar wetland), or an eco-sensitive zone? About 10 km is a screening distance, not a PS rule.
- `p6_natural` (PS6 paras 13–15) [blocks C] Will the project clear or alter natural habitat (forest, grassland, wetland, river, mangrove, coast)?
- `p6_species` (PS6 paras 16–19) [A, blocks C] Could the site hold critical habitat: habitat that matters for Critically Endangered or Endangered species, endemic or restricted-range species, large concentrations of migratory or congregatory species (flyways, stopovers), or highly threatened ecosystems? Examples: Great Indian Bustard, vultures, elephant corridors.
- `p6_living` (PS6 paras 26–30) [blocks C] Does the project produce or buy living natural resources (crops, timber, palm oil, fish, aquaculture)?
- `p6_services` (PS6 paras 24–25; PS4 para 8) [blocks C] Do local communities depend on ecosystems the project could affect (water, fuelwood, fisheries, flood protection)?

Traps:
- Screening only against notified protected-area boundaries. Critical habitat (para 16) is defined by biodiversity value, not by legal boundary: habitat of significant importance to Critically Endangered or Endangered species, endemic or restricted-range species, globally significant concentrations of migratory or congregatory species, highly threatened or unique ecosystems, or key evolutionary processes. Where the region has documented sensitive-species risk (see india-risk-flags.md), mark NEEDS REVIEW or TRIGGERED and call for a critical habitat assessment.
- "Internationally recognised areas" in PS6 means UNESCO Natural World Heritage Sites, UNESCO Man and the Biosphere reserves, Key Biodiversity Areas and Ramsar wetlands (para 20, footnote 17). The 10 km screening distance is an EMC heuristic, not a PS rule.
- Grasslands and drylands are often treated as "wasteland" although they are natural habitat.
- For rivers (hydropower, water abstraction), consider downstream flows and fish passage, not only the footprint.

## PS7 Indigenous Peoples

- `p7_present` (PS7 paras 4–8) [blocks C] Are Indigenous Peoples present in or using the project area (in India, Scheduled Tribes or Adivasi communities, or a Fifth or Sixth Schedule area)?
- `p7_fpic` (PS7 paras 12–16) [A, blocks C] Will the project be on, or take natural resources from, land that Indigenous Peoples traditionally own or customarily use; relocate them from such land; or significantly affect cultural heritage that is critical to them?

Trap: concluding "no Scheduled Area, so no PS7". Scheduled Tribe communities live outside Scheduled Areas too. Check village-level census data and customary use.
FPIC applies in three circumstances (paras 13-16): impacts on land or natural resources under traditional ownership or customary use; relocation of Indigenous Peoples from such land; significant impact on critical cultural heritage. Commercial use of Indigenous Peoples' cultural heritage also needs FPIC (para 17); the checklist catches that when PS7 present and PS8 commercial use are both Yes.

## PS8 Cultural heritage

- `p8_known` (PS8 paras 6–10) [blocks C] Are there known heritage sites near the footprint (protected monuments, temples, sacred groves, graves, shrines)?
- `p8_critical` (PS8 paras 12–15) [A, blocks C] Could the project significantly damage or remove cultural heritage that cannot be replaced, or that is internationally or nationally important (a World Heritage property, an ancient monument, a major sacred site)?
- `p8_dig` (PS8 paras 7–8) [blocks C] Will there be significant excavation or earthworks in an area where cultural heritage is likely to be found?
- `p8_use` (PS8 para 16; PS7 para 17) [blocks C] Will the project use cultural heritage or traditional knowledge for commercial purposes?

PS8 does not apply to Indigenous Peoples' cultural heritage; PS7 covers it (para 5).
A chance-find procedure is required where the assessment finds the location is in an area where heritage is expected to be found (para 8). Where there is ground disturbance and no specific indicator, recommend one as good practice and say it is not a requirement.

## Sector intensity guide (starting point, not a verdict)

Sector ids are the values for `sector` in a case file. Risk class feeds the category rules; EC gate shows sectors outside India's Environmental Clearance schedule.

| Sector id | Sector | Risk class | India EC gate | Typical exposure |
|---|---|---|---|---|
| `solar` | Solar power | med | outside EC schedule | PS3 low; PS5 and PS6 often decisive (land, grazing, birds, grassland); PS4 for lines and traffic |
| `wind` | Wind power | med | outside EC schedule | PS6 birds and bats; PS5 land and access roads; PS4 blade throw, shadow flicker, traffic; PS7 where on tribal land |
| `hydro` | Hydropower or dams | high | - | High across PS4 (dam safety), PS5, PS6 (river), PS7, PS8; cumulative impacts |
| `td` | Power transmission and distribution | med | outside EC schedule | PS5 right-of-way; PS6 birds and forest corridors; PS4 line safety |
| `thermal` | Thermal power | high | - | PS3 high (emissions, GHG, ash, hazardous materials); PS4 including ash ponds |
| `transport` | Roads, rail or metro | med | - | PS4 traffic and influx; PS5 right-of-way; PS6 for forest and coastal alignments |
| `ports` | Ports or airports | high | - | PS5, PS6 coastal habitat, PS4 traffic and hazardous materials |
| `oilgas` | Oil, gas or pipelines | high | - | PS3, PS4 (pipeline safety), PS5 right-of-way, PS6 |
| `mining` | Mining or quarrying | high | - | High across PS3 to PS8; tailings safety; legacy land |
| `heavy` | Heavy industry (cement, steel, chemicals) | high | - | PS3 high; PS4 hazardous materials; PS2 OHS |
| `light` | Light manufacturing | med | - | PS2 and PS3 moderate; PS2 supply chain in textiles and electronics |
| `agri` | Agribusiness or food processing | med | - | PS2 seasonal and child labour; PS3 pesticides; PS6 sourcing |
| `forestry` | Forestry or plantations | high | - | PS6 habitat conversion; PS7 customary use; PS2 |
| `realestate` | Real estate, hospitality or commercial buildings | med | - | PS2 construction labour; PS4 life and fire safety; PS5 if land assembled |
| `water` | Water, sanitation or waste | med | - | PS3 effluent and sludge; PS4; PS5 for pipelines and plants |
| `social` | Healthcare or education | low | - | PS1 and PS2; healthcare adds PS3 medical waste (so pollution answers block Category C here) |
| `services` | Services, IT or retail | low | - | Usually PS1 and PS2 only |
| `fi` | Financial intermediary (bank, NBFC, fund, insurer) | fi | - | Apply through the FI’s ESMS to sub-projects |

Stage ids: `greenfield` (Greenfield (new site)), `expansion` (Expansion of an existing site), `existing` (Existing operations), `acquisition` (Acquisition of a company). Country: `IN` for India, `OTHER` for anywhere else.
