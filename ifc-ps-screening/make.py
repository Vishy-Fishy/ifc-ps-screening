"""One command for everything you do after changing the rule set.

    python make.py build      rebuild the HTML checklist and refresh the Skill's copies and generated references
    python make.py test       lint the rule set, run the reference cases, compare HTML and engine
    python make.py package    write dist/: the Skill zip, the checklist, and the participant package zip
    python make.py all        build, test, package

Works on Windows, macOS and Linux. Needs Python 3.9+ and, for `test`, Node.js 18+.
The rule set (toolkit/ifc_ps_rules_v*.json) is the only place rules live: never edit
the built HTML or the copies inside skill/ by hand, because `build` overwrites them.
"""
import json
import os
import shutil
import subprocess
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent
TK = ROOT / "toolkit"
SK = ROOT / "skill" / "ifc-ps-screening"
DIST = ROOT / "dist"
ENV = dict(os.environ, PYTHONUTF8="1", PYTHONIOENCODING="utf-8", PYTHON=sys.executable)


def run(cmd, cwd):
    print("  $ " + " ".join(str(c) for c in cmd))
    r = subprocess.run([str(c) for c in cmd], cwd=str(cwd), env=ENV)
    if r.returncode:
        sys.exit(f"FAILED ({r.returncode}): {' '.join(str(c) for c in cmd)}")


def rules_path():
    found = sorted(TK.glob("ifc_ps_rules_v*.json"))
    if len(found) != 1:
        sys.exit(f"expected exactly one toolkit/ifc_ps_rules_v*.json, found {len(found)}")
    return found[0]


def version():
    return json.loads(rules_path().read_text(encoding="utf8"))["version"]


def copy_text(src, dst):
    # same bytes in, same bytes out, so the result is identical on every operating system
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(src, dst)


def build():
    print("build")
    rp = rules_path()
    run([sys.executable, "-I", "build_html.py"], TK)
    copy_text(TK / "screen.py", SK / "scripts" / "screen.py")
    copy_text(rp, SK / "references" / "ifc_ps_rules.json")
    run([sys.executable, "-I", "make_triggers.py", rp, SK / "references" / "triggers.md"], TK)
    run([sys.executable, "-I", "make_exclusion.py", rp, SK / "references" / "exclusion-list.md"], TK)
    notice = (SK / "NOTICE.txt").read_text(encoding="utf8")
    if f"v{version()}" not in notice:
        print(f"  WARNING: skill/ifc-ps-screening/NOTICE.txt does not mention rule set v{version()}. Update it by hand.")


def test():
    print("test")
    run([sys.executable, "-I", "run_tests.py"], TK)
    if shutil.which("node") is None:
        sys.exit("Node.js is needed for the parity test: install it from nodejs.org")
    run(["node", "parity.js"], TK)


def zip_dir(src_dir, zip_path, top):
    with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as z:
        for p in sorted(src_dir.rglob("*")):
            if p.is_file() and "__pycache__" not in p.parts:
                z.write(p, Path(top, p.relative_to(src_dir)).as_posix())


def package():
    print("package")
    v = version()
    if DIST.exists():
        shutil.rmtree(DIST)
    DIST.mkdir()
    zip_dir(SK, DIST / "ifc-ps-screening.zip", "ifc-ps-screening")
    shutil.copyfile(TK / "ifc-ps-screening-tool.html", DIST / "ifc-ps-screening-tool.html")

    pkg = DIST / "IFC-PS-Screening-Package"
    part, own = ROOT / "docs" / "participant", ROOT / "docs" / "owner"
    layout = {
        "1_Quick_Checklist": [TK / "ifc-ps-screening-tool.html"],
        "2_Claude_Skill": [DIST / "ifc-ps-screening.zip", part / "IFC_PS_Skill_Setup_Kit.docx"],
        "3_Optional_Claude_Project": [part / "IFC_PS_Assistant_Setup_Kit.docx", part / "IFC_PS_Assistant_Instructions.txt"],
        "4_Official_IFC_Documents": [part / "DOWNLOAD_LINKS.md"],
        "5_Example_Cases": sorted((ROOT / "examples").glob("*.json")),
        "6_For_The_Rule_Set_Owner": [rules_path(), *[TK / n for n in (
            "screen.py", "build_html.py", "template.html", "make_triggers.py", "make_exclusion.py",
            "run_tests.py", "parity.js", "test_cases.json", "ifc-ps-screening-tool.html")],
            ROOT / "CHANGES.md", own / "IFC_PS_Rule_Set_Guide.docx", own / "IFC_PS_Connector_Specification.docx"],
    }
    for folder, files in layout.items():
        (pkg / folder).mkdir(parents=True)
        for f in files:
            shutil.copyfile(f, pkg / folder / f.name)
    shutil.copyfile(part / "README.md", pkg / "README.md")
    if shutil.which("pandoc"):
        run(["pandoc", "README.md", "-o", "README.docx", "--from", "gfm"], pkg)
    else:
        print("  (pandoc not found: README.docx not created; README.md is included)")
    zip_dir(pkg, DIST / f"IFC-PS-Screening-Package-{v}.zip", "IFC-PS-Screening-Package")
    print(f"  wrote {DIST}")


COMMANDS = {"build": [build], "test": [test], "package": [package], "all": [build, test, package]}

if __name__ == "__main__":
    if len(sys.argv) != 2 or sys.argv[1] not in COMMANDS:
        print(__doc__)
        sys.exit(2)
    for step in COMMANDS[sys.argv[1]]:
        step()
    print("done")
