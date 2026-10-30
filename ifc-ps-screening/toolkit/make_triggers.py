"""Generates references/triggers.md from the rule set, so the Skill and the checklist show the same questions."""
import json, sys
rules = json.load(open(sys.argv[1], encoding="utf8"))
out = []
w = out.append
w("# Trigger questions, traps and intensity")
w("")
w(f"Generated from rule set v{rules['version']}. These are the same 33 questions, in the same words, as EMC's HTML checklist, so a screen done in chat and one done with the checklist reach the same verdicts. Each line gives the question id (use it as the key in a case file), the Performance Standard paragraphs it rests on, and flags: **A** = a Yes is a Category A signal; **blocks C** = a Yes rules out Category C; **EMC** = EMC practice or judgement rather than Performance Standard text.")
w("")
w("## How answers become verdicts")
w("")
w("- Any **Yes** in a standard triggers it. All **No** clears it. No answers at all leaves it **not screened**. Anything else (Not sure, or a mix of No and unanswered) is **needs review** and becomes an open fact.")
w("- PS1 is always triggered.")
w(f"- A category is given only when a sector is chosen and at least {rules['category_rules']['min_informative_answers']} questions are answered Yes or No (Not sure does not count). A Category A signal can show earlier.")
w("- Category order: FI sector first; then A if any A signal; then \"not yet categorised\" if the sector is missing or there are too few answers; then C if the sector is low risk and no \"blocks C\" question is answered Yes; otherwise B.")
w("- Every A-signal question not answered No becomes a \"could move to A\" item on a B or C result.")
w("- Sanity checks: if an answer looks implausible for the sector (for example No to land for a solar park), the engine returns a warning. Raise it with the user.")
w("")
traps = {
1: ["Always triggered for a project financed under the Performance Standards. The question is how substantial the ESMS must be, which follows the category."],
2: ["Trap: screening only direct employees. PS2 reaches workers engaged by third parties (paras 24-26) and, where risks are known, the primary supply chain (paras 27-29). For acquisitions, retrenchment is often the main PS2 issue.",
    "Camps: the IFC/EBRD Workers' Accommodation guidance is referred to in Guidance Note 2 (GN2-32). Migrant workers: the Guidance Note says clients may not retain workers' identity documents (GN2-71) and should avoid practices that create unpayable debt (GN2-72)."],
3: ["Trap: treating PS3 as triggered or not. It applies to almost every physical project; what matters is intensity. State it.",
    "GHG: PS3 para 8 asks the client to quantify emissions annually where the project is expected to produce more than 25,000 tCO2e a year. It does not itself require public reporting.",
    "Pesticides: WHO Class Ia and Ib products are not to be purchased, stored, used, manufactured or traded; Class II only where there are controls and trained handlers (para 17)."],
4: ["NOT TRIGGERED is defensible only for sites with no community proximity, no public road use, no security and no public-safety structures. Say why.",
    "Dams, tailings dams and ash ponds in high-risk locations need review by external experts separate from the designers, from early design through decommissioning (para 6). This is a Category A signal in this rule set.",
    "Labour influx: the PS4 text (para 10) covers communicable disease. Controls on gender-based violence and sexual exploitation are lender practice; label them that way.",
    "Security: PS4 paras 12-14 set the requirements (proportionality, vetting, training, grievance mechanism). The Voluntary Principles are a common benchmark but the PS text does not name them."],
5: ["Traps:",
    "- \"The land is government wasteland\" does not clear PS5. Revenue, gauchar (grazing) and common land is often used informally. Ask for a land-use and livelihood survey.",
    "- PS5 does not apply to voluntary transactions: the seller is not obliged to sell and the buyer cannot resort to expropriation if talks fail (para 6). It also does not apply where land use is not changing. The checklist therefore asks you to show voluntariness parcel by parcel; where expropriation powers stand behind the negotiation (para 5), treat it as involuntary.",
    "- People with no legal right or recognisable claim are not paid for the land, but are offered resettlement with security of tenure, compensation for non-land assets owned before the cut-off date, and help to restore livelihoods (para 22 and footnote 8). People who arrive after a published cut-off date need not be compensated (para 23).",
    "- Linear projects (transmission, roads, pipelines) create many small impacts: right-of-way, tower footprints, crop damage, access restrictions.",
    "- Legacy acquisition by a state agency (industrial parks, solar parks) needs a legacy review and, where there are gaps, a corrective action plan. This is lender practice anchored in PS1 para 9 (third-party risks) and PS5 paras 30-31."],
6: ["Traps:",
    "- Screening only against notified protected-area boundaries. Critical habitat (para 16) is defined by biodiversity value, not by legal boundary: habitat of significant importance to Critically Endangered or Endangered species, endemic or restricted-range species, globally significant concentrations of migratory or congregatory species, highly threatened or unique ecosystems, or key evolutionary processes. Where the region has documented sensitive-species risk (see india-risk-flags.md), mark NEEDS REVIEW or TRIGGERED and call for a critical habitat assessment.",
    "- \"Internationally recognised areas\" in PS6 means UNESCO Natural World Heritage Sites, UNESCO Man and the Biosphere reserves, Key Biodiversity Areas and Ramsar wetlands (para 20, footnote 17). The 10 km screening distance is an EMC heuristic, not a PS rule.",
    "- Grasslands and drylands are often treated as \"wasteland\" although they are natural habitat.",
    "- For rivers (hydropower, water abstraction), consider downstream flows and fish passage, not only the footprint."],
7: ["Trap: concluding \"no Scheduled Area, so no PS7\". Scheduled Tribe communities live outside Scheduled Areas too. Check village-level census data and customary use.",
    "FPIC applies in three circumstances (paras 13-16): impacts on land or natural resources under traditional ownership or customary use; relocation of Indigenous Peoples from such land; significant impact on critical cultural heritage. Commercial use of Indigenous Peoples' cultural heritage also needs FPIC (para 17); the checklist catches that when PS7 present and PS8 commercial use are both Yes."],
8: ["PS8 does not apply to Indigenous Peoples' cultural heritage; PS7 covers it (para 5).",
    "A chance-find procedure is required where the assessment finds the location is in an area where heritage is expected to be found (para 8). Where there is ground disturbance and no specific indicator, recommend one as good practice and say it is not a requirement."],
}
for s in rules["standards"]:
    ps = s["ps"]
    w(f"## PS{ps} {s['name']}")
    w("")
    qs = [q for q in rules["questions"] if q["ps"] == ps]
    for q in qs:
        flags = []
        if q["a_signal"]: flags.append("A")
        if q["blocks_c"]: flags.append("blocks C")
        if q["basis"] == "EMC": flags.append("EMC")
        w(f"- `{q['id']}` ({'; '.join(q['cite'])}){' [' + ', '.join(flags) + ']' if flags else ''} {q['text']}")
    if qs: w("")
    for t in traps[ps]:
        w(t)
    w("")
w("## Sector intensity guide (starting point, not a verdict)")
w("")
w("Sector ids are the values for `sector` in a case file. Risk class feeds the category rules; EC gate shows sectors outside India's Environmental Clearance schedule.")
w("")
w("| Sector id | Sector | Risk class | India EC gate | Typical exposure |")
w("|---|---|---|---|---|")
for s in rules["sectors"]:
    w(f"| `{s['id']}` | {s['label']} | {s['risk']} | {'outside EC schedule' if s['india_ec_exempt'] else '-'} | {s['exposure']} |")
w("")
w("Stage ids: " + ", ".join(f"`{s['id']}` ({s['label']})" for s in rules["stages"]) + ". Country: `IN` for India, `OTHER` for anywhere else.")
open(sys.argv[2], "w", encoding="utf8", newline="\n").write("\n".join(out) + "\n")
print("wrote", sys.argv[2])
