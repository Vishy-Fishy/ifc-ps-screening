"""Reference screening engine for the EMC IFC PS rule set (engine 1.2.0).

Usage:
    python screen.py rules.json case.json      print the result as JSON
    python screen.py --check rules.json        lint the rule set and exit
    python screen.py --batch rules.json cases.json   screen a list of cases (used by parity.js)

A case looks like:
    {"sector": "solar", "stage": "greenfield", "country": "IN",
     "answers": {"p5_land": "yes", "p6_species": "unsure"}}

Answers are "yes", "no" or "unsure" (any letter case); "" or null means not
answered. Anything else is rejected with a CaseError that lists every problem,
because a silently misread answer (for example True or "Yes please") would
change the verdict without telling anyone.

All logic comes from the rule set. This file only decides how each rule type is
read, so the HTML tool built from the same rule set cannot drift from it.
"""
import json
import sys

ENGINE_VERSION = "1.2.0"
ANSWERS = ("yes", "no", "unsure")
COUNTRIES = ("IN", "OTHER")


class CaseError(ValueError):
    """The case contains values the rule set does not recognise."""

    def __init__(self, errors):
        self.errors = list(errors)
        super().__init__("; ".join(self.errors))


class RulesError(ValueError):
    """The rule set is internally inconsistent."""


# ------------------------------------------------------------------ rule set lint
def check_rules(rules):
    """Return a list of problems in the rule set (empty list means it is consistent)."""
    errs = []
    qids = [q["id"] for q in rules["questions"]]
    if len(qids) != len(set(qids)):
        errs.append("duplicate question ids")
    sids = [s["id"] for s in rules["sectors"]]
    if len(sids) != len(set(sids)):
        errs.append("duplicate sector ids")
    ps_listed = [s["ps"] for s in rules["standards"]]
    if ps_listed != list(range(1, 9)):
        errs.append("standards must list PS1 to PS8 in order")
    for q in rules["questions"]:
        if q["ps"] not in range(2, 9):
            errs.append(f"{q['id']}: ps must be 2 to 8")
        for k in ("text", "section", "cite", "basis", "a_signal", "blocks_c", "if_yes_reason",
                  "if_open_confirm", "owner", "actions_if_yes"):
            if k not in q:
                errs.append(f"{q['id']}: missing {k}")
        if not q.get("cite"):
            errs.append(f"{q['id']}: no citation")
        if q.get("basis") not in ("PS", "EMC"):
            errs.append(f"{q['id']}: basis must be PS or EMC")
        for a in q.get("actions_if_yes", []):
            if not a.get("text") or not a.get("cite"):
                errs.append(f"{q['id']}: every action needs text and cite")
    for s in rules["standards"]:
        for a in s["base_actions"]:
            if not a.get("text") or not a.get("cite"):
                errs.append(f"PS{s['ps']}: every base action needs text and cite")
    for s in rules["sectors"]:
        for qid in s.get("blocks_c_extra", []):
            if qid not in qids:
                errs.append(f"sector {s['id']}: blocks_c_extra names unknown question {qid}")
    for c in rules.get("sanity_checks", []):
        for sid in c["sector_in"]:
            if sid not in sids:
                errs.append(f"sanity check {c['id']}: unknown sector {sid}")
        for qid in c["answers"]:
            if qid not in qids:
                errs.append(f"sanity check {c['id']}: unknown question {qid}")
    for s in rules["sectors"]:
        n = s.get("policy_note")
        if n is not None and not (n.get("text") and n.get("cite")):
            errs.append(f"sector {s['id']}: policy_note needs text and cite")
    el = rules.get("exclusion_list")
    if not el:
        errs.append("exclusion_list is missing")
    else:
        for k in ("prompt", "fi_prompt", "intro", "items", "footnotes", "reasonableness_test", "fi_additional", "cite"):
            if not el.get(k):
                errs.append(f"exclusion_list: missing {k}")
        lists = [el.get("items", [])] + [g.get("items", []) for g in el.get("fi_additional", {}).values()]
        for items in lists:
            for it in items:
                if not it.get("text"):
                    errs.append("exclusion_list: an item has no text")
                for fn in str(it.get("footnote", "")).replace(" ", "").split(","):
                    if fn and fn not in el.get("footnotes", {}):
                        errs.append(f"exclusion_list: footnote {fn} is not defined")
    for sig in rules["category_rules"]["a_signals"]:
        if sig["type"] == "all_answers":
            for qid in sig["answers"]:
                if qid not in qids:
                    errs.append(f"a_signal {sig['id']}: unknown question {qid}")
        elif sig["type"] not in ("question_flag", "sector_stage"):
            errs.append(f"a_signal {sig['id']}: unknown type {sig['type']}")
    return errs


