# Example Mode 6 output — Validation Report

This example shows the output format for Mode 6 (message validation). The recruiter provides a draft message and asks the skill to validate it against the playbook. The skill produces a structured report with pass/fail status, evidence for each failed check, and a suggested rewrite.

---

## Input

**Draft message (provided by recruiter):**

```
Subject: Exciting Opportunity at our cutting-edge company!

Hi Sofia,

I noticed your impressive background at Stripe and wanted to reach
out about an exciting opportunity for a senior backend engineer
position at our innovative payments platform. Our team is doing
groundbreaking work and we'd love to chat with you about how you
might leverage your skills to drive impact.

Feel free to reach out if you're interested or want to learn more
about this exciting opportunity!

Best regards,
The Recruiting Team
```

**Channel:** Email
**Touch number:** 1
**Role archetype:** Engineering
**Role title (for context):** Senior Backend Engineer

---

## Output

# Validation Report

**Verdict:** Reject. Revise before sending.

**Summary:** 4 of 11 checks passed. 7 failures across content, banned phrases, structure, and signoff.

---

## Per-check results

| Check | Status | Evidence |
|---|---|---|
| Length (within band) | Pass | 87 words (within 75 to 140 range for touch 1 email) |
| Identity line present | **Fail** | No human-backed identity. Required: "I'm Zee, an AI assistant working with [Company]'s recruiting team on [Role]." |
| No banned phrases | **Fail (multiple)** | See banned phrase detail below |
| Single CTA | **Fail** | Two CTAs: "reply if interested" and "learn more about this exciting opportunity" |
| Timeline anchor | **Fail** | No concrete timeline or scope fact. Engineering archetype touch 1 requires one. |
| Persona line | **Fail** | No "Best fit:" line scoping the ideal candidate |
| Approved signoff | **Fail** | "Best regards, The Recruiting Team" does not match policy. Required: "— Zee, supporting the [Company] recruiting team" |
| Subject line rules | **Fail** | Contains banned word ("cutting-edge"), exclamation point (banned), and starts with marketing phrase |
| Title matches context | Pass | "senior backend engineer" matches provided role title |
| Compliance disclosure | Pass | (US-based assumed; no EU disclosure needed) |
| No opt-out in touch 1 | Pass | No opt-out language present |

## Banned phrase detail

Seven banned phrases or patterns detected:

1. "exciting opportunity" (3 occurrences) — banned, marketing filler
2. "cutting-edge" (subject line) — banned, marketing filler
3. "innovative" — banned, replace with specific descriptor
4. "I noticed your impressive background" — banned, fake personalization (recruiter has no verified candidate data context)
5. "leverage your skills" — banned, replace "leverage" with "use"
6. "groundbreaking" — banned, marketing filler
7. "feel free to reach out" — banned, weak CTA pattern

## Suggested rewrite

```
Subject: Senior Backend Engineer, payments infrastructure

Hi Sofia,

I'm Zee, an AI assistant working with [Company]'s recruiting team
on a Senior Backend Engineer role focused on Go and AWS-based
payments infrastructure.

The team is shipping a multi-region payments rewrite this quarter,
so the next hire owns the throughput layer design. Stack is Go,
AWS, Postgres, and Kafka.

Best fit: engineers with prior production payments experience.

Would you like to go through a few quick questions to assess fit?

— Zee, supporting the [Company] recruiting team
```

**Rewrite word count:** 98 words (within band).

## What changed and why

1. **Subject line.** Removed exclamation, "cutting-edge", and marketing framing. Used JD-derived title plus one scope fact. Under 50 characters.
2. **Identity line added.** Human-backed identity required per policy in touch 1.
3. **Fake personalization removed.** "I noticed your impressive background" assumes verified candidate data not present in the draft context. Replaced with role specificity.
4. **Timeline anchor added.** "multi-region payments rewrite this quarter" satisfies the engineering archetype requirement.
5. **Persona line added.** "Best fit: engineers with prior production payments experience" scopes the ideal candidate.
6. **Banned phrases removed.** All seven banned phrases stripped. Replaced where needed with specific descriptors.
7. **Single CTA.** Two CTAs collapsed to one: "Would you like to go through a few quick questions to assess fit?"
8. **Signoff fixed.** "— Zee, supporting the [Company] recruiting team" replaces "Best regards, The Recruiting Team."

## Final assessment

The original message would underperform benchmark and damage trust. Common failure pattern combination observed here: marketing-language overload plus fake personalization plus weak CTA. This pattern correlates with -40% response rate in engineering cohorts versus compliant outreach.

Use the suggested rewrite, or revise to address each failed check above.

---

## Storage

This validation report is ephemeral by default. The recruiter can request to save it.

**Suggested filename if saved:** `validations/2026-05-15_sofia-m-touch1-email.md`
