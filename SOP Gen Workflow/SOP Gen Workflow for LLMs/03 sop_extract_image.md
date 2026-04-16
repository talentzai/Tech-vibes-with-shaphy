# Image and Handwritten Notes OCR Prompt
**SOP Generator — Input Processing**
**Add this file to: Claude Project > Knowledge files**
**Use when: Source material is a photo, scan, or whiteboard image**

---

## WHEN TO USE THIS FILE

Use this extraction approach when the knowledge source is:
- A phone photo of handwritten notes on a legal pad or notebook
- A scanned page of notes or a printed form with handwritten additions
- A whiteboard photo taken after a knowledge transfer session
- A PDF scan of old paper documentation
- A close-up photo of sticky notes or a notepad

Do not use for:
- Digital text you can copy and paste directly
- Screenshots of software interfaces or system screens
- Charts or org charts (describe what you need instead)

---

## BEFORE YOU UPLOAD — image quality checklist

- [ ] Good lighting — no shadows crossing the text
- [ ] Camera held parallel to the page — no angled or keystoned shots
- [ ] Minimum resolution: 1200 pixels on the short side
- [ ] All page edges in frame — nothing cut off
- [ ] Multiple pages: photograph each page separately and number them
- [ ] Whiteboards: capture before erasing — there is no second chance

---

## HOW TO USE

1. Take or locate the photo or scan
2. Open this Claude Project and start a new conversation
3. Upload the image directly in the chat (drag and drop or use the attachment button)
4. In the same message, paste the full prompt below
5. Send — Claude processes the image and returns structured text
6. Review all [ILLEGIBLE] and [UNCLEAR] flags before proceeding
7. If the output shows `READY FOR SOP GENERATION: No` — resolve the flagged gaps first
8. Then ask: `Now convert this extracted content into a formal SOP`

---

## THE PROMPT — upload image first, then paste this in the same message

```
ROLE: You are an IT documentation specialist reviewing a photographed or scanned document containing handwritten or printed notes.

TASK — complete three passes in sequence:

PASS 1 — TRANSCRIBE
Read every piece of text visible in the image. Reproduce the content exactly as written.
Preserve and note the following:
  - Numbering and bullet structure (keep as-is)
  - Crossed-out text: [CROSSED OUT: original text]
  - Circled or underlined items: [CIRCLED: text] or [UNDERLINED: text]
  - Arrows and connectors: describe as "arrow from [item A] pointing to [item B]"
  - Asterisks or stars: [STARRED: text]
  - Margin notes: [MARGIN NOTE: text]
  - The author's own question marks: preserve exactly

For unreadable text:
  - Completely unreadable: [ILLEGIBLE]
  - Partially readable: [UNCLEAR: your best guess]

Do not interpret or reorganize in Pass 1. Transcribe only.

PASS 2 — ORGANIZE
Group the transcription into these logical sections:

HEADER / TITLE: [any title or label at the top of the page]
DATE (if visible): [date written on notes, if present]

MAIN STEPS / SEQUENCE:
[numbered or bulleted steps]

SIDE NOTES / EXCEPTIONS:
[margin notes, asterisked items, parenthetical additions]

REFERENCE INFORMATION:
[any names, phone numbers, system names, or links written in the notes]

QUESTIONS / FOLLOW-UP ITEMS:
[anything written as a question or marked as TBD or unclear by the original author]

PASS 3 — ASSESS
Provide this assessment at the end:

PROCESS IDENTIFIED: [your best interpretation of what process these notes document]
NOTE AUTHOR ROLE: [inferred from context if possible, otherwise Unknown]
COMPLETENESS: [what appears to be missing or assumed]
LOGICAL GAPS: [steps that seem to be implied but not written down]
READY FOR SOP GENERATION: Yes / No
REASON IF NO: [what must be resolved before SOP generation can proceed]

RULES:
  - Do not add information that is not visible in the image
  - Do not correct spelling errors in Pass 1 — transcribe exactly as written, note errors in Pass 2
  - If the image contains multiple separate documents or sections, label each one clearly
  - Preserve the author's own question marks and uncertainty markers
  - If the image quality is too poor to read reliably, state this clearly and describe what is and is not readable
```

---

## AFTER OCR

Once you receive the structured output:

1. Review every [ILLEGIBLE] — return to the original image or ask the note author
2. Review every [UNCLEAR] — confirm the best guess with the note author before accepting it
3. Verify all arrow descriptions match the actual flow direction in the original notes
4. Check `READY FOR SOP GENERATION` — do not proceed if it says No
5. Scrub any names, credentials, or internal system references that appeared in the notes
6. Then ask: `Now convert this organized content into a formal SOP following your standard format`

---

## QUALITY CHECKLIST

A good OCR output will have:
- [ ] A Pass 1 that closely matches what a human reader would see
- [ ] [ILLEGIBLE] flags only for genuinely unreadable sections
- [ ] A Pass 3 that correctly identifies the process from context clues
- [ ] Arrows described with clear directionality

A poor OCR output will have:
- [ ] A Pass 1 that interprets instead of transcribes
- [ ] Missing crossed-out text or margin notes
- [ ] `READY FOR SOP GENERATION: Yes` when significant gaps clearly exist
- [ ] Arrow descriptions that are vague ("there is an arrow here")

---

*Image OCR Prompt v1.0 | SOP Generator | TAGITM 2026*