# ------------------------------------------------------------------ case validation
def _j(v):
    # compact form, so the message is identical to JSON.stringify in the HTML tool
    return json.dumps(v, ensure_ascii=False, separators=(",", ":"))


def normalise_case(rules, case):
    """Return a clean copy of the case, or raise CaseError listing every problem."""
    errs = []
    if not isinstance(case, dict):
        raise CaseError(["case must be a JSON object"])
    sector_ids = {s["id"] for s in rules["sectors"]}
    stage_ids = {s["id"] for s in rules["stages"]}
    qids = {q["id"] for q in rules["questions"]}

    sector = case.get("sector")
    sector = "" if sector is None else sector
    if not isinstance(sector, str) or (sector and sector not in sector_ids):
        errs.append(f"unknown sector {_j(sector)}; use one of: {', '.join(sorted(sector_ids))}")
    stage = case.get("stage")
    stage = "" if stage is None else stage
    if not isinstance(stage, str) or (stage and stage not in stage_ids):
        errs.append(f"unknown stage {_j(stage)}; use one of: {', '.join(sorted(stage_ids))}")
    country = case.get("country")
    if country is None or country == "":
        country = "IN"
    if country not in COUNTRIES:
        errs.append(f"unknown country {_j(country)}; use IN or OTHER")

    raw = case.get("answers")
    raw = {} if raw is None else raw
    answers = {}
    if not isinstance(raw, dict):
        errs.append("answers must be an object of question id to yes, no or unsure")
        raw = {}
    for qid, v in raw.items():
        if qid not in qids:
            errs.append(f"unknown question id {_j(qid)}")
            continue
        if v is None or (isinstance(v, str) and v == ""):
            continue
        if not isinstance(v, str) or v.strip().lower() not in ANSWERS:
            errs.append(f"{qid}: {_j(v)} is not yes, no or unsure")
            continue
        answers[qid] = v.strip().lower()
    if errs:
        raise CaseError(errs)
    return {"sector": sector, "stage": stage, "country": country, "answers": answers}


