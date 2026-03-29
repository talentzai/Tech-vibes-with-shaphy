# COWORK MODE — YouTube Research Engine

## Environment
This is Cowork. YouTube API search is NOT available here.
Do not attempt searchVideos. Direct user to Claude Code for that.

## Cowork handles
- Single video transcript + summary + .md + PDF
- Slack messages
- Gmail drafts (not sending)

## Workflow
1. get_video_info → derive friendly slug from video title
2. get_transcript (no timestamps, response-limit 15000)
3. Write summary using Summary Format below
4. Save to summaries/[slug]-summary.md
5. python3 generate_pdf.py summaries/[slug]-summary.md pdfs/[slug]-summary.pdf
6. Confirm both files exist
7. ASK: send to Slack?
8. ASK: need similar videos? Tell user:
   "Open Terminal and run: cd ~/research/youtube-engine && claude
    Then type: find similar videos for [slug]-summary.md"

## Summary format
# [Video title]
**Channel:** [name] | **Published:** [date] | **URL:** [full URL]

## Core argument
[2–3 sentences — the single central claim]

## 5 key insights
- [Insight 1]
- [Insight 2]
- [Insight 3]
- [Insight 4]
- [Insight 5]

## Evidence used
[Named sources, data points, examples from the video]

## Gaps and limitations
[What the video doesn't cover or overstates]

## SMB / AI workflow relevance
[1–2 sentences connecting to your research context]

## Hard stops
- Transcript tool error → stop and report
- File write fails → report immediately
- No captions available → report and stop
- Never attempt YouTube API search — not available in Cowork
- Gmail: create draft only, never attempt to send
