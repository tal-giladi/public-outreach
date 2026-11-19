"""Build the public MK scorecard from official Knesset OData + our own letter log.

Run: py scripts/scorecard.py [--prev 25]
Writes scorecard/members.md, scorecard/ministries.md, scorecard/data.json.
Every number links back to a public, reproducible source (see scorecard/METHODOLOGY.md).
"""
import json
import re
import sys
import time
import urllib.parse
import urllib.request
from collections import defaultdict
from datetime import date, datetime
from pathlib import Path

BASE = "https://knesset.gov.il/OdataV4/ParliamentInfo"
ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "scorecard"
UA = {"User-Agent": "public-outreach-scorecard/1.0"}


def fetch(entity, **params):
    q = "&".join(f"${k}={urllib.parse.quote(str(v), safe='(),/')}" for k, v in params.items())
    url = f"{BASE}/{entity}?{q}"
    for attempt in range(4):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=90) as r:
                time.sleep(0.25)
                return json.load(r)
        except Exception:
            if attempt == 3:
                raise
            time.sleep(3 * (attempt + 1))


def get_all(entity, **params):
    data = fetch(entity, **params)
    rows = data["value"]
    while data.get("@odata.nextLink"):
        with urllib.request.urlopen(urllib.request.Request(data["@odata.nextLink"], headers=UA), timeout=90) as r:
            data = json.load(r)
        rows += data["value"]
        time.sleep(0.25)
    return rows


def count(entity, flt):
    return fetch(entity, filter=flt, count="true", top=0)["@odata.count"]


def d(s):
    return datetime.fromisoformat(s).date() if s else None


def iso(x):
    return x.isoformat()


def our_reply_stats():
    """Read letters/*.md front matter: to_id, status, sent_at, reply_at."""
    stats = defaultdict(lambda: {"sent": 0, "replied": 0, "days": []})
    for f in (ROOT / "letters").glob("*.md"):
        text = f.read_text(encoding="utf-8")
        m = re.match(r"---\n(.*?)\n---", text, re.S)
        if not m:
            continue
        fm = dict(re.findall(r"^(\w+):\s*(.*)$", m.group(1), re.M))
        if fm.get("status") in (None, "", "draft") or not fm.get("to_id"):
            continue
        s = stats[int(fm["to_id"])]
        s["sent"] += 1
        if fm.get("reply_at"):
            s["replied"] += 1
            try:
                s["days"].append((date.fromisoformat(fm["reply_at"]) - date.fromisoformat(fm["sent_at"])).days)
            except ValueError:
                pass
    return stats


