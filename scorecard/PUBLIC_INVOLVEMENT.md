# Public involvement beyond our emails — what we can measure

Research, 19.11.2026. Goal: does each MK talk *with* the public (answers, replies), not only *to* it (posts)?

## Channel by channel

| Channel | Can we read it? | Cost | What it shows per MK | Verdict |
|---|---|---|---|---|
| **X (Twitter)** | Yes, official API, pay-per-use: about $0.005 per post read ([X docs](https://docs.x.com/x-api/getting-started/pricing)) | 120 MKs × ~300 posts/month ≈ 36,000 reads ≈ $180/month; less if we sample one week a month | Posts, and **replies to ordinary users** (not to other politicians or journalists). Closest thing to "do they answer the public" | Best single source. Start with a monthly one-week sample (~$40) |
| **YouTube** | Yes, free official Data API | Free (daily quota) | Videos, and whether the channel owner **replies to comments** | Do it. Few MKs active, but the reply data is exact |
| **Telegram** | Yes, public channels are open | Free | Posting frequency. Channels are one-way, so no replies | Activity only |
| **Facebook / Instagram** | No open access since Meta closed CrowdTangle (2024). Meta Content Library is open only to approved researchers and nonprofits | Free if approved | Posts, comment replies | Apply once we have an amuta or a university partner. Do not scrape (against Meta's terms) |
| **TikTok** | Research API, for researchers / nonprofits | Free if approved | Posts, comments | Same as Meta: later, with an amuta |
| **Knesset (official)** | Yes, open data (already used) | Free | Plenum speeches, committee participation, parliamentary questions, motions | Already on the scoreboard; add committee attendance from protocols |
| **Blocking and deleted comments** | Reported: MKs must report to the Ethics Committee every user they block or comment they delete ([Israel Hayom](https://www.israelhayom.co.il/tech/tech-news/article/18511298)) | Free if published; otherwise an FOI request to the Knesset | How many citizens each MK blocked | Strong "listening to the public" signal. Check whether the reports are public; if not, request them |

## Accounts

[contacts/social-accounts.md](../contacts/social-accounts.md): 67 of 120 MKs have at least one account in Wikidata (X 49, Facebook 62, Instagram 36, Telegram 15, YouTube 17, TikTok 17 among the 87 matched). The other 53 (mostly new MKs) need a one-time manual lookup from their Knesset page.

## Proposed "talks with the public" score (per MK, per month)

1. Replies to ordinary users on X (excluding MKs, ministers, verified journalists and news outlets).
2. Replies to comments on their own YouTube videos.
3. Our letters: answered or not.
4. Citizens blocked (from Ethics Committee reports, once available).

Shown as separate columns, not one combined number, so nobody has to trust our weights.

## Rules

- Only the MK's own public accounts and their own public posts. We do not store the names or posts of the citizens they reply to; we keep counts only.
- Each account must be the MK's verified official one; personal or family accounts are excluded.
- Same sampling window for all MKs.
- Comparisons between parties are not published; per-MK only, alphabetical, like the rest of the site.

## Already published by others

SCOOPER (a commercial media-monitoring company) analysed MKs on X in early 2026: Merav Cohen was the most active and Netanyahu got the most interaction ([Maariv](https://www.maariv.co.il/news/politics/article-1278267)). No published method, and it counts reach, not answers to the public.

## Decisions for Tal

- X budget: about $40/month (one sample week) or about $180/month (everything).
- Whether to request the Ethics Committee blocking reports (FOI).
