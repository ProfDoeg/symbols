#!/usr/bin/env python3
"""Run any dossier set unattended: N at a time, skipping items that exist, committing and pushing
each dossier as it lands (exact paths, both remotes), logging to <set_dir>/batch_progress.log.
Deterministic, no model in the loop (the land_subject.py precedent).

    python3 atlas_tools/run_dossier_batch.py <set_dir> [concurrency]

<set_dir>/make_briefs.py must define SIGNS {slug: (name, ...)}, ORDER, and may define
out_path(slug) (relative to set_dir; default <slug>.dossier.md); briefs live in <set_dir>/briefs/.
"""
import importlib.util, os, subprocess, sys, threading, time
from concurrent.futures import ThreadPoolExecutor

HERE = os.path.dirname(os.path.abspath(__file__))
RUNNER = os.path.join(HERE, "codex_dossier_set.py")

SET = os.path.abspath(sys.argv[1])
N = int(sys.argv[2]) if len(sys.argv) > 2 else 3
# the repo is whichever one holds the set (the sets live in ProfDoeg/dossiers since 2026-09-14)
REPO = subprocess.run(["git", "-C", SET, "rev-parse", "--show-toplevel"], capture_output=True, text=True).stdout.strip()
REMOTES = subprocess.run(["git", "-C", REPO, "remote"], capture_output=True, text=True).stdout.split()
PROGRESS = os.path.join(SET, "batch_progress.log")
REL = os.path.relpath(SET, REPO)
LABEL = os.path.basename(SET)

spec = importlib.util.spec_from_file_location("make_briefs", os.path.join(SET, "make_briefs.py"))
mb = importlib.util.module_from_spec(spec); spec.loader.exec_module(mb)
out_path = getattr(mb, "out_path", lambda s: f"{s}.dossier.md")
git_lock = threading.Lock()


def log(msg):
    line = time.strftime("%m-%d %H:%M:%S ") + msg
    print(line, flush=True)
    open(PROGRESS, "a").write(line + "\n")


def git(*args):
    return subprocess.run(["git", "-C", REPO, *args], capture_output=True, text=True)


def land(slug, name):
    rel = f"{REL}/{out_path(slug)}"
    with git_lock:
        git("add", rel)
        git("commit", "-q", "-m", f"{LABEL}: {name} dossier", "-m",
            f"Codex-researched from the {LABEL} prompt and the per-item brief ({REL}). Separate from the atlas.",
            "-m", "Co-Authored-By: El Gólem <golem@localhost>")
        for remote in REMOTES:
            r = git("push", remote, "main")
            if r.returncode != 0:
                log(f"  push to {remote} failed: {r.stderr.strip()[:200]}")


def one(slug):
    name = mb.SIGNS[slug][0]
    out = os.path.join(SET, out_path(slug))
    if os.path.exists(out):
        log(f"skip {slug}: exists"); return slug, "exists"
    brief = os.path.join(SET, "briefs", f"{slug}.brief.md")
    log(f"start {slug} ({name})")
    r = subprocess.run([sys.executable, RUNNER, SET, slug, name, brief, out], capture_output=True, text=True)
    if r.returncode == 0 and os.path.exists(out):
        lines = sum(1 for _ in open(out))
        land(slug, name)
        log(f"DONE {slug}: {lines} lines, committed and pushed"); return slug, "done"
    log(f"FAIL {slug}: rc={r.returncode} {r.stdout.strip()[-200:]}"); return slug, "fail"


if __name__ == "__main__":
    todo = [s for s in mb.ORDER if not os.path.exists(os.path.join(SET, out_path(s)))]
    log(f"batch {LABEL}: {len(todo)} to run, {N} at a time")
    results = {}
    with ThreadPoolExecutor(max_workers=N) as ex:
        for slug, status in ex.map(one, todo):
            results[status] = results.get(status, 0) + 1
    log(f"batch {LABEL} finished: {results}")