def main():
    prev = int(sys.argv[sys.argv.index("--prev") + 1]) if "--prev" in sys.argv else None
    kn = get_all("KNS_KnessetDates", filter="IsCurrent eq true")[0]["KnessetNum"]
    prev = prev or kn - 1

    cur_pos = get_all("KNS_PersonToPosition", filter=f"KnessetNum eq {kn} and IsCurrent eq true")
    current_ids = sorted({p["PersonID"] for p in cur_pos})
    people = {p["Id"]: p for p in get_all("KNS_Person", filter="IsCurrent eq true")}
    faction = {}
    roles = defaultdict(set)
    for p in cur_pos:
        if p.get("FactionName"):
            faction[p["PersonID"]] = p["FactionName"]
        r = p.get("DutyDesc") or p.get("GovMinistryName")
        if r:
            roles[p["PersonID"]].add(r)

    prev_pos = get_all("KNS_PersonToPosition", filter=f"KnessetNum eq {prev}")
    prev_span = {}
    for p in prev_pos:
        s, e = d(p.get("StartDate")), d(p.get("FinishDate")) or date.today()
        if not s:
            continue
        a, b = prev_span.get(p["PersonID"], (s, e))
        prev_span[p["PersonID"]] = (min(a, s), max(b, e))

    replies = our_reply_stats()
    rows = []
    for i, pid in enumerate(current_ids, 1):
        p = people.get(pid)
        if not p:
            continue
        row = {"id": pid, "name": f"{p['FirstName']} {p['LastName']}", "faction": faction.get(pid, ""),
               "roles": sorted(roles[pid]), "email": (p.get("Email") or "").strip()}
        span = prev_span.get(pid)
        if span:
            a, b = span
            row["prev_member"] = True
            row["bills"] = count("KNS_BillInitiator",
                                 f"PersonID eq {pid} and IsInitiator eq true and KNS_Bill/KnessetNum eq {prev}")
            row["queries"] = count("KNS_Query", f"PersonID eq {pid} and KnessetNum eq {prev}")
            row["motions"] = count("KNS_Agenda", f"InitiatorPersonID eq {pid} and KnessetNum eq {prev}")
            total_votes = count("KNS_PlenumVote", f"VoteDateTime ge {iso(a)}T00:00:00Z and VoteDateTime le {iso(b)}T23:59:59Z")
            cast = count("KNS_PlenumVoteResult", f"MkId eq {pid} and VoteDate ge {iso(a)}T00:00:00Z and VoteDate le {iso(b)}T23:59:59Z")
            row["votes_cast"], row["votes_total"] = cast, total_votes
            row["vote_pct"] = round(100 * cast / total_votes) if total_votes else None
        else:
            row["prev_member"] = False
        r = replies.get(pid)
        row["our_sent"] = r["sent"] if r else 0
        row["our_replied"] = r["replied"] if r else 0
        row["our_median_days"] = sorted(r["days"])[len(r["days"]) // 2] if r and r["days"] else None
        rows.append(row)
        print(f"{i}/{len(current_ids)} {row['name']}", flush=True)

    # Ministries: how many parliamentary questions they answered, and how late.
    queries = get_all("KNS_Query", filter=f"KnessetNum eq {prev}",
                      select="Id,GovMinistryID,SubmitDate,ReplyMinisterDate,ReplyDatePlanned,TypeDesc")
    ministries = {m["Id"]: m["Name"] for m in get_all("KNS_GovMinistry")}
    mstats = defaultdict(lambda: {"asked": 0, "answered": 0, "late_days": []})
    for q in queries:
        s = mstats[q.get("GovMinistryID")]
        s["asked"] += 1
        if q.get("ReplyMinisterDate"):
            s["answered"] += 1
            planned, actual = d(q.get("ReplyDatePlanned")), d(q["ReplyMinisterDate"])
            if planned and actual:
                s["late_days"].append((actual - planned).days)

    OUT.mkdir(exist_ok=True)
    today = date.today().isoformat()
    (OUT / "data.json").write_text(json.dumps({"generated": today, "knesset": kn, "prev_knesset": prev,
                                               "members": rows, "ministries": {
                                                   ministries.get(k, str(k)): v for k, v in mstats.items()}},
                                              ensure_ascii=False, indent=1), encoding="utf-8")

    def cell(v, suffix=""):
        return "—" if v is None else f"{v}{suffix}"

    lines = [f"# Knesset {kn} members — public activity scorecard", "",
             f"Generated {today}. Activity columns cover the Knesset {prev} term (official Knesset OData). "
             "\"Our letters\" columns count only letters sent from this project. Method: [METHODOLOGY.md](METHODOLOGY.md). "
             "Attendance hours and committee presence from other trackers: [PUBLIC_SOURCES.md](PUBLIC_SOURCES.md).", "",
             f"| Name | Faction | Bills initiated (K{prev}) | Parliamentary questions (K{prev}) | Agenda motions (K{prev}) | Plenum votes cast | Our letters: sent / replied | Median reply days |",
             "|---|---|---|---|---|---|---|---|"]
    for r in sorted(rows, key=lambda r: r["name"]):
        if r["prev_member"]:
            votes = f"{r['votes_cast']}/{r['votes_total']} ({cell(r['vote_pct'], '%')})"
            act = [str(r["bills"]), str(r["queries"]), str(r["motions"]), votes]
        else:
            act = [f"new in K{kn}"] + ["—"] * 3
        lines.append(f"| {r['name']} | {r['faction']} | " + " | ".join(act) +
                     f" | {r['our_sent']} / {r['our_replied']} | {cell(r['our_median_days'])} |")
    (OUT / "members.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    ml = [f"# Ministries — answers to parliamentary questions (Knesset {prev})", "",
          f"Generated {today}. \"Late\" = answer date after the planned reply date in the Knesset record.", "",
          "| Ministry | Asked | Answered | Answered % | Median days late (answered) |", "|---|---|---|---|---|"]
    for name, s in sorted(((ministries.get(k, str(k)), v) for k, v in mstats.items()), key=lambda kv: -kv[1]["asked"]):
        late = sorted(s["late_days"])
        med = late[len(late) // 2] if late else None
        pct = round(100 * s["answered"] / s["asked"]) if s["asked"] else 0
        ml.append(f"| {name} | {s['asked']} | {s['answered']} | {pct}% | {cell(med)} |")
    (OUT / "ministries.md").write_text("\n".join(ml) + "\n", encoding="utf-8")
    print("done")


if __name__ == "__main__":
    main()
