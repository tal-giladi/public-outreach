"""Committee protocols -> per-MK attendance and speaking numbers.

Run: py scripts/protocols.py [--knesset 25] [--limit N]
1. Lists every committee protocol of that Knesset from the official OData service.
2. Downloads each (cached in .cache/protocols/, resumable, polite rate).
3. Parses the "נכחו" attendance list and every speaking turn (<< יור >>, << דובר >>, << אורח >> tags).
4. Writes scorecard/protocols.json (per MK totals) and scorecard/protocols_unmatched.txt (names not matched to an MK).
"""
import json
import re
import sys
import time
import urllib.parse
import urllib.request
import zipfile
from collections import defaultdict
from pathlib import Path

BASE = "https://knesset.gov.il/OdataV4/ParliamentInfo"
ROOT = Path(__file__).resolve().parent.parent
CACHE = ROOT / ".cache" / "protocols"
UA = {"User-Agent": "public-outreach-protocols/1.0 (github.com/tal-giladi/public-outreach)"}
TAG = re.compile(r"<< (\S+) >>")


def get_all(entity, flt, select=None):
    q = f"$filter={urllib.parse.quote(flt, safe='(),/:')}"
    if select:
        q += f"&$select={select}"
    url, rows = f"{BASE}/{entity}?{q}", []
    while url:
        with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=120) as r:
            data = json.load(r)
        rows += data["value"]
        url = data.get("@odata.nextLink")
        time.sleep(0.2)
    return rows


def norm(name):
    name = re.sub(r"\(.*?\)", "", name)
    name = re.sub(r'היו"ר|היו״ר|יו"ר|מ"מ|ד"ר|פרופ\'|השר[הת]?|סגנ?ית? השר[הת]?|ח"כ|עו"ד', "", name)
    name = re.split(r"\s[–-]\s", name)[0]
    name = re.sub(r"[\"'״׳`]", "", name).replace("-", " ")
    return " ".join(name.split())


def paragraphs(path):
    try:
        x = zipfile.ZipFile(path).read("word/document.xml").decode("utf-8")
    except (zipfile.BadZipFile, KeyError):
        return None
    ps = [re.sub(r"<[^>]+>", "", p) for p in re.findall(r"<w:p[ >].*?</w:p>", x, re.S)]
    ps = [p.replace("&lt;", "<").replace("&gt;", ">").replace("&quot;", '"').replace("&amp;", "&").strip() for p in ps]
    return [p for p in ps if p]


def parse(ps):
    """Return (present_mks:set, speech: {name: [turns, words]}, n_guests:int, chair:str|None)."""
    present, guests, chair = set(), 0, None
    section = None
    for p in ps:
        m = TAG.match(p)
        if m and m.group(1) in ("יור", "דובר", "אורח"):
            break
        if m:
            continue
        if p in ("חברי הוועדה:", "חברי הכנסת:"):
            section = "mk"; continue
        if p == "מוזמנים:":
            section = "guest"; continue
        if p.endswith(":") and len(p) < 40:
            section = None; continue
        if section == "mk":
            present.add(norm(p))
        elif section == "guest" and p not in ("–", "-"):
            guests += 1
    guests //= 2  # each guest = name line + role line
    speech, cur = defaultdict(lambda: [0, 0]), None
    for p in ps:
        m = TAG.match(p)
        if m:
            kind = m.group(1)
            if kind in ("יור", "דובר", "אורח"):
                cur = norm(TAG.sub("", p).strip().rstrip(":"))
                speech[cur][0] += 1
                if kind == "יור" and not chair:
                    chair = cur
            else:
                cur = None
            continue
        if cur:
            speech[cur][1] += len(p.split())
    return present, dict(speech), guests, chair


def main():
    kn = int(sys.argv[sys.argv.index("--knesset") + 1]) if "--knesset" in sys.argv else 25
    limit = int(sys.argv[sys.argv.index("--limit") + 1]) if "--limit" in sys.argv else None
    CACHE.mkdir(parents=True, exist_ok=True)

    docs = get_all("KNS_DocumentCommitteeSession",
                   f"GroupTypeID eq 23 and startswith(FilePath,'https://fs.knesset.gov.il/{kn}/')",
                   "Id,CommitteeSessionID,DocumentName,FilePath")
    by_session = {}
    for d in docs:
        if d["CommitteeSessionID"] not in by_session or d["Id"] > by_session[d["CommitteeSessionID"]]["Id"]:
            by_session[d["CommitteeSessionID"]] = d
    sessions = sorted(by_session.values(), key=lambda d: d["Id"])[:limit]
    print(f"Knesset {kn}: {len(sessions)} sessions with a protocol", flush=True)

    mks = {}
    for line in (ROOT / "contacts" / "knesset-members.md").read_text(encoding="utf-8").splitlines():
        m = re.match(r"^\| (\d+) \| ([^|]+) \|", line)
        if m:
            mks[norm(m.group(2))] = int(m.group(1))

    stats = defaultdict(lambda: {"present": 0, "spoke": 0, "turns": 0, "words": 0, "chaired": 0})
    unmatched, bad = defaultdict(int), 0
    for i, d in enumerate(sessions, 1):
        f = CACHE / Path(urllib.parse.urlparse(d["FilePath"]).path).name
        if not f.exists():
            try:
                req = urllib.request.Request(d["FilePath"], headers=UA)
                with urllib.request.urlopen(req, timeout=120) as r:
                    f.write_bytes(r.read())
                time.sleep(0.3)
            except Exception as e:
                print(f"skip {d['FilePath']}: {e}", flush=True)
                bad += 1
                continue
        ps = paragraphs(f)
        if ps is None:
            bad += 1
            continue
        present, speech, guests, chair = parse(ps)
        spoke_mks = {n for n in speech if n in mks}
        for n in present | spoke_mks:
            if n in mks:
                stats[mks[n]]["present"] += 1
            else:
                unmatched[n] += 1
        for n in spoke_mks:
            s = stats[mks[n]]
            s["spoke"] += 1
            s["turns"] += speech[n][0]
            s["words"] += speech[n][1]
        if chair in mks:
            stats[mks[chair]]["chaired"] += 1
        if i % 250 == 0:
            print(f"{i}/{len(sessions)}", flush=True)

    out = {"knesset": kn, "sessions": len(sessions), "unreadable": bad, "members": {str(k): v for k, v in stats.items()}}
    (ROOT / "scorecard" / "protocols.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    (ROOT / "scorecard" / "protocols_unmatched.txt").write_text(
        "\n".join(f"{c}\t{n}" for n, c in sorted(unmatched.items(), key=lambda kv: -kv[1])), encoding="utf-8")
    print(f"done: {len(sessions)} sessions, {bad} unreadable, {len(stats)} MKs matched", flush=True)


if __name__ == "__main__":
    main()
