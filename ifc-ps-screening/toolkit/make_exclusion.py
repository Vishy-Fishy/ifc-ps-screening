"""Writes references/exclusion-list.md for the Skill from the rule set's exclusion_list block."""
import json, sys
r = json.load(open(sys.argv[1], encoding="utf8")); el = r["exclusion_list"]
L = []; w = L.append
def items(lst):
    for i, it in enumerate(lst, 1):
        fn = f" (note {it['footnote']})" if it.get("footnote") else ""
        w(f"{i}. {it['text']}{fn}")
w("# IFC Exclusion List")
w("")
w(f"Generated from rule set v{r['version']}. {el['name']}. Source: {el['source']}")
w("")
w("The Exclusion List is a gate that comes before the Performance Standards. Activities on it are not financed by IFC (Sustainability Policy para 19), whatever the Performance Standards result. The engine output carries an `exclusion_check` reminder on every result. The engine cannot tell whether an activity is excluded: that needs the project facts, so you check it.")
w("")
w("## How to use it")
w("")
w("- At intake, compare the project's products, services, supply chain and sponsor activities with the list. If one matches, say so first, before any verdict, and name the item.")
w("- Where the match is uncertain (for example a sponsor with a tobacco or alcohol arm, or asbestos in building materials), do not decide: say which fact decides it (see note 1 and the asbestos exception) and who should confirm.")
w("- The reasonableness test is IFC's to apply, not yours or the client's. Do not suggest a project qualifies.")
w(f"- {el['amendment_note']}")
w("")
w(f"## {el['intro']}")
w("")
items(el["items"])
w("")
for k, v in el["footnotes"].items():
    w(f"- **Note {k}.** {v}")
w("")
w(el["reasonableness_test"])
w("")
w("## Financial intermediaries")
w("")
for g in el["fi_additional"].values():
    w(f"**{g['label']}:**")
    w("")
    items(g["items"])
    w("")
w(f"{el['fi_substantially_involved']} ({el['fi_cite']})")
w("")
w("## Other restrictions")
w("")
w(el["other_restrictions_note"])
w("")
open(sys.argv[2], "w", encoding="utf8", newline="\n").write("\n".join(L))
print("wrote", sys.argv[2])
