"""Checks the rule set and the engine against test_cases.json.

Usage:  python run_tests.py [rules.json]
Works from any folder: files are found next to this script.
Exit code 0 only if every check passes.

Each case lists the exact status of PS1 to PS8, the exact category, and (where
given) the exact list of A-signals, watch items and sanity warnings. Tokens:
  q:<id>    the text a question gives when answered Yes (signals) or still open (watch)
  sig:<id>  the reason text of a non-question A-signal rule
"""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from screen import CaseError, check_rules, normalise_case, screen  # noqa: E402

rules_path = Path(sys.argv[1]) if len(sys.argv) > 1 else next(HERE.glob("ifc_ps_rules_v*.json"))
rules = json.loads(rules_path.read_text(encoding="utf8"))
cases = json.loads((HERE / "test_cases.json").read_text(encoding="utf8"))

Q = {q["id"]: q for q in rules["questions"]}
SIG = {s["id"]: s for s in rules["category_rules"]["a_signals"]}
failures = []
total = 0


def check(name, errs):
    global total
    total += 1
    if errs:
        failures.append(name)
    print(("PASS " if not errs else "FAIL ") + name + ("" if not errs else ":\n     " + "\n     ".join(errs)))


def token(kind, t):
    typ, key = t.split(":", 1)
    if typ == "q":
        return Q[key]["if_yes_reason" if kind == "signal" else "if_open_confirm"]
    if typ == "sig":
        return SIG[key]["reason"]
    raise ValueError(t)


# 1. the rule set is internally consistent
check("rule set lint", check_rules(rules))

# 2. reference cases, exact match
for c in cases:
    r = screen(rules, {k: c[k] for k in ("sector", "stage", "country", "answers")})
    e, errs = c["expect"], []
    got_status = {str(s["ps"]): s["status"] for s in r["standards"]}
    if r["category"]["value"] != e["category"]:
        errs.append(f"category {r['category']['value']!r} != {e['category']!r}")
    if "why" in e and r["category"]["why"] != e["why"]:
        errs.append(f"why {r['category']['why']!r} != {e['why']!r}")
    if "status" in e and got_status != e["status"]:
        errs.append(f"status {got_status} != {e['status']}")
    if "signals" in e:
        want = [token("signal", t) for t in e["signals"]]
        if r["category"]["signals"] != want:
            errs.append(f"signals {r['category']['signals']} != {want}")
    if "watch" in e:
        want = [token("watch", t) for t in e["watch"]]
        if r["category"]["watch"] != want:
            errs.append(f"watch {r['category']['watch']} != {want}")
    if "warnings" in e and [w["id"] for w in r["warnings"]] != e["warnings"]:
        errs.append(f"warnings {[w['id'] for w in r['warnings']]} != {e['warnings']}")
    if "ec_gate" in e and (("india_ec_gate" in r) != e["ec_gate"]):
        errs.append(f"EC gate present={('india_ec_gate' in r)} expected {e['ec_gate']}")
    if "ps1_first_action_starts" in e and not r["standards"][0]["actions"][0]["text"].startswith(e["ps1_first_action_starts"]):
        errs.append("PS1 first action is " + r["standards"][0]["actions"][0]["text"][:50])
    if e.get("ps8_note_if_clear") and not r["standards"][7]["note_if_clear"]:
        errs.append("PS8 clear note missing")
    if "fi_prompt" in e and (r["exclusion_check"]["fi_prompt"] is not None) != e["fi_prompt"]:
        errs.append(f"fi_prompt present={r['exclusion_check']['fi_prompt'] is not None} expected {e['fi_prompt']}")
    if "policy_note_cite" in e and r.get("sector_policy_note", {}).get("cite") != e["policy_note_cite"]:
        errs.append(f"policy note cite {r.get('sector_policy_note', {}).get('cite')!r} != {e['policy_note_cite']!r}")
    if e.get("no_national_law") and any(s["national_law"] for s in r["standards"]):
        errs.append("national law lines shown for another country")
    check(c["name"], errs)

# 3. invariants on every reference result
errs = []
for c in cases:
    r = screen(rules, {k: c[k] for k in ("sector", "stage", "country", "answers")})
    for s in r["standards"]:
        if s["status"] != "trig" and (s["actions"] or s["documents"] or s["because"]):
            errs.append(f"{c['name']}: PS{s['ps']} shows actions or documents without being triggered")
        for a in s["actions"]:
            if not a["cite"]:
                errs.append(f"{c['name']}: PS{s['ps']} action without citation")
        if s["status"] == "open" and (s["confirm"] or s["national_law"]):
            errs.append(f"{c['name']}: PS{s['ps']} not screened but shows confirm or law lines")
    if not r["exclusion_check"]["prompt"]:
        errs.append(f"{c['name']}: no Exclusion List prompt")
    if (r["exclusion_check"]["fi_prompt"] is not None) != (c["sector"] == "fi"):
        errs.append(f"{c['name']}: FI Exclusion List wording shown for the wrong sector")
    if r["category"]["value"] != "A" and r["category"]["signals"]:
        errs.append(f"{c['name']}: signals shown for category {r['category']['value']}")
    if r["category"]["value"] not in ("B", "C") and r["category"]["watch"]:
        errs.append(f"{c['name']}: watch items shown for category {r['category']['value']}")
check("invariants on all reference results", errs)

# 4. input handling: bad input is rejected loudly, harmless variants are accepted
good = {"sector": "solar", "stage": "greenfield", "country": "IN", "answers": {"p5_land": "yes"}}
bad_inputs = {
    "boolean answer": dict(good, answers={"p5_land": True}),
    "free text answer": dict(good, answers={"p5_land": "Yes please"}),
    "unknown question id": dict(good, answers={"p9_nonsense": "yes"}),
    "unknown sector": dict(good, sector="Solar PV"),
    "unknown stage": dict(good, stage="construction"),
    "unknown country": dict(good, country="India"),
    "answers not an object": dict(good, answers=["yes"]),
    "case not an object": ["solar"],
}
for name, case in bad_inputs.items():
    try:
        screen(rules, case)
        check("rejects " + name, ["no error raised"])
    except CaseError:
        check("rejects " + name, [])
many = dict(good, sector="nonsense", stage="x", country="Y", answers={"p5_land": 1, "zz": "no"})
try:
    normalise_case(rules, many)
    check("reports every problem at once", ["no error raised"])
except CaseError as e:
    check("reports every problem at once", [] if len(e.errors) == 5 else [f"expected 5 problems, got {len(e.errors)}: {e.errors}"])
variants = dict(good, answers={"p5_land": " YES ", "p5_users": None, "p5_access": ""})
same = screen(rules, dict(good, answers={"p5_land": "yes"}))
check("accepts letter case, spaces, null and empty answers",
      [] if screen(rules, variants) == same else ["result differs from the clean case"])
check("country defaults to IN", [] if screen(rules, {"sector": "solar", "answers": {}})["input"]["country"] == "IN" else ["default not IN"])

print(f"\n{total - len(failures)}/{total} checks passed")
sys.exit(1 if failures else 0)
