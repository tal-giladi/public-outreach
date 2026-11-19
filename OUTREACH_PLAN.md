# Outreach plan — email is our only power, so we use all of it

Tal's approach, 19.11.2026: no budget, no organisation behind us. The one thing we can do at scale is send email. Every campaign should reach as many people as possible: not only the Knesset, but every official, organisation, journalist and citizen who can move the issue.

The plan below maximises reach **without** getting the project shut down. Two things can kill it overnight:

1. **The anti-spam law** (Communications Law, section 30A): a message sent "to the public" as **propaganda (תעמולה) or a donation request** counts as advertising and needs the recipient's **prior consent**. Each unsolicited message can cost up to **₪1,000** in a lawsuit, with no need to prove damage ([Kol Zchut](https://www.kolzchut.org.il/he/%D7%A4%D7%99%D7%A6%D7%95%D7%99_%D7%91%D7%92%D7%99%D7%9F_%D7%9E%D7%A9%D7%9C%D7%95%D7%97_%D7%93%D7%91%D7%A8%D7%99_%D7%A4%D7%A8%D7%A1%D7%95%D7%9E%D7%AA_%D7%9C%D7%9C%D7%90_%D7%94%D7%A1%D7%9B%D7%9E%D7%94_%D7%A9%D7%9C_%D7%94%D7%A0%D7%9E%D7%A2%D7%9F_(%D7%97%D7%95%D7%A7_%D7%94%D7%A1%D7%A4%D7%90%D7%9D))). 5,000 cold emails to private people = a theoretical ₪5 million exposure.
2. **Deliverability**: a new address sending thousands of unsolicited emails gets flagged as spam within days, and then even the MKs stop receiving us.

So: officials and organisations get written to directly; private people are reached through consent and through each other. A lawyer should confirm the line before round 1 (see the end).

## Who we write to, in three rings

### Ring 1 — Public officials (write directly, at official addresses)

Writing to an official about their public duty is not "advertising to the public". Individual emails, official published addresses, one clear ask.

| Group | About how many | Where the addresses come from | Status |
|---|---|---|---|
| Members of Knesset | 120 | Knesset open data | Have (`contacts/knesset-members.md`) |
| Ministers and deputy ministers | ~35 | Knesset open data + gov.il | Partly have |
| Knesset committees (coordinators) | ~30 | Knesset open data | Have (`contacts/knesset-committees.md`) |
| Directors-general and relevant heads: Transport Ministry, Road Safety Authority, Police traffic division, Finance (budgets), Education (school routes) | ~30 | gov.il ministry pages | To collect |
| Heads of local authorities | 257 | Local authority sites, data.gov.il, Union of Local Authorities | To collect |
| Municipal traffic-safety officers (ממוני בטיחות בדרכים) and city engineers | ~500 | Local authority sites | To collect |
| City council members | ~3,000 | Local authority sites | To collect, largest cities first |
| Oversight bodies: State Comptroller, Ombudsman, Knesset Research Center | ~5 | Official sites | To collect |

Ring 1 is about **4,000 addresses**, all legitimate. Local officials matter most for pedestrians: crosswalks, bumps, daylighting and signal timing are municipal decisions.

### Ring 2 — Organisations and media (one personal email, opt-out, no blasting)

Published work addresses, a message relevant to their work, written to them by name, with "reply 'stop' and I won't write again".

| Group | About how many | Source | Status |
|---|---|---|---|
| Road-safety and pedestrian NGOs | ~15 | `partners/road-safety.md` | Started |
| Bereaved-family organisations | ~3 | `partners/road-safety.md`, only under the rules there | Started |
| Parents' bodies (national parents' leadership, city parents' committees) | ~100 | Their sites | To collect |
| Senior-citizen organisations (65+ = 45% of pedestrian deaths) | ~20 | Their sites | To collect |
| Disability organisations (accessible crossings) | ~15 | Their sites | To collect |
| Resident and neighbourhood associations | ~200 | Local sites | Later |
| Transport and road-safety researchers (Technion, universities) | ~50 | University pages | To collect |
| Journalists: transport, local news, Knesset reporters | ~150 | Bylines, outlet contact pages | To collect |
| Organisations that appear in Knesset road-safety sessions | from protocols | `scripts/protocols.py` guest lists | Tool ready |