# ------------------------------------------------------------------ the screening
def screen(rules, case):
    c = normalise_case(rules, case)
    answers, stage, country = c["answers"], c["stage"], c["country"]
    qs = rules["questions"]
    sector = next((s for s in rules["sectors"] if s["id"] == c["sector"]), None)
    ans = lambda qid: answers.get(qid, "")

    # 1. status of each standard
    std = {}
    for s in rules["standards"]:
        ps = s["ps"]
        if ps in rules["status_rule"]["always_triggered"]:
            std[ps] = {"status": "trig", "yes": [], "pending": []}
            continue
        mine = [q for q in qs if q["ps"] == ps]
        a = [ans(q["id"]) for q in mine]
        if "yes" in a:
            st = "trig"
        elif a and all(x == "no" for x in a):
            st = "clear"
        elif all(x == "" for x in a):
            st = "open"
        else:
            st = "review"
        std[ps] = {"status": st,
                   "yes": [q for q in mine if ans(q["id"]) == "yes"],
                   "pending": [q for q in mine if ans(q["id"]) in ("", "unsure")]}

    # 2. A-signals, in a fixed order: question flags, then sector rules, then combinations
    cr = rules["category_rules"]
    signals = []
    for sig in cr["a_signals"]:
        if sig["type"] == "question_flag":
            signals += [q["if_yes_reason"] for q in qs if q["a_signal"] and ans(q["id"]) == "yes"]
        elif sig["type"] == "sector_stage":
            if sector and sector["risk"] == sig["sector_risk"] and stage == sig["stage"]:
                signals.append(sig["reason"])
        elif sig["type"] == "all_answers":
            if all(ans(k) == v for k, v in sig["answers"].items()):
                signals.append(sig["reason"])
    watch = [q["if_open_confirm"] for q in qs if q["a_signal"] and ans(q["id"]) != "no"]
    informative = sum(1 for v in answers.values() if v in ("yes", "no"))
    min_info = cr["min_informative_answers"]
    c_blockers = {q["id"] for q in qs if q["blocks_c"]} | set(sector.get("blocks_c_extra", []) if sector else [])

    # 3. category: first matching rule wins
    cat = None
    for rule in cr["order"]:
        w = rule["when"]
        if w == "default":
            cat = rule
        elif "sector_risk" in w and "no_blocks_c_answered_yes" not in w:
            if sector and sector["risk"] == w["sector_risk"]:
                cat = rule
        elif w.get("any_a_signal"):
            if signals:
                cat = rule
        elif w.get("no_sector"):
            if not sector or informative < min_info:
                cat = rule
        elif w.get("no_blocks_c_answered_yes"):
            if sector and sector["risk"] == w["sector_risk"] and not any(ans(i) == "yes" for i in c_blockers):
                cat = rule
        if cat:
            break
    value = cat["category"]
    category = {"value": value, "label": cat["label"], "why": cat["why"],
                "signals": signals if value == "A" else [],
                "watch": watch if value in ("B", "C") else []}
    if value == "C" and any(ans(i) != "no" for i in c_blockers):
        category["why"] += " " + cat["note_if_any_open"]

    # 4. output
    ps1 = rules["standards"][0]
    out = {"rule_set_version": rules["version"], "engine_version": ENGINE_VERSION,
           "input": c, "informative_answers": informative, "category": category, "standards": []}
    for s in rules["standards"]:
        ps = s["ps"]
        r = std[ps]
        actions = []
        if r["status"] == "trig":
            if ps == 1:
                actions += ps1.get("category_actions", {}).get(value, [])
            actions += s["base_actions"] + [a for q in r["yes"] for a in q["actions_if_yes"]]
        out["standards"].append({
            "ps": ps, "name": s["name"], "status": r["status"],
            "because": [{"reason": q["if_yes_reason"], "section": q["section"], "cite": q["cite"]} for q in r["yes"]],
            "actions": actions,
            "documents": s["documents"] if r["status"] == "trig" else [],
            "confirm": [{"fact": q["if_open_confirm"], "owner": q["owner"], "cite": q["cite"]} for q in r["pending"]]
                       if r["status"] != "open" else [],
            "note_if_clear": s.get("note_if_clear") if r["status"] == "clear" else None,
            "national_law": rules["national_law"].get(country, {}).get("by_ps", {}).get(str(ps))
                            if r["status"] != "open" else None})
    out["warnings"] = [{"id": k["id"], "message": k["message"]} for k in rules.get("sanity_checks", [])
                       if sector and sector["id"] in k["sector_in"]
                       and all(ans(qid) == v for qid, v in k["answers"].items())]
    if country == "IN" and sector and sector["india_ec_exempt"]:
        out["india_ec_gate"] = rules["national_law"]["IN"]["ec_gate_note"]
    el = rules["exclusion_list"]
    out["exclusion_check"] = {"prompt": el["prompt"],
                              "fi_prompt": el["fi_prompt"] if sector and sector["risk"] == "fi" else None}
    if sector and sector.get("policy_note"):
        out["sector_policy_note"] = sector["policy_note"]
    out["disclaimer"] = rules["disclaimer"]
    return out


def main(argv):
    # Windows consoles and pipes default to a legacy code page; the output contains symbols such as CO₂.
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8")
    if len(argv) == 3 and argv[1] == "--check":
        problems = check_rules(json.load(open(argv[2], encoding="utf8")))
        print("\n".join(problems) if problems else "rule set is consistent")
        return 1 if problems else 0
    if len(argv) == 4 and argv[1] == "--batch":
        rules = json.load(open(argv[2], encoding="utf8"))
        results = []
        for case in json.load(open(argv[3], encoding="utf8")):
            try:
                results.append(screen(rules, case))
            except CaseError as e:
                results.append({"error": e.errors})
        print(json.dumps(results, ensure_ascii=False))
        return 0
    if len(argv) != 3:
        print(__doc__)
        return 2
    rules = json.load(open(argv[1], encoding="utf8"))
    case = json.load(open(argv[2], encoding="utf8"))
    try:
        print(json.dumps(screen(rules, case), indent=2, ensure_ascii=False))
    except CaseError as e:
        print("Case rejected:\n  " + "\n  ".join(e.errors), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
