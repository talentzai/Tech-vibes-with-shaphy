# Email Extraction Prompt
**SOP Generator — Input Processing**
**Add this file to: Claude Project > Knowledge files**
**Use when: Source material is an email thread**

---

## WHEN TO USE THIS FILE

Use this extraction approach when the knowledge source is:
- An email from a departing employee to their successor
- A "here is how things work" reply to a knowledge capture request
- A chain of replies documenting how a process has evolved
- A response to "can you write down how you do X?" that came back as an email

Do not use for:
- Auto-generated system notifications
- Vendor proposal or support emails
- Meeting invites or scheduling threads

---

## HOW TO USE

1. Copy the full email thread body text (all replies)
2. Open this Claude Project and start a new conversation
3. Type: `Use the email extraction approach` then paste the prompt below
4. Paste the email content after the divider line
5. Send and receive the structured extraction output
6. Review, scrub names and credentials, then ask: `Now convert this into a formal SOP`

---

## THE PROMPT — paste this into chat, then add email content below

```
ROLE: You are an IT documentation specialist for a Texas city government.

CONTEXT: The following is an email or email thread containing informal knowledge transfer from an experienced employee.

TASK — complete two passes in sequence:

PASS 1 — EXTRACT
Filter out everything that is not procedural knowledge. Discard:
  - Greetings, sign-offs, pleasantries
  - Scheduling ("let us meet Thursday")
  - Opinions not tied to a specific process step
  - Email headers (From / To / CC / Subject / Date)

Keep only:
  - Actions (what to do)
  - Sequence (in what order)
  - Tools, systems, logins, or approvals needed
  - Exceptions and edge cases
  - Known failure modes and workarounds
  - Names of related documents or policies

PASS 2 — STRUCTURE
Organize the extracted content into this format exactly:

PROCESS NAME: [your best inference]
PROCESS OWNER ROLE: [role title, not a person name]
TRIGGER / WHEN: [what event starts this process]
FREQUENCY: [how often — daily, weekly, on-demand]

PREREQUISITES:
- [access, tool, or condition needed before starting]

STEPS:
1. [first action]
2. [second action]
[continue for all steps]

DECISION POINTS:
- IF [condition]: [action]

KNOWN ISSUES / WARNINGS:
- [anything flagged as a common mistake or exception]

GAPS:
- [anything implied but not explicitly stated]

RULES:
- Replace all personal names with role titles: "Call Maria" becomes "Contact [Network Admin]"
- Replace all email addresses with [EMAIL: role description]
- Replace all system URLs, server names, IP addresses with [SYSTEM: name] or [IP_ADDRESS]
- Flag implied steps with [IMPLIED: description]
- If multiple distinct processes appear, separate them with a clear header
- Do not add steps not present in the email — flag gaps instead

EMAIL CONTENT:
[paste full email thread below this line]
```

---

## AFTER EXTRACTION

Once you receive the structured output:

1. Review each [IMPLIED] flag — clarify with the email author or accept the best-guess interpretation
2. Confirm the PROCESS NAME is accurate
3. Check that no real names or credentials remain
4. Review all GAPS — decide which need follow-up before generating the SOP
5. Then ask: `Now convert this extracted content into a formal SOP following your standard format`

---

## QUALITY CHECKLIST

A good extraction will have:
- [ ] A clearly named process
- [ ] Steps that are specific and single-action
- [ ] At least one item in the GAPS section (almost every email leaves something out)
- [ ] No real names in the output

A poor extraction will have:
- [ ] Vague steps like "do the usual thing"
- [ ] An empty GAPS section (flag this — it likely means the AI missed implied knowledge)
- [ ] Steps that are actually two actions combined with "and"

---

*Email Extraction Prompt v1.0 | SOP Generator | TAGITM 2026*
