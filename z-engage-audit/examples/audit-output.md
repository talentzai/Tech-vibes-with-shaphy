# Example Mode 4 output — Audit Report

This example shows the output format for Mode 4. Audit of a hypothetical 87-conversation batch.

---

## Input

**Scope:** Engineering archetype campaigns, April 2026, 87 conversations across 6 roles.

**Data provided by user:** Conversation transcripts, outbound and inbound logs, outcome states, timestamps.

---

## Output

# Audit Report

**Audit ID:** audit_eng_2026_04
**Scope:** April 1 to April 30, 2026
**Conversations audited:** 87
**Roles covered:** 6 engineering roles (3 backend, 2 ML, 1 DevOps)
**Generated:** 2026-05-15

---

## Metric panel

| Metric | Value | Benchmark (engineering archetype) | Delta |
|---|---|---|---|
| Response rate (72h) | 4.1% | 6 to 10% | -2 to -6 points (below band) |
| Screening completion | 18% | 55 to 70% | -37 to -52 points (critical) |
| Qualified routing | 62% | 60 to 75% | Within band |
| Post-handoff acceptance | 71% | 75 to 85% | -4 to -14 points (below band) |
| Time-to-first-substantive-reply (median) | 14 hours | <8 hours | +6 hours (above target) |
| Drop-off at interest-to-screening | 73% | 30 to 45% | Critical |

**Assessment:** Response rate is below benchmark; the bigger issue is interest-to-screening drop-off at 73%, which is 28 to 43 points worse than benchmark. The funnel breaks between candidate interest and screening completion.

---

## Findings

### Finding 1 — Question repetition (Pattern A1)

- **Severity:** Critical
- **Category:** Runtime
- **Frequency:** 12 of 87 conversations (14%)
- **Evidence:**
  - conv_001, messages 4 and 7: Agent asks "Have you led HLD/LLD for IP/MPLS edge or BNG/BRAS deployments?" Candidate answers in message 5 with 17 years experience. Agent re-asks identical question in message 7.
  - conv_023, messages 3 and 6: Same pattern.
  - conv_055, messages 5 and 9: Same pattern.
  - [9 more conversations with same signature]

- **Recommendation:** Add state reconciliation step before generating any agent reply. Mark answered questions complete in conversational state. If all screening questions answered, route to human recruiter; do not ask additional questions.

- **Proposed KB change:** New rule rule_22_v2. Statement: "Before generating reply to inbound, reconcile state against screening checklist. Answered questions are marked complete and never re-asked."

---

### Finding 2 — Mis-parsed inbound (Pattern A2)

- **Severity:** Critical
- **Category:** Runtime
- **Frequency:** 8 of 87 conversations (9%)
- **Evidence:**
  - conv_034, message 4: Candidate replies "My preference would be hybrid, but I am flexible. I have both SPHR and SHRM-SCP certifications. I have more than 15 years of progressively responsible HR experience." Agent reply in message 5: "So sorry, I need your responses to the questions above."
  - conv_071, messages 3 and 4: Same signature.
  - [6 more with similar pattern]

- **Recommendation:** Deploy hybrid intent classifier with confidence-gated routing. If classifier confidence is below threshold, ask one clarifying question rather than treating as unanswered. Improve threaded reply parsing to extract inline replies even when candidates do not strip quoted text.

- **Proposed KB change:** New rule rule_23. Statement: "When intent classification confidence is below 0.7, ask one short clarifying question. Do not assume the candidate has not responded."

---

### Finding 3 — Drop-off at interest-to-screening stage

- **Severity:** Critical
- **Category:** Strategy
- **Frequency:** 73% of conversations that reached interest never completed screening
- **Evidence:** Of 24 candidates who replied affirmatively, only 6 completed all screening questions. Average time gap between affirmative reply and first screening question: 6 hours. Average screening question count: 5.
- **Hypothesis:** The 6-hour gap allows interest to decay. Five questions may exceed completion tolerance.
- **Recommendation:**
  1. Reduce screening-question latency to under 5 minutes from affirmative reply (MIT lead-response study: 21x lift inside 5-minute window).
  2. Cap screening at 3 to 4 questions for engineering archetype; consolidate where possible.
  3. Pilot a "split screening" option: candidates can answer 2 now and 2 later by SMS.
- **Proposed KB change:** Modified rule_15. From: "Send screening questions within 1 hour of affirmative reply." To: "Send screening questions within 5 minutes of affirmative reply." Cap engineering screening at 4 questions.

---

### Finding 4 — File-format friction (Pattern A3)

- **Severity:** High
- **Category:** Content (system message exposure)
- **Frequency:** 3 of 87 conversations (3%)
- **Evidence:**
  - conv_018, message 5: System-voiced rejection: "Resume attachment rejected: Resume must be PDF, DOC, or DOCX. Received: .gif. Please send a PDF, DOC, or DOCX file under 10MB." Breaks conversational flow.
- **Recommendation:** Replace system-message error envelopes with agent-voiced equivalents. Sample replacement: "Thanks for sending that. Our system needs a PDF or DOCX. Want to send a link instead, or skip the resume for now?"
- **Proposed KB change:** New rule rule_24. Statement: "All file-format and system-error messages are wrapped in agent voice. System-voiced messages never appear in candidate-facing threads."

---

### Finding 5 — Identity-line absence (Pattern A5)

- **Severity:** Medium
- **Category:** Content
- **Frequency:** 6 of 87 conversations (7%)
- **Evidence:** 6 touch-1 messages start with "I'm Zee, an AI Hiring Assistant from Pricesenz" without the "working with our recruiting team" framing required by policy. Pattern correlates with -45% response rate vs. compliant outreach.
- **Recommendation:** Enforce identity-line template at content-generation step. Reject output that does not match.

---

## Patterns clustering (severity x category)

| | Strategy | Personalization | Content | Runtime |
|---|---|---|---|---|
| **Critical** | Finding 3 | — | — | Findings 1, 2 |
| **High** | — | — | Finding 4 | — |
| **Medium** | — | — | Finding 5 | — |

---

## Proposed KB changes (for Mode 5)

| Diff type | Rule ID | Domain | Statement |
|---|---|---|---|
| New rule | rule_22_v2 | Conversational state | State reconciliation before reply generation |
| New rule | rule_23 | Intent classification | Confidence-gated clarification |
| Modified | rule_15 | Screening flow | Screening questions sent within 5 minutes |
| New rule | rule_24 | Content | System errors wrapped in agent voice |

---

## What to do next

1. Surface Findings 1, 2, and 3 to product immediately. These are critical and recurring.
2. Run Mode 5 (Feedback Loop Enrichment) on these audit findings plus any others from the same period.
3. Roll the KB updates into production ZeeEngage. Begin with Findings 1 and 2 (runtime fixes); Finding 3 (strategy change) requires broader review.
4. Re-audit at 30-day window after deployment to confirm impact.

---

## What I could not audit

- Cause of the 14-hour median time-to-first-substantive-reply. Could be candidate-side (candidates take longer to respond) or agent-side (delayed processing). Needs further data on agent-side latency.
- Post-handoff acceptance gap of 4 to 14 points. Could indicate ZeeEngage is routing weak fits to recruiters. Recommend a recruiter-feedback audit on a sample of rejected routings.
