#!/usr/bin/env python3
"""Run extract_relations.py over every dossier of the pantheon set, N at a time, skipping ones that
already have pantheon/<tradition>/relations/<slug>.json. No git here: the main loop commits the
relations/ folders when the batch is done. Log: pantheon/relations_progress.log.

    python3 tools/run_relations_batch.py [concurrency] [folder ...]
"""
import os, subprocess, sys, time
from concurrent.futures import ThreadPoolExecutor

HERE = os.path.dirname(os.path.abspath(__file__))
args = sys.argv[1:]
# optional first argument: the set directory (default pantheon); e.g. tools/run_relations_batch.py heroes 8
SET = os.path.join(os.path.dirname(HERE), "pantheon")
if args and os.path.isdir(os.path.join(os.path.dirname(HERE), args[0])):
    SET = os.path.join(os.path.dirname(HERE), args.pop(0))
RUNNER = os.path.join(HERE, "extract_relations.py")
PROGRESS = os.path.join(SET, "relations_progress.log")
SKIP_DIRS = {"briefs", "__pycache__", "dossiers", "relations", "notes"}
N = int(args[0]) if args else 4
ONLY = set(args[1:])
LABEL = os.path.basename(SET)


def log(msg):
    line = time.strftime("%m-%d %H:%M:%S ") + msg
    print(line, flush=True)
    open(PROGRESS, "a").write(line + "\n")


def items():
    for trad in sorted(os.listdir(SET)):
        d = os.path.join(SET, trad)
        if not os.path.isdir(d) or trad in SKIP_DIRS or (ONLY and trad not in ONLY):
            continue
        for f in sorted(os.listdir(d)):
            if f.endswith(".md") and not f.startswith("_"):
                slug = f[:-3]
                yield trad, slug, os.path.join(d, f), os.path.join(d, "relations", slug + ".json")


def one(it):
    trad, slug, doss, out = it
    if os.path.exists(out):
        return "exists"
    log(f"start {trad}/{slug}")
    r = subprocess.run([sys.executable, RUNNER, doss, out], capture_output=True, text=True)
    if r.returncode == 0 and os.path.exists(out):
        log(f"DONE {trad}/{slug}"); return "done"
    log(f"FAIL {trad}/{slug}: rc={r.returncode} {r.stdout.strip()[-160:]}"); return "fail"


if __name__ == "__main__":
    todo = [it for it in items() if not os.path.exists(it[3])]
    log(f"relations batch {LABEL}: {len(todo)} to run, {N} at a time")
    results = {}
    with ThreadPoolExecutor(max_workers=N) as ex:
        for status in ex.map(one, todo):
            results[status] = results.get(status, 0) + 1
    log(f"relations batch {LABEL} finished: {results}")
