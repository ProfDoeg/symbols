#!/usr/bin/env python3
"""codex_dossier_set.py -- run the Codex dossier machine ONCE for one item of any dossier set.

    python3 atlas_tools/codex_dossier_set.py <set_dir> <slug> "<Display Name>" <brief.md> <out.md>

The set directory (working/goetia, working/tree, ...) holds exactly one PROMPT_TEMPLATE_*.md
(the part after the first '---' is the prompt, with [NAME] substituted) and a DELIVER.txt (the
closing instructions, with {name} substituted). Generalizes codex_dossier_bode/tribes/tarot.py.
Separate from the atlas: no roster addendum.
"""
import glob, os, re, subprocess, sys, time

LAB = os.path.expanduser("~/codex_lab")
CODEX = os.path.expanduser("~/.local/bin/codex")


def main(set_dir, slug, name, brief_path, out):
    set_dir = os.path.abspath(set_dir)
    tag = "[" + os.path.basename(set_dir) + "]"

    def log(msg):
        line = time.strftime("%m-%d %H:%M:%S ") + tag + " " + msg
        print(line, flush=True)
        open(f"{LAB}/batch.log", "a").write(line + "\n")

    tpls = glob.glob(os.path.join(set_dir, "PROMPT_TEMPLATE_*.md"))
    if len(tpls) != 1:
        log(f"{slug}: expected one PROMPT_TEMPLATE_*.md in {set_dir}, found {len(tpls)}"); return 3
    tpl = open(tpls[0]).read().split("---", 1)[1].strip().replace("[NAME]", name).replace("[name]", name)
    brief = open(brief_path).read().split("---", 1)[1].strip()
    deliver = open(os.path.join(set_dir, "DELIVER.txt")).read().strip().replace("{name}", name)
    prompt = tpl + "\n\nITEM-SPECIFIC BRIEF (overrides the template where they differ):\n\n" + brief + "\n\n" + deliver
    tagname = os.path.basename(set_dir)
    open(f"{LAB}/prompt_{tagname}_{slug}.txt", "w").write(prompt)
    logfile = f"{LAB}/run_{tagname}_{slug}.log"
    log(f"{slug}: run ({name}), prompt {len(prompt)} chars")
    home = os.path.expanduser("~")
    extra = []
    rfile = os.path.join(set_dir, "REASONING.txt")      # e.g. "high": raises the model's reasoning effort for this set
    if os.path.exists(rfile):
        level = open(rfile).read().strip()
        if level:
            extra = ["-c", f"model_reasoning_effort={level}"]
            log(f"{slug}: reasoning effort {level}")
    try:
        with open(logfile, "w") as lf:
            subprocess.run([CODEX, "exec", "-s", "workspace-write", "--skip-git-repo-check",
                            "-C", LAB, "-c", "tools.web_search=true", *extra, "-"],
                           input=prompt, stdout=lf, stderr=subprocess.STDOUT, text=True, timeout=7200,
                           env={**os.environ, "HOME": home, "PATH": f"{home}/.local/bin:" + os.environ.get("PATH", "")})
    except subprocess.TimeoutExpired:
        log(f"{slug}: TIMEOUT after 120 min"); return 2
    text = open(logfile).read()
    marker = f"# {name}: Research Dossier"
    i = text.rfind(marker)
    if i < 0:
        i = text.rfind("# " + name)
    doc = None if i < 0 else re.sub(r"\ntokens used\n[\d,]+\s*$", "\n", text[i:])
    if doc:
        # a transient "ERROR: Reconnecting... n/5" stream notice is not a failure; drop it
        doc = re.sub(r"^ERROR: Reconnecting\.\.\. \d+/\d+\n?", "", doc, flags=re.M)
    if not doc or re.search(r"\nERROR: ", doc):
        log(f"{slug}: no clean dossier in output, tail: " + text[-200:].replace("\n", " ")); return 1
    os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
    open(out, "w").write(doc)
    log(f"{slug}: DONE {doc.count(chr(10))} lines -> {out}")
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 6:
        sys.exit(__doc__)
    sys.exit(main(*sys.argv[1:6]))
