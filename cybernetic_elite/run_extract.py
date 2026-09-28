#!/usr/bin/env python3
"""Extract the tie list of every dossier in this set that has none yet, N at a time, into relations/.

    python3 cybernetic_elite/run_extract.py [N]

Deterministic, no model in the loop beyond the Codex extraction itself. Then run
tools/build_network.py cybernetic_elite.
"""
import os, subprocess, sys, time
from concurrent.futures import ThreadPoolExecutor

HERE = os.path.dirname(os.path.abspath(__file__))
TOOL = os.path.join(os.path.dirname(HERE), "tools", "extract_network_ties.py")
N = int(sys.argv[1]) if len(sys.argv) > 1 else 8
REL = os.path.join(HERE, "relations"); os.makedirs(REL, exist_ok=True)
LOG = os.path.join(HERE, "extract_progress.log")


def log(msg):
    line = time.strftime("%m-%d %H:%M:%S ") + msg
    print(line, flush=True)
    open(LOG, "a").write(line + "\n")


def one(slug):
    out = os.path.join(REL, f"{slug}.json")
    r = subprocess.run([sys.executable, TOOL, HERE, os.path.join(HERE, f"{slug}.dossier.md"), out], capture_output=True, text=True)
    status = "done" if r.returncode == 0 and os.path.exists(out) else "fail"
    log(f"{'DONE' if status == 'done' else 'FAIL'} {slug} {r.stdout.strip()[-120:]}")
    return status


if __name__ == "__main__":
    todo = sorted(f[:-len(".dossier.md")] for f in os.listdir(HERE) if f.endswith(".dossier.md")
                  and not os.path.exists(os.path.join(REL, f[:-len(".dossier.md")] + ".json")))
    log(f"extract: {len(todo)} dossiers, {N} at a time")
    results = {}
    with ThreadPoolExecutor(max_workers=N) as ex:
        for s in ex.map(one, todo):
            results[s] = results.get(s, 0) + 1
    log(f"extract finished: {results}")
