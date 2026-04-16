# Transcript Cleaning Prompt
**SOP Generator — Input Processing**
**Add this file to: Claude Project > Knowledge files**
**Use when: Source material is a Zoom, Teams, or audio recording transcript**

---

## WHEN TO USE THIS FILE

Use this extraction approach when the knowledge source is:
- A Zoom auto-generated transcript (.txt or .vtt file)
- A Microsoft Teams meeting transcript or recap download
- An Otter.ai, Whisper, or similar auto-transcription service output
- A manually typed transcription of an audio recording

Do not use for:
- Meeting minutes that were already cleaned up by a human note-taker
- Written summaries of a meeting (use rough notes input instead)
- Agendas or pre-written talking points

---

## HOW TO GET THE TRANSCRIPT

**Zoom (Cloud Recording required):**
1. Go to zoom.us > Recordings > find the meeting
2. Click the meeting name > Audio Transcript tab
3. Download as .txt — includes timestamps and speaker labels

**Microsoft Teams:**
1. Open the meeting in the Teams calendar
2. Click the Transcript tab in the meeting details panel
3. Download as .docx or copy all text

**No transcript available:**
Upload the audio file (.mp3, .m4a, .wav) directly to Claude — it will transcribe the audio first.
Alternative: use Whisper (free, open source) or Otter.ai (free tier) to generate the transcript, then paste it here.

**Best practice:** Schedule a deliberate 20-minute verbal knowledge capture session focused on one process, rather than trying to extract procedure knowledge from a general team meeting recording. The focused session produces cleaner output.

---

## HOW TO USE

1. Get the transcript text using one of the methods above
2. Open this Claude Project and start a new conversation
3. Type: `Use the transcript cleaning approach` then paste the prompt below
4. Paste the full raw transcript after the divider line
5. Send and receive the cleaned and structured output
6. Review all [CONFLICT] and [INCOMPLETE] flags with the SME
7. Scrub remaining names and credentials
8. Then ask: `Now convert this extracted content into a formal SOP`

---

## THE PROMPT — paste this into chat, then add transcript below

```
ROLE: You are an IT documentation specialist processing a raw Zoom or Teams transcript to extract operational process knowledge.

CONTEXT: The following is an auto-generated transcript from a knowledge transfer session between an experienced employee and a staff member learning the process. The transcript is raw — it includes timestamps, speaker labels, filler words, and off-topic conversation.

TASK — complete two passes in sequence:

PASS 1 — CLEAN
Remove the following completely:
  Filler words: um, uh, like, you know, sort of, kind of, basically, literally, 
                honestly, right?, okay so, I mean, you see what I'm saying
  False starts: keep only the corrected version when a speaker restarts a sentence
  Small talk: greetings, weather comments, scheduling, anything unrelated to the process
  Technical difficulties: "can you hear me", "you're on mute", "my video is off", 
                          "I think you're breaking up", connection issues
  Repetitions: where a speaker repeats the same information without adding anything new
  Speaker labels and timestamps: remove them, keep only the content
  Filler acknowledgments: "yeah", "mm-hmm", "got it", "sure", "absolutely" 
                          when used only to signal listening, not to add content

Keep everything else:
  All procedural content (what to do, in what order, what tools to use)
  Questions that reveal knowledge gaps or edge cases
  The corrected version of self-corrections
  Explicit warnings about common mistakes
  References to systems, tools, forms, approvals, contacts, or policies

PASS 2 — EXTRACT AND STRUCTURE
From the cleaned content, identify the primary process being discussed.
Organize into this format exactly:

PROCESS NAME: [your best inference from the conversation]
PROCESS OWNER ROLE: [role of the person sharing the knowledge]
TRIGGER / WHEN: [what event starts this process]
FREQUENCY: [how often — daily, weekly, on-demand, annually]

PREREQUISITES:
- [access, system, or condition needed before starting]

STEPS:
1. [first action — specific, single, actionable]
2. [second action]
[continue for all steps extracted from the conversation]

DECISION POINTS:
- IF [condition]: [action taken]
- IF NOT [condition]: [alternative action]

WARNINGS (common mistakes the speaker mentioned):
- [specific warning — preserve the intent exactly]

VENDOR / CONTACT REFERENCES:
- [any external contacts, vendors, or escalation points mentioned]

GAPS:
- [CONFLICT: description] — two speakers gave contradictory information about this
- [INCOMPLETE: description] — this step was started but not fully explained
- [ASSUMED: description] — this knowledge was clearly assumed but never stated

RULES:
  - When two speakers discuss the same step, synthesize into one clear instruction
  - Use the correction, not the original, when a speaker corrects themselves
  - Replace all personal names with role titles throughout
  - Replace all system credentials, URLs, and server names with placeholders
  - If the transcript covers more than one distinct process, separate them with headers
  - Do not add steps not present in the transcript — use GAPS to flag what is missing
  - Preserve the intent of explicit warnings even if the phrasing was informal

TRANSCRIPT:
[paste full raw transcript below this line]
```

---

## AFTER CLEANING

Once you receive the structured output:

1. Review every [CONFLICT] — ask the SME which version is correct before proceeding to SOP generation
2. Review every [INCOMPLETE] — schedule a follow-up with the speaker to finish explaining the step
3. Note: audio-to-SOP typically produces more [VERIFY] flags than other input types — budget 30 minutes for SME review
4. Scrub any remaining names, phone numbers, or internal system references
5. Then ask: `Now convert this extracted content into a formal SOP following your standard format`

---

## QUALITY CHECKLIST

A good cleaning output will have:
- [ ] Steps written as clean instructions: "Disable the Active Directory account" not "so you go in and do the AD thing"
- [ ] At least one item in the GAPS section
- [ ] [CONFLICT] flags wherever two speakers disagreed
- [ ] No speaker names or personal identifiers remaining

A poor cleaning output will have:
- [ ] Steps that quote the speaker: "so what you do is you go into the..."
- [ ] An empty GAPS section
- [ ] Speaker names still present in the content
- [ ] Filler words still present in the step descriptions

---

*Transcript Cleaning Prompt v1.0 | SOP Generator | TAGITM 2026*
