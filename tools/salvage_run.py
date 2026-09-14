#!/usr/bin/env python3
"""Salvage a dossier from a codex run log that the extractor rejected because of a transient
"ERROR: Reconnecting... n/5" notice printed mid-stream. Strips those lines, writes the dossier,
commits and pushes it under the same lock the batch driver uses.

    python3 tools/salvage_run.py <run.log> "<Display Name>" <out.md>
"""
import fcntl, os, re, subprocess, sys

log, name, out = sys.argv[1], sys.argv[2], os.path.abspath(sys.argv[3])
text = open(log, errors="ignore").read()
i = text.rfind(f"# {name}: Research Dossier")
if i < 0:
    sys.exit("no dossier marker in the log")
doc = text[i:]
doc = re.sub(r"^ERROR: Reconnecting\.\.\. \d+/\d+\n?", "", doc, flags=re.M)
doc = re.sub(r"\ntokens used\n[\d,]+\s*$", "\n", doc)
if re.search(r"^ERROR: ", doc, flags=re.M):
    sys.exit("a real ERROR line remains; not salvaging")
os.makedirs(os.path.dirname(out), exist_ok=True)
open(out, "w").write(doc)
repo = subprocess.run(["git", "-C", os.path.dirname(out), "rev-parse", "--show-toplevel"], capture_output=True, text=True).stdout.strip()
rel = os.path.relpath(out, repo)
label = rel.split("/")[0]
with open(os.path.join(repo, ".dossier_git.lock"), "w") as lk:
    fcntl.flock(lk, fcntl.LOCK_EX)
    subprocess.run(["git", "-C", repo, "add", rel], check=True)
    subprocess.run(["git", "-C", repo, "commit", "-q", "-m", f"{label}: {name} dossier", "-m",
                    "Salvaged from the run log after a transient stream reconnect notice; content complete.",
                    "-m", "Co-Authored-By: El Gólem <golem@localhost>"], check=True)
    for remote in subprocess.run(["git", "-C", repo, "remote"], capture_output=True, text=True).stdout.split():
        subprocess.run(["git", "-C", repo, "push", remote, "main"], capture_output=True)
print("salvaged", rel, doc.count("\n"), "lines")
