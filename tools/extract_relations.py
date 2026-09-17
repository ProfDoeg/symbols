#!/usr/bin/env python3
"""extract_relations.py -- run Codex ONCE (no web search) to pull the relation list out of one
pantheon dossier.

    python3 tools/extract_relations.py <dossier.md> <out.json>

Prompt = pantheon/RELATIONS_PROMPT.md (after the first '---') + the dossier text. Codex prints a
JSON array; we take the last balanced [...] in its output and validate it. Exit 0 on success.
"""
import json, os, re, subprocess, sys, time

LAB = os.path.expanduser("~/codex_lab")
CODEX = os.path.expanduser("~/.local/bin/codex")
HERE = os.path.dirname(os.path.abspath(__file__))
PROMPT = os.path.join(HERE, "..", "pantheon", "RELATIONS_PROMPT.md")
KINDS = {"parent_of","child_of","sibling_of","consort_of","ancestor_of","descendant_of","created","created_by",
         "fought","killed","killed_by","allied","seduced","seduced_by","deceived","deceived_by","judged","judged_by",
         "rescued","rescued_by","punished","punished_by","transformed","transformed_by","contest","theft","gift",
         "taught","taught_by","served","served_by","identified_with","shared_myth","other"}


def log(msg):
    line = time.strftime("%m-%d %H:%M:%S ") + "[relations] " + msg
    print(line, flush=True)
    open(f"{LAB}/batch.log", "a").write(line + "\n")


def last_json_array(text):
    """Return the last balanced top-level [...] in text that parses as a JSON list, else None."""
    end = len(text)
    while True:
        close = text.rfind("]", 0, end)
        if close < 0:
            return None
        depth = 0; i = close
        while i >= 0:
            c = text[i]
            if c == "]": depth += 1
            elif c == "[":
                depth -= 1
                if depth == 0:
                    try:
                        v = json.loads(text[i:close + 1])
                        if isinstance(v, list):
                            return v
                    except json.JSONDecodeError:
                        pass
                    break
            i -= 1
        end = close


def main(doss, out):
    slug = os.path.basename(doss).replace(".md", "")
    tpl = open(PROMPT).read().split("---", 1)[1].strip()
    body = open(doss).read()
    prompt = tpl + "\n\n" + body + "\n\nNow print the JSON array."
    logfile = f"{LAB}/rel_{slug}.log"
    log(f"{slug}: run, {len(body)} chars")
    home = os.path.expanduser("~")
    try:
        with open(logfile, "w") as lf:
            subprocess.run([CODEX, "exec", "-s", "read-only", "--skip-git-repo-check", "-C", LAB,
                            "-c", "tools.web_search=false", "-"],
                           input=prompt, stdout=lf, stderr=subprocess.STDOUT, text=True, timeout=1800,
                           env={**os.environ, "HOME": home, "PATH": f"{home}/.local/bin:" + os.environ.get("PATH", "")})
    except subprocess.TimeoutExpired:
        log(f"{slug}: TIMEOUT after 30 min"); return 2
    text = open(logfile).read()
    if re.search(r"\nERROR: (?!Reconnecting)", text):
        log(f"{slug}: codex ERROR, tail: " + text[-160:].replace("\n", " ")); return 1
    arr = last_json_array(text)
    if arr is None:
        log(f"{slug}: no JSON array in output, tail: " + text[-160:].replace("\n", " ")); return 1
    clean = []
    for e in arr:
        if not isinstance(e, dict) or "other" not in e:
            continue
        e.setdefault("other_aliases", []); e.setdefault("kind", "other"); e.setdefault("myth", "")
        e.setdefault("note", ""); e.setdefault("source", ""); e.setdefault("date", ""); e.setdefault("tier", "")
        if e["kind"] not in KINDS:
            e["kind"] = "other"
        clean.append(e)
    os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
    json.dump({"subject": slug, "relations": clean}, open(out, "w"), ensure_ascii=False, indent=1)
    log(f"{slug}: DONE {len(clean)} relations -> {out}")
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    sys.exit(main(sys.argv[1], sys.argv[2]))
