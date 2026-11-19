# Public Outreach

Citizens writing to Members of Knesset and senior officials about issues that bother the public, and publishing who answers.

Everything here is plain Markdown, generated from official public data or from letters we actually sent.

## What is here

| Folder / file | What |
|---|---|
| `scorecard/members.md` | Every current MK: legislative activity in the previous Knesset (official data) and how they answered our letters |
| `scorecard/ministries.md` | How many parliamentary questions each ministry answered, and how late |
| `scorecard/PUBLIC_SOURCES.md` | What Israel already publishes on MK activity, and the only past email-reply tests (2005, 2007) |
| `scorecard/METHODOLOGY.md` | Exactly how every number is computed, and its limits |
| `issues/` | One file per issue: facts, sources, the concrete asks |
| `letters/` | Every letter sent, exact text, with date / status / reply date in the front matter |
| `contacts/` | Generated list of MKs and committees with official emails |
| `log.md` | One line per event |
| `deadlines.md` | Follow-ups and legal deadlines due |
| `OPTIONS.md` | The strategy research behind this project |

## Rebuild the data

```
py scripts/sync_knesset.py
py scripts/scorecard.py
```

## Principles

- Same standard for every MK and every party. No ranking by opinion, only by recorded facts.
- Every number is reproducible from a public source.
- A letter counts in the reply rate only if it was a real, individual, non-identical letter with a clear question.
- Corrections welcome: open an issue.
