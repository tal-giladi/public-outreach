# Roadmap — campaign 1: "לחזור הביתה" (road safety)

Written 19.11.2026 by the campaign manager (Claude) for Tal. Who does what: **Tal** = needs you (money, accounts, approvals, your name). **Claude** = I build or prepare it; nothing goes out without your go.

**Launch (Day 0): Sunday 3.1.2027.** Chosen because the 26th Knesset offices will be set up by then, it is after Hanukkah (4–12.12.2026), and it leaves six weeks to build everything properly. If the permanent Knesset committees are still not formed by 27.12, we launch anyway: the letters go to MKs and to local authorities, which do not depend on the committees.

## At a glance

| Phase | Dates | Goal |
|---|---|---|
| 0. Foundations | 20.11 – 13.12.2026 | Domain, mailbox ready to send, legal check, contact lists, sending tools, FOI requests out |
| 1. Pre-launch | 14.12 – 2.1.2027 | Campaign page live, partners and journalists briefed, mailbox warmed up |
| 2. The series | 3.1 – 10.2.2027 | 12 emails to ~4,700 officials and organisations, twice a week |
| 3. Close and publish | 11.2 – 3.3.2027 | Reply window, right to correct, results published, press |
| 4. Next campaign | from 4.3.2027 | Pick topic 2, reuse everything |

## Phase 0 — Foundations (20.11 – 13.12.2026)

### Week of 22.11
| Who | Task | Done when |
|---|---|---|
| Tal | Buy `bachaim.org.il` (+ `bechaim.org.il`, `bachaim.co.il` optional) | Domain bought |
| Claude | Connect the domain to the site; give Tal the DNS records | Site opens at bachaim.org.il with HTTPS |
| Tal | Turn on 2-step verification on magiim.bachaim@gmail.com; create an app password for sending | App password stored in Credential Manager |
| Claude | Draft FOI requests to the Road Safety Authority, Transport Ministry and Police traffic division (questions in `issues/road-safety.md`) | Drafts ready for Tal |
| Tal | Approve and send the FOI requests (fee is small, paid online) | Sent by **26.11** → answers due about **26.12** |
| Claude | Choose subjects proposal: main or alternate for each of the 12 emails | Tal picks |

### Week of 29.11
| Who | Task | Done when |
|---|---|---|
| Claude | Collect Ring 1 contacts: ministers, directors-general, 257 heads of local authorities, traffic-safety officers, city engineers | `contacts/` files, each address with its public source |
| Claude | Collect Ring 2 contacts: NGOs, parents' bodies, senior and disability organisations, researchers, journalists | `contacts/` files |
| Claude | Run the protocol parser on 25th-Knesset road-safety sessions → map of every organisation that took part | Coalition list in `partners/` |
| Tal | One hour with a lawyer (pro-bono via a partner NGO, or paid): political-message reading of section 30A, opt-out wording | Notes in `OUTREACH_PLAN.md` |
| Tal | Start mailbox warm-up: send normal personal emails from it every day (friends, sign-ups, replies) | 10–20 real emails a day |

### Week of 6.12 (Hanukkah)
| Who | Task | Done when |
|---|---|---|
| Claude | Build `make_letters.py`, `send.py` (safe daily rate, log, stop list), `check_replies.py` (match replies, bounces, "stop") | Dry run on 5 test addresses of Tal's |
| Claude | Add local authorities to the scoreboard (heads of authorities next to MKs) | Live on the site |
| Tal | Decide: register an amuta now or later | Decision in `PLAN.md` |
| Claude | City council members for the 10 cities with the most pedestrian deaths | Contacts ready |

## Phase 1 — Pre-launch (14.12.2026 – 2.1.2027)

