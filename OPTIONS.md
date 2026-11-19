# Public-interest outreach — options (research, 19.11.2026)

Goal: write to MKs and senior public officials about issues that bother the public (example: road deaths), track everything locally in md files, and get real change — not just "sent emails".

## The honest bottom line

Mass email to all 120 MKs is the weakest lever. Staff delete identical letters. What moves things in Israel, roughly from strongest to weakest:

1. A formal procedure that legally obliges a reply or a decision (FOI request, Ombudsman complaint, State Comptroller complaint, objection to a draft law/regulation).
2. Getting the issue onto a Knesset committee agenda (a committee session forces the ministry to show up and answer on the record).
3. One specific MK (or 2–3) who owns the issue and files a parliamentary question / motion for the agenda / bill.
4. Media + data: an original, verifiable number nobody published before.
5. Bulk letters.

So the automation should support all five, with the tracker as the spine.

## Option A — Targeted MK letters (what you described, done right)

- Who: not all 120. Pick the members of the relevant committee (road safety → Economic Affairs Committee and any road-safety subcommittee; check the current Knesset), plus MKs who already spoke on the issue (searchable in committee protocols / plenum).
- Addresses: MK emails are public on the Knesset site (pattern `name@knesset.gov.il`). The official OData service (`https://knesset.gov.il/OdataV4/ParliamentInfo/`) gives names, factions, committee membership — emails not confirmed there, so we scrape/verify from the MK pages once and store them in `contacts/`.
- Each letter: personal (names their committee/past statement), one concrete ask ("file a parliamentary question to the Transport Minister asking X"), one page, sources linked.
- Follow-up after 14 days; second follow-up by phone to the parliamentary aide (aides' names are on the MK pages).
- Legal: political/advocacy email is not "advertising" under the anti-spam section 30A of the Communications Law (courts held political messages are outside it). Still: send individually, from a real named address, no mass BCC, include opt-out — deliverability and reputation, not law.

## Option B — Knesset committees

- Every committee accepts position papers by email to the committee coordinator before a session; papers get distributed to members and can be quoted in the protocol.
- You can ask to speak at a session (the course already has `templates/committee-participation-request.md`).
- Automation: watch the committee agendas (OData has sessions/agenda items) and alert when a session matches our keywords → send a position paper within the window.

## Option C — Duty-to-answer channels (the strongest)

- Freedom of Information Act 1998: ask the ministry/authority for the data (e.g., National Road Safety Authority: enforcement cameras installed vs. budgeted, dangerous-junction list and fix dates). They must answer within 30 days (extendable). Template: `templates/foi-request.md`; complaint path: `templates/foi-unit-complaint.md`.
- State Comptroller / Ombudsman (Commissioner for Public Complaints): for a specific failure by a public body.
- Public comment on draft laws and regulations (government memoranda site and "public participation" on gov.il): ministries must publish and consider comments.
- Municipalities: council questions (`templates/council-question-request.md`) — many dangerous roads/junctions are local.
- Last resort: administrative petition / HCJ petition (templates exist in this repo; needs a lawyer).

## Option D — Data + media

- Public data: CBS and the National Road Safety Authority publish accident data by location; data.gov.il has datasets.
- A local, specific finding ("this junction: 9 deaths in 5 years, plan approved in 2019, not built") gets press and gives MKs a ready-made question.
- Send to journalists who cover the beat; track them in the same contact list.

## Option E — Coalitions

- Existing NGOs (road safety: e.g., Or Yarok; other topics: relevant amutot) already have MK relationships. Offering them data/research gets further than starting from zero.
- Later: a group of citizens sending personal (not identical) letters, coordinated from the same tracker.

## Proposed local system (md files, git-tracked)

```
outreach/
  issues/road-safety.md        # the issue: facts, sources, the concrete asks, status
  contacts/mk-<name>.md        # one per person: role, committees, email, aide, past statements, history
  letters/2026-11-20-road-safety-mk-<name>.md   # exact text sent, front matter: to, date, issue, channel
  log.md                       # one line per event: date | who | channel | what | status
  deadlines.md                 # FOI 30-day clocks, follow-ups due, committee sessions
```

Front matter on each letter: `status: draft | sent | replied | no-reply | follow-up-due`, `sent_at`, `reply_at`, `reply_summary`.

Automation (Claude-driven, you approve every send):
1. Build contacts from the Knesset OData + MK pages.
2. Draft personalized letters from the issue file → you approve → send from a dedicated Gmail/agent mailbox (Gmail connector or the AgentMail inbox).
3. Daily scheduled task: check the inbox for replies, match to the thread, update the letter's status and `log.md`, flag due follow-ups and FOI deadlines.
4. Weekly: committee-agenda watch for issue keywords.

## Suggested first campaign (road safety)

1. FOI to the National Road Safety Authority + Transport Ministry for the specific data.
2. Pick 5–8 MKs (relevant committee + those who spoke on it) → personal letters with one ask each.
3. Position paper to the committee at its next relevant session.
4. Publish the finding when the FOI answer arrives.

## Sources

- Knesset OData: https://knesset.gov.il/OdataV4/ParliamentInfo/
- Open Knesset API (legacy, had MK emails): https://oknesset-api.readthedocs.io/en/stable/api_v2/interacting.html
- Anti-spam and political messages: https://www.bizportal.co.il/takdin/news/article/20016683 , https://www.chamber.org.il/serviceslobby/legal/74023/115485/
- Examples of NGO position papers to Knesset committees: https://law.acri.org.il/he/wp-content/uploads/2017/06/knesst-reforms-220517.pdf
- This repo: `templates/`, `projects/m05-foi-to-petition.md`, `references/where-to-get-help.md`
