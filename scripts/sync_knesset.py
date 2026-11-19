"""Pull current MKs and committees from the Knesset OData service into contacts/.

Run: py scripts/sync_knesset.py
Writes contacts/knesset-members.md and contacts/knesset-committees.md (regenerated each run).
Per-person history lives in contacts/mk-<id>.md and is never overwritten.
"""
import json
import re
import urllib.parse
import urllib.request
from datetime import date
from pathlib import Path

BASE = "https://knesset.gov.il/OdataV4/ParliamentInfo"
ROOT = Path(__file__).resolve().parent.parent
EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[A-Za-z]{2,}$")
KNOWN_TLDS = ("knesset.gov.il", ".gov.il", ".co.il", ".org.il", ".com", ".net", ".org")


def get_all(entity, **params):
    query = urllib.parse.urlencode({f"${k}": v for k, v in params.items()}, safe="(),$ ")
    url = f"{BASE}/{entity}?{query}".replace(" ", "%20")
    rows = []
    while url:
        with urllib.request.urlopen(url, timeout=60) as r:
            data = json.load(r)
        rows += data["value"]
        url = data.get("@odata.nextLink")
    return rows


def current_knesset():
    return get_all("KNS_KnessetDates", filter="IsCurrent eq true")[0]["KnessetNum"]


def main():
    kn = current_knesset()
    positions = get_all("KNS_PersonToPosition", filter=f"KnessetNum eq {kn} and IsCurrent eq true")
    person_ids = sorted({p["PersonID"] for p in positions})
    people = {p["Id"]: p for p in get_all("KNS_Person", filter="IsCurrent eq true")}
    for pid in person_ids:
        if pid not in people:
            for p in get_all("KNS_Person", filter=f"Id eq {pid}"):
                people[pid] = p

    by_person = {}
    for pos in positions:
        by_person.setdefault(pos["PersonID"], []).append(pos)

    committees = get_all("KNS_Committee", filter=f"KnessetNum eq {kn}")

    today = date.today().isoformat()
    lines = [f"# Knesset {kn} — current members", "",
             f"Generated {today} from the Knesset OData service. Do not edit by hand; run `py scripts/sync_knesset.py`.", "",
             "| ID | Name | Faction | Roles | Email |", "|---|---|---|---|---|"]
    for pid, poss in sorted(by_person.items(), key=lambda kv: people.get(kv[0], {}).get("LastName", "")):
        p = people.get(pid)
        if not p:
            continue
        faction = next((x["FactionName"] for x in poss if x.get("FactionName")), "")
        roles = sorted({x.get("DutyDesc") or x.get("CommitteeName") or x.get("GovMinistryName") or "" for x in poss} - {""})
        email = (p.get("Email") or "").strip()
        if not EMAIL_RE.match(email):
            email = "MISSING"
        elif not email.lower().endswith(KNOWN_TLDS):
            email = f"CHECK {email}"
        lines.append(f"| {pid} | {p['FirstName']} {p['LastName']} | {faction} | {'; '.join(roles)} | {email} |")
    (ROOT / "contacts" / "knesset-members.md").write_text("\n".join(lines) + "\n", encoding="utf-8")

    cl = [f"# Knesset {kn} — committees", "", f"Generated {today}.", "",
          "| ID | Name | Type | Email | Current |", "|---|---|---|---|---|"]
    for c in sorted(committees, key=lambda c: c["Name"]):
        cl.append(f"| {c['Id']} | {c['Name']} | {c.get('CommitteeTypeDesc') or ''} | {c.get('Email') or ''} | {c.get('IsCurrent')} |")
    (ROOT / "contacts" / "knesset-committees.md").write_text("\n".join(cl) + "\n", encoding="utf-8")

    missing = sum(1 for l in lines if l.endswith("MISSING |"))
    print(f"Knesset {kn}: {len(by_person)} people, {missing} without a valid email, {len(committees)} committees")


if __name__ == "__main__":
    main()