| Date | Who | Task |
|---|---|---|
| 14–17.12 | Claude | Build the campaign page: the problem in one screen, sign-up (consent checkbox), one-click "write to your MK / mayor" |
| 14–17.12 | Claude | Generate all 4,700 × 12 letter files; spot-check 20 |
| 18.12 | Tal | Review the campaign page and 5 sample letters; approve |
| 20.12 | Claude → Tal approves | **Partner intros** (Ring 2, personal): Or Yarok, Beterem, Yad Hanik'tafim, Transportation Today & Tomorrow, parents and senior organisations: "this starts on 3.1, here is the data, here is what we offer" |
| 20–31.12 | Tal | Mailbox warm-up continues; grow to ~100 emails a day (Ring 2 intros count) |
| 24.12 | Claude | Publish the method and the 12 emails (the "pre-registration" commit) |
| ~26.12 | Claude | FOI answers arrive (or the 30-day deadline passes: send the FOI-unit complaint) → add facts to emails 06–07 |
| 27.12 | Claude → Tal approves | Campaign page live; journalists briefed (Ring 2): "3.1, all MKs and mayors get the same letter; results published" |
| 31.12 | Tal + Claude | Final check: data, links, sending tool, stop list. **Go / no-go** |

## Phase 2 — The series (3.1 – 10.2.2027)

Every send day: emails go out from 08:00 at a safe rate (MKs and ministers first, then local authorities, then organisations); I log everything and report the same evening.

| Week | Sunday | Wednesday |
|---|---|---|
| 1 | **3.1** — 01 Change is possible | **6.1** — 02 The economic cost |
| 2 | **10.1** — 03 Children and pedestrians | **13.1** — 04 Human error |
| 3 | **17.1** — 05 Speed where people live | **20.1** — 06 Budget not executed |
| 4 | **24.1** — 07 The plan exists | **27.1** — 08 Clear responsibility |
| 5 | **31.1** — 09 Serious injuries | **3.2** — 10 Act before disaster |
| 6 | **7.2** — 11 Enforcement by results | **10.2** — 12 A commitment we can check |

Running in parallel, every week:
| Day | Who | Task |
|---|---|---|
| Daily | Claude | Check replies; classify (reply / commitment / done / stop); send the right follow-up (F1–F3) for Tal's approval; update the log |
| Monday | Claude | Update the scoreboard: who answered, who committed |
| Tuesday | Claude → Tal approves | Short update to the sign-up list: "this week X answered; one thing you can do" |
| Thursday (every 2 weeks) | Claude → Tal approves | Numbers to journalists and partners |
| Any day | Tal | Phone calls to offices that replied with a commitment (a person's voice closes the deal) |

Resends: offices that have not answered any email get each email once more, 4–5 days later (Thursday for Sunday's email, Monday for Wednesday's), with the second subject line.

Stop rule: an office that commits to an action with a date leaves the series and gets personal follow-up around that date.

## Phase 3 — Close and publish (11.2 – 3.3.2027)

| Date | Who | Task |
|---|---|---|
| 24.2 | Claude | Reply window closes (14 days after email 12). Right-to-correct email to everyone marked "no reply" |
| 1.3 | Claude | Results page: answered / committed / done, per MK and per local authority, with every letter linked |
| 2.3 | Tal | Review and approve the results |
| **3.3** | Tal + Claude | **Publish.** Press release to journalists; thank-you to every official who acted; update to sign-up list and partners |

## Phase 4 — Next campaign (from 4.3.2027)

- 4–10.3: retrospective (what worked, answer rates per email, which subjects opened best).
- Choose topic 2 from what the public raised during campaign 1.
- Same machine: issue file → emails → schedule → three rings → publish. Target launch about 6 weeks later.

## What I report to you, and when

- **Every send day, evening**: one line — sent, replies, commitments, problems.
- **Every Sunday**: the week ahead and anything waiting for your approval.
- Anything that needs your money, your accounts or your name, I ask first.

## Risks and what we do

| Risk | What we do |
|---|---|
| Gmail limits or spam flags | Warm-up from December, own domain with SPF/DKIM/DMARC, slow rate; move to Google Workspace on the domain if needed (~$6/month) |
| Knesset committees not formed by launch | Launch anyway; the follow-up debate asks wait until they exist |
| Legal complaint about the emails | Opt-out in every email, honoured at once; lawyer's notes on file; amuta as second basis |
| Low reply rates | That is itself the story: "X of 120 did not answer about 128 dead pedestrians" |
| Tal's time | Everything is prepared; Tal's part is approvals, phone calls and his name |
