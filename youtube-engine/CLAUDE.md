# CLAUDE CODE MODE — YouTube Research Engine

## Environment
This is Claude Code. YouTube API search IS available here.
YouTube search, Gmail sending, and multi-video processing
are all fully enabled in this environment.

## Claude Code handles
- YouTube similar video search via searchVideos
- Multi-video transcript + summary + PDF processing
- Comparative report generation
- Gmail sending (not just drafts)
- Slack messages

## Workflow

### Find similar videos
1. User specifies a summary file e.g. "find similar videos for [slug]-summary.md"
2. Read that file → extract topic from Core argument section
3. ASK: "Searching YouTube costs 100 API units. Proceed?"
4. Call searchVideos — use topic, maxResults=5, order=relevance
5. Show shortlist:
   1. [Title] — [Channel] — [views] views
      https://youtube.com/watch?v=[id]
6. STOP — wait for user to select videos

### Process selected videos
For each selected video:
1. Derive friendly slug from title (lowercase, hyphens, 3-6 words)
2. get_video_info → get_transcript (no timestamps)
3. Write summary using Summary Format below
4. Save to summaries/[slug]-summary.md
5. python3 generate_pdf.py summaries/[slug]-summary.md pdfs/[slug]-summary.pdf
6. Confirm file saved before moving to next video

### Consolidated report
1. Read all summaries from this session
2. Write comparative analysis using Comparison Format below
3. Save to comparisons/[topic-slug]-comparison.md
4. python3 generate_pdf.py comparisons/[slug].md pdfs/[slug]-comparison.pdf

### Send via Gmail
1. Ask for recipient email address
2. Show full draft — subject + body
3. Wait for explicit confirmation
4. Send

## API cost tracking — show at session end always
---
Session API usage
searchVideos calls: [n]
Units used: [n x 100]
Units remaining today: [10000 - used]
Files created: [list all .md and .pdf paths]
---

## Summary format
# [Video title]
**Channel:** [name] | **Published:** [date] | **URL:** [full URL]

## Core argument
[2–3 sentences]

## 5 key insights
- [Insight 1]
- [Insight 2]
- [Insight 3]
- [Insight 4]
- [Insight 5]

## Evidence used
[Named sources, data points, examples]

## Gaps and limitations
[What the video doesn't cover]

## SMB / AI workflow relevance
[1–2 sentences]

## Comparison format
# Comparative analysis: [Topic]
**Videos analysed:** [n] | **Date:** [YYYY-MM-DD]

## Topic overview
[2–3 sentences on the landscape]

## Per-video summaries
[Summary Format repeated for each video]

## Comparative matrix
| Dimension        | Video 1 | Video 2 | Video 3 |
|------------------|---------|---------|---------|
| Core angle       |         |         |         |
| Evidence quality |         |         |         |
| Target audience  |         |         |         |
| Unique insight   |         |         |         |
| Verdict          |         |         |         |

## Synthesis
[What the combined view reveals that no single video covers]

## Hard stops
- Never call searchVideos without explicit user approval
- Never send Gmail without showing draft and getting confirmation
- Transcript tool error → stop and report
- File write fails → report immediately
