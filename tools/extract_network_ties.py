#!/usr/bin/env python3
"""extract_network_ties.py -- run Codex ONCE (no web search) to pull the tie list out of one
dossier of a network set (cybernetic_elite and any later set with a NETWORK_PROMPT.md).

    python3 tools/extract_network_ties.py <set_dir> <dossier.md> <out.json>

Prompt = <set_dir>/NETWORK_PROMPT.md (after the first '---') + the dossier text. Codex prints a
JSON array; we take the last balanced [...] in its output and validate it. Exit 0 on success.
The sibling of extract_relations.py (pantheon), with the tie vocabulary of NETWORK_PROMPT.md.
"""
import json, os, re, subprocess, sys, time

LAB = os.path.expanduser("~/codex_lab")
CODEX = os.path.expanduser("~/.local/bin/codex")
KINDS = {"funded", "funded_by", "employed", "employed_by", "advised", "advised_by", "married", "related_to", "board_of",
         "founded", "founded_by", "member_of", "introduced", "introduced_by", "corresponded", "met", "flew_with",
         "co_authored", "published", "published_by", "invested_in", "invested_by", "donated_to", "received_from",
         "attacked", "attacked_by", "investigated", "investigated_by", "prosecuted", "prosecuted_by", "sued", "sued_by",
         "accused", "accused_by", "testified_about", "interviewed", "interviewed_by", "cited", "cited_by",
         "studied_under", "taught", "protected", "recruited", "other"}
TIERS = {"primary", "journalism", "alleged", "subject_claim", "rumor", "disproved"}
TYPES = {"person", "institution", "company", "foundation", "agency", "program", "publication", "event", "text", "place"}


def log(msg):
    line = time.strftime("%m-%d %H:%M:%S ") + "[network] " + msg
    print(line, flush=True)
    open(f"{LAB}/batch.log", "a").write(line + "\n")


def last_json_array(text):
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


def main(set_dir, doss, out):
    slug = os.path.basename(doss).replace(".dossier.md", "").replace(".md", "")
    tpl = open(os.path.join(set_dir, "NETWORK_PROMPT.md")).read().split("---", 1)[1].strip()
    body = open(doss).read()
    prompt = tpl + "\n\n" + body + "\n\nNow print the JSON array."
    logfile = f"{LAB}/net_{slug}.log"
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
        if not isinstance(e, dict) or not e.get("other"):
            continue
        for k in ("other_type", "kind", "note", "dates", "money", "source", "source_date", "tier"):
            e.setdefault(k, "")
        if e["kind"] not in KINDS: e["kind"] = "other"
        if e["tier"] not in TIERS: e["tier"] = "journalism" if e["tier"] else ""
        if e["other_type"] not in TYPES: e["other_type"] = "person"
        clean.append(e)
    os.makedirs(os.path.dirname(os.path.abspath(out)), exist_ok=True)
    json.dump({"subject": slug, "ties": clean}, open(out, "w"), ensure_ascii=False, indent=1)
    log(f"{slug}: DONE {len(clean)} ties -> {out}")
    return 0


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(__doc__)
    sys.exit(main(*sys.argv[1:4]))
