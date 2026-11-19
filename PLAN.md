# Plan

Reviewed 19.11.2026. Replaces the action list in OPTIONS.md (that file stays as the background research).

## What we are

The first public, repeated, documented measurement of whether Israeli MKs answer the public. The last one was ynet in 2007 (36 of 119 answered). Every round asks every MK one real question on a non-partisan public issue, publishes the letter, and publishes who answered.

The reply rate is the hook. The question itself must still be worth answering, so every round also pushes a real issue (round 1: road deaths).

## Credibility rules (if these break, the project is worthless)

1. **Publish the method before sending.** METHODOLOGY.md and the exact letter are committed to GitHub before the first email; the commit date proves we did not change the rules after seeing results.
2. **Same letter to everyone.** Identical Hebrew text, only the name changes. Sent individually (one email per MK, no BCC), same day, from the same named sender.
3. **Only real MKs.** The 120 sitting MKs. Ministers who resigned their seat under the Norwegian law are not MKs; they get their own table if we write to them at all.
4. **A fair window.** 30 days to answer, one reminder on day 21 (same as ynet 2007, so the numbers compare).
5. **Clear definition of a reply.** Counts: any human answer from the MK or their office, including "we passed it on". Does not count: auto-reply, read receipt. A bounce → resend to the office's alternative address from the Knesset site; if no working address exists, the MK is marked "unreachable", not "did not answer".
6. **Right to correct.** Before publishing results, every MK marked "no reply" gets a final email: "our record shows no reply; if you answered, tell us". Corrections go in the git history.
7. **Publish summaries, not people.** Replies are summarised in our words; aides' names and personal details are not published. Full replies stay in `replies/` (not pushed).
8. **Neutral topics, neutral wording.** Every round's topic must be one every faction can support. No party is singled out in the write-up; tables are alphabetical, not "worst to best".
9. **Honest comparison.** Our letter says it will be published. That may raise reply rates compared with 2007; we say so next to the comparison.

## Timing

The 26th Knesset was sworn in on 10.11.2026. Permanent committees are not formed yet and offices are still being set up. Measuring now would punish new MKs for setup delays.

- Now → committees formed: publish method + letter, build the sending and tracking tools, send the FOI request on road safety (it is not about MKs and takes 30+ days anyway).
- First week after permanent committees are formed: round 1 goes out.
- Round 1 + 30 days: publish results.
- Then one round per Knesset session (about 3 a year), each on a new topic, so we get a trend per MK.

## Round 1 checklist

1. Fix data: drop the 5 non-MK ministers from the MK list; fix the 3 broken addresses (Eisenkot, Feiglin missing; Kroizer typo).
2. Tal picks subjects (main or alternate) for the 12 emails in campaigns/road-safety/.
3. Pick the sending mailbox: one dedicated address under Tal's real name (Gmail limit 500/day is enough).
4. Commit method + final letter (the "pre-registration" commit).
5. Generate 120 letter files from the approved text; send all on one day; log each send.
6. Daily: check the inbox, match replies to letters, update status, log.
7. Day 21: reminders to everyone with no reply.
8. Day 30: right-to-correct email.
9. Day 37: publish results table + a short write-up; send it to journalists and to the trackers below.

## Getting heard

- Partners that already have an audience and MK data: Shakuf (Parlameter), Knesset Time, Shomrim. Offer them our data for free; one mention from them reaches more people than we can.
- Journalists who cover the Knesset: the story is "20 years later, do MKs answer?" plus the issue itself.
- Each MK who answers well is credited by name; that makes answering attractive, not only silence embarrassing.

## Tools to build (in this repo)

| Script | Does |
|---|---|
| `sync_knesset.py` | MK list and emails (exists; needs the non-MK fix) |
| `make_letters.py` | Approved draft → one letter file per MK with front matter |
| `send.py` | Sends approved letters, one by one, writes `sent_at`; never sends without Tal's go |
| `check_replies.py` | Reads the inbox, matches replies by thread, fills `reply_at`, flags bounces |
| `scorecard.py` | Rebuilds the tables (exists) |

## Data inventory

| Data | Source | Cost | Status |
|---|---|---|---|
| MK list, emails, factions, roles | Knesset OData | Free | Live (`sync_knesset.py`) |
| Bills, parliamentary questions, agenda motions, plenum votes | Knesset OData | Free | Live on the site (`scorecard.py`) |
| Ministries' answers to parliamentary questions | Knesset OData | Free | Live on the site |
| Committee attendance, speaking turns and words, chairing, invited public | Committee protocols (Word files, ~10,855 sessions in K25) | Free | Parser built and tested on one protocol (`protocols.py`); full run not started |
| Plenum speeches | Plenum protocols | Free | Same parser, not adapted yet |
| Ministers' meeting diaries | gov.il / foi.gov.il, per ministry | Free (FOI where missing) | Not collected |
| Ethics Committee decisions | Knesset site | Free | Not collected |
| Social accounts | Wikidata | Free | 67 of 120 MKs mapped (`contacts/social-accounts.md`) |
| YouTube comment replies | YouTube Data API | Free | Not built |
| Telegram posting | Public channels | Free | Not built |
| X replies to the public | X API | ~$40–180/month | On hold (Tal deciding) |
| Facebook / Instagram / TikTok | Researcher programmes | Free if approved | Needs an amuta or university partner |
| Our letters: replies | Our own mailbox | Free | Waiting: new mailbox, letter improvements |
| Past email-reply tests | ynet 2005, 2007 | — | Documented (`PUBLIC_SOURCES.md`) |

## Later, if it works

- Register an amuta (nonprofit) so the project is not one person; the course has a template.
- Add municipalities (council members) with the same method.
- A simple public site generated from the Markdown (GitHub Pages).

## Open decisions for Tal

- Mailbox to send from.
- Approve the letter.
- Whether round 1 also writes to the non-MK ministers.
