# Audit rubric

Mode 4 (engagement audit) uses this rubric. Every finding must cite specific evidence (message indices, transcript excerpts, timestamps). Generic findings are rejected.

---

## Failure pattern catalog

The patterns below recur across ZeeEngage production data. Each has a detection signature, severity tier, and recommended remediation.

---

### Pattern A1 — Question repetition

**Severity.** Critical.

**Detection signature.** Agent asks the same or substantially similar question to the candidate in two separate messages within one conversation, after the candidate has already answered.

**Detection method.**
1. Extract all agent messages from the conversation.
2. Identify which contain screening questions.
3. For each question, check if the candidate answered it in any prior message.
4. Flag if the agent re-asks an already-answered question.

**Evidence template.**
> Conversation [conv_id], messages [N] and [M]. Agent asks "[question]" in message [N]. Candidate answers in message [N+1]: "[answer]". Agent re-asks the same question in message [M].

**Recommended remediation.**
- Add state reconciliation step before generating any agent reply: read conversation history, mark answered questions complete in state, generate next response only from remaining unanswered questions.
- If state reconciliation reveals all questions answered, route to human recruiter immediately.

**Production examples.** Documented in conversation_history.txt (May 13, IP/MPLS engineer thread). Agent asks HLD/LLD question, candidate confirms 17 years experience, agent re-asks same question.

---

### Pattern A2 — Mis-parsed inbound

**Severity.** Critical.

**Detection signature.** Agent treats a candidate reply as unanswered or empty when the candidate clearly responded.

**Detection method.**
1. Identify inbound candidate messages.
2. For each, check the next agent reply.
3. Flag if the agent reply ignores or contradicts the inbound content (e.g., agent says "I need your responses" when candidate already replied).

**Evidence template.**
> Conversation [conv_id], message [N] from candidate: "[content]". Agent reply in message [N+1] says "[contradictory statement]".

**Recommended remediation.**
- Hybrid intent classifier with confidence-gated routing. If classifier confidence is below threshold, ask a short clarifying question rather than acting on misread intent.
- Threaded reply parsing must extract inline replies even when candidates do not strip quoted text.

**Production example.** Documented in conversation_history_2.txt (Nov 12, HR Director thread). Candidate replies with answers; agent responds "So sorry, I need your responses to the questions above."

---

### Pattern A3 — File-format friction

**Severity.** High.

**Detection signature.** System message (not agent-voiced) appears in the conversation thread, typically rejecting an attachment, format, or input.

**Detection method.** Scan for messages tagged as "System" or containing system-level error text ("rejected", "must be PDF", "exceeds size limit") that are not wrapped in agent voice.

**Evidence template.**
> Conversation [conv_id], message [N]. System-voiced rejection: "[content]". Breaks conversational flow.

**Recommended remediation.**
- Replace all system-message error envelopes with agent-voiced equivalents. Example: "Thanks for sending that. Our system needs a PDF or DOCX. Want to send a link instead, or skip the resume for now?"
- File-format errors should never expose system internals to the candidate.

**Production example.** conversation_history.txt, May 13, .gif resume rejection.

---

### Pattern A4 — Garbled handoff summary

**Severity.** High.

**Detection signature.** Handoff summary (when ZeeEngage routes to a human recruiter) is incoherent, contradictory, or contains fabricated detail.

**Detection method.** Compare the handoff summary against the conversation content. Flag if:
- Summary contains facts not present in conversation.
- Summary contradicts candidate statements.
- Summary uses placeholder text ([Candidate name]) instead of resolved values.
- Summary garbles tenure, certifications, or other specifics.

**Evidence template.**
> Conversation [conv_id]. Candidate stated tenure as "15+ years" in message [N]. Handoff summary states "23+ years". Source of discrepancy unclear.

**Recommended remediation.**
- Standardize handoff payload to seven structured fields: candidate identifier, role reference, verified-interest level, conversation summary (max 80 words), structured screening responses, open items, AI-suggested next action.
- Generate summary from structured screening responses, not free-text generation over the full transcript.

**Production example.** conversation_history_2.txt, Nov 12, SenBot summary states "23+ years" when candidate disclosed "15+ years".

---

### Pattern A5 — Identity-line absence

**Severity.** Medium.

**Detection signature.** Touch 1 message does not contain the human-backed identity line.

**Detection method.** Check the first agent message in the conversation for the substring pattern: "I'm Zee, an AI assistant working with [...] recruiting team on [...]".

**Recommended remediation.**
- Enforce the identity-line template at the content-generation step.
- Reject touch 1 output that does not satisfy the template.

---

### Pattern A6 — Banned phrases

**Severity.** Medium.

**Detection signature.** Any banned phrase from references/quality-rules.md appears in agent output.

**Detection method.** Regex match against the banned phrase list.

**Recommended remediation.**
- Pre-send quality check that scans for banned phrases and regenerates if found.

