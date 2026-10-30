"""Builds the single-file HTML tool from the rule set.

Usage:  python build_html.py [rules.json] [template.html] [out.html]
Defaults: the rule set and template next to this script; output
ifc-ps-screening-tool.html next to this script.

The rule set is embedded in the page, so the tool needs no network and shows
exactly the logic and wording of the JSON. Rebuild after every rule-set change,
then run run_tests.py and parity.js.
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from screen import ENGINE_VERSION, check_rules  # noqa: E402

rules_path = Path(sys.argv[1]) if len(sys.argv) > 1 else next(HERE.glob("ifc_ps_rules_v*.json"))
template_path = Path(sys.argv[2]) if len(sys.argv) > 2 else HERE / "template.html"
out_path = Path(sys.argv[3]) if len(sys.argv) > 3 else HERE / "ifc-ps-screening-tool.html"

rules = json.loads(rules_path.read_text(encoding="utf8"))
problems = check_rules(rules)
if problems:
    sys.exit("Rule set is inconsistent, not building:\n  " + "\n  ".join(problems))

blob = json.dumps(rules, ensure_ascii=False, separators=(",", ":"))
blob = blob.replace("</", "<\\/").replace("<!--", "<\\!--").replace("\u2028", "\\u2028").replace("\u2029", "\\u2029")
html = template_path.read_text(encoding="utf8")
for marker in ("@@RULES_JSON@@", "@@ENGINE_VERSION@@"):
    if html.count(marker) != 1:
        sys.exit(f"template must contain {marker} exactly once")
html = html.replace("@@RULES_JSON@@", blob).replace("@@ENGINE_VERSION@@", ENGINE_VERSION)
with open(out_path, "w", encoding="utf8", newline="\n") as fh:
    fh.write(html)
print(f"built {out_path.name}: rule set {rules['version']}, engine {ENGINE_VERSION}, {len(html):,} bytes")