Ring 2 is about **700 addresses**. Each of them has its own list and audience: one partner newsletter reaches more private people than we ever could, legally.

### Ring 3 — Private people (consent first, then they multiply us)

We do **not** cold-email private people. We make it easy for them to come to us, and then each one sends on our behalf, from their own address:

1. **Sign-up on the site**: "קבלו עדכון כשחבר הכנסת שלכם עונה". One field (email), explicit consent checkbox, confirmation email (double opt-in). This is our own list.
2. **"Write to your MK / mayor" in one click**: a page per campaign with a ready message (`mailto:` link, prefilled subject and text) addressed to the official. The citizen sends it from their own email. 1,000 citizens = 1,000 emails from real voters, which MK offices count far more than one email from us. No spam-law issue: each person writes in their own name.
3. **Forward to friends**: every update ends with "Forward this to 3 people who cross the street every day."
4. **Partners send to their own lists**: Or Yarok, parents' bodies and others already have consent from their audiences; we give them a ready text and the sign-up link.
5. **Media**: every published result ("X of 120 MKs answered") is a press story, and every story links to the sign-up.

## The campaign cycle (repeat for each campaign)

| Step | When | Ring | What |
|---|---|---|---|
| 1 | Week −2 | — | Issue file, facts verified, emails written, method published |
| 2 | Week −1 | 2 | Personal emails to partner organisations and journalists: "this starts next week, here is the data" |
| 3 | Week 0 | 3 | Campaign page live: sign-up + one-click "write to your MK / mayor" |
| 4 | Weeks 1–6 | 1 | The email series to all officials (road safety: 12 emails, `campaigns/road-safety/`) |
| 5 | Weekly | 3 | Short update to the sign-up list: who answered this week, one action for them |
| 6 | Every 2 weeks | 2 | Data to journalists and partners: answer rates, new commitments |
| 7 | Week 8 | all | Results published; thank-you to officials who acted; next campaign announced |

## Sending capacity

| Tool | Limit | Cost | Use |
|---|---|---|---|
| Gmail (new address) | ~500 emails/day | Free | Ring 1 at first: 120 MKs a day is fine |
| Google Workspace on our own domain | ~2,000/day | ~$6/month | Ring 1 at full size (~4,000 over 2–3 days) |
| An email service with free tier (e.g. Brevo, MailerLite) | Free up to a few hundred/day or ~1,000 subscribers | Free | Ring 3 sign-up list only (consented) |

Rules: our own domain with SPF, DKIM and DMARC set up before the first big send; warm the address up (start with tens a day, grow over 2–3 weeks); one recipient per email for Rings 1–2; never buy or scrape lists of private people. Tal works in email marketing, so he knows these better than anyone; if the service used is his employer's, say so publicly to keep the independence statement true.

## What to build (in this repo, when Tal says go)

| Tool | Does |
|---|---|
| `contacts/` collectors | Local authority heads, safety officers, council members, ministry officials, organisations, journalists → one file per group, each address with its public source |
| `make_letters.py` | One letter file per recipient from the campaign emails |
| `send.py` | Sends approved letters at a safe daily rate, logs each send; never sends without Tal's go |
| `check_replies.py` | Matches replies, updates status, flags bounces and "stop" requests |
| Campaign page | Sign-up + one-click "write to your MK / mayor" (mailto links, no server needed) |
| Supporter list | Double opt-in sign-up through a free email service |
| Scoreboard | Add mayors and local authorities next to MKs |

## Open decisions for Tal

- Lawyer check (an hour with someone who knows section 30A): confirm Ring 1 and Ring 2 are fine as designed, and the exact wording for the sign-up consent. The activist-law course already covers the law; a pro-bono lawyer from a partner organisation is the cheapest route.
- Which email service for the consented list.
- Which cities first for council members (suggestion: the 10 cities with the most pedestrian deaths, from the Road Safety Authority data).