---

### Pattern A7 — Cadence breaks

**Severity.** Medium.

**Detection signature.** Scheduled touch (2, 3, or 4) is missing or significantly delayed.

**Detection method.** For each conversation:
1. Compute expected touch dates based on 3-7-7 from touch 1 timestamp.
2. Check actual touch dates against expected.
3. Flag if any touch is missing (no reply terminated cadence prematurely) or delayed by more than 48 hours.

**Recommended remediation.**
- Audit the scheduling system; cadence breaks usually indicate runtime issues, not strategy issues.
- If cadence breaks correlate with low response rate, prioritize fix.

---

### Pattern A8 — Wrong title

**Severity.** Medium.

**Detection signature.** Outreach message uses a role title that differs from the JD title in a way that changes seniority (Manager vs Director, Senior vs Lead).

**Detection method.** Compare the role title in the agent message against the JD title.

**Recommended remediation.**
- Use JD title verbatim in subject line, identity line, and persona line.

**Production example.** Radisys Sr. Director Supply Chain role was sent as "Sr Supply Chain & Operations Manager" — a full seniority level off.

---

### Pattern A9 — Two CTAs

**Severity.** Low.

**Detection signature.** Touch 1 contains more than one ask. Examples: "Would you like to learn more or schedule a call?" or "Reply with questions or click here to apply."

**Recommended remediation.**
- Enforce single CTA rule at content-generation step.

---

### Pattern A10 — Opt-out in touch 1

**Severity.** Low.

**Detection signature.** Touch 1 contains opt-out language ("You can opt out at any time", "If not interested, let me know").

**Recommended remediation.**
- Reserve opt-out language for touch 2 onward.
- SMS exception: opt-out language is required by TCPA/CASL in every SMS.

---

## Severity tiers and routing

| Severity | Definition | Routing |
|---|---|---|
| Critical | Trust-breaking; recurs in production transcripts | Surface to product immediately; propose KB rule change |
| High | Quality-degrading; affects response or completion rates | Aggregate across batch; propose KB diff in next enrichment |
| Medium | Style or compliance gaps; not trust-breaking | Track frequency; address in batch updates |
| Low | Polish issues | Track but do not surface unless persistent |

---

## Metric panel for batch audits

For every audit batch, compute and compare against archetype benchmarks:

| Metric | Definition | Source |
|---|---|---|
| Response rate (72h) | Replies within 72 hours / total sent | Outbound and inbound logs |
| Screening completion | Completed screenings / interested replies | Conversation state |
| Qualified routing | Routed to recruiter / completed screenings | Routing log |
| Post-handoff acceptance | Routings recruiter advanced / total routed | Recruiter ATS state |
| Time-to-first-substantive-reply | Median minutes, outreach send to first non-trivial reply | Conversation timestamps |
| Drop-off by stage | % lost at outreach, interest, screening, booking | Funnel analytics |

If a metric falls more than 20% below archetype benchmark, treat as critical finding and identify the contributing pattern.

---

## Audit report structure

Every audit report contains:

1. **Scope.** Date range, strategies covered, conversations audited.
2. **Metric panel.** All six metrics with values, benchmarks, deltas.
3. **Findings.** Each finding with severity, category, pattern, evidence references, frequency, recommendation.
4. **KB proposals.** Specific playbook diffs the audit motivates.

See examples/audit-output.md for a worked example.

---

## What not to audit

- Outcomes attributable to candidate behavior (chose competing offer, withdrew for personal reasons).
- Performance differences across roles in different archetypes (compare within archetype only).
- Patterns from a single conversation (require minimum frequency before promoting to a finding).

---

## Aggregation thresholds (multi-conversation audits)

When auditing multiple conversations for the same JD, apply these thresholds to cluster findings by frequency.

| Frequency in batch | Treatment |
|---|---|
| Less than 10% | Note in combined report; do not prioritize for Mode 5 |
| 10 to 29% | Candidate playbook change; recommend Mode 5 review |
| 30% or higher | Critical regardless of original severity tier; surface immediately to product |

**Singleton handling.** Patterns appearing in only one conversation are noted as singletons. They do not promote to playbook changes unless they recur in subsequent audits.

**Ranking rule for combined reports.** Rank patterns by frequency first, then by severity tier within the same frequency band. A 35%-frequency Medium pattern ranks above a 15%-frequency Critical pattern in the surfaced order, because the recurring problem typically has more aggregate impact than the rare-but-severe one.

**Combined report structure.** Output includes:

1. Aggregate metric panel (median, P25, P75 per metric; distribution of outcomes).
2. Ranked pattern table (frequency, pattern code, severity tier, conversations affected).
3. Per-pattern detail with representative evidence from individual reports.
4. References to individual reports for full context.
5. Proposed KB diffs for any pattern at 10%+ frequency.
