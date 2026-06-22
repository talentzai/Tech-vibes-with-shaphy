# Cadence and timing

ZeeEngage uses the 3-7-7 cadence with three behavior-triggered overlays. The cadence is defensible at the scaffold level; the behavior triggers add adaptive response without breaking the structure.

---

## Default cadence: 3-7-7

| Touch | Day | Purpose | Channel |
|---|---|---|---|
| 1 | 1 | Primary outreach | Email (or per-archetype default) |
| 2 | 3 | First follow-up; new angle | Channel switch (LinkedIn or SMS) |
| 3 | 10 | Second follow-up; reframe | Email |
| 4 | 17 | Breakup; pattern-interrupt close | Email or LinkedIn |

**Why this works.** Digital Bloom 2025 analysis confirms 3-7-7 captures roughly 93% of total replies by day 10. Gem 2024 and 2025 data shows replies flatten after stage four to five; additional touches add cost without adding interested replies.

**Spacing logic.**
- Day 1 to Day 3 is short because candidates who are interested but busy need a prompt before the initial message fades.
- Day 3 to Day 10 widens to avoid harassment perception.
- Day 10 to Day 17 widens again. The breakup itself counterintuitively produces some of the highest reply rates.

---

## Behavior triggers (apply within the cadence)

These overlays react to candidate behavior in real time. They do not replace the cadence; they accelerate or pause it.

### Trigger 1 — Open twice without reply

**Condition.** Candidate opens the same message twice within 24 hours and does not reply.

**Action.** Advance the next scheduled touch by 24 hours and switch channel.

**Rationale.** Two opens without a reply signal interest plus friction. The reader is considering but has not crossed the threshold. A channel switch and a faster follow-up reduce decision friction.

### Trigger 2 — Click without reply

**Condition.** Candidate clicks any link in the outreach (calendar, profile, JD) but does not reply within four hours.

**Action.** Send a one-line acknowledgment within four hours of the click.

**Example acknowledgment (email).**
```
Saw you opened the role detail. Want to do a quick fit check?

— Zee
```

**Rationale.** Click-without-reply is high-intent. The acknowledgment is a low-friction nudge that does not assume a yes.

### Trigger 3 — Partial reply

**Condition.** Candidate sends any inbound message (even one word, even an out-of-office) before the next scheduled touch.

**Action.** Suspend the scheduled cadence immediately. Enter conversational mode. Classify the inbound intent and respond.

**Rationale.** Sending the next scheduled touch after a candidate replies is the primary cause of the "ZeeEngage asked the same question twice" failure mode observed in production. The fix is structural: never send a scheduled touch when state shows an unhandled inbound.

**Mandatory state reconciliation.** Before generating any reply to an inbound message:
1. Read the conversation history.
2. Identify which screening questions have been answered.
3. Mark answered questions complete in conversational state.
4. Generate the next response based on remaining unanswered questions.

If state reconciliation reveals all screening questions are answered, route to the human recruiter immediately. Do not ask additional questions.

---

## Send-time defaults

Apply to all touches unless overridden by a behavior trigger or candidate-specific signal.

| Channel | Best send window | Backup window |
|---|---|---|
| Email (general) | Tuesday 9am to 11am local | Wednesday or Thursday 9am to 11am |
| Email (senior leadership) | Tuesday 9am OR Sunday 2pm local | Wednesday 9am |
| LinkedIn InMail | Tuesday 11am OR Wednesday 11am local | Thursday 11am |
| SMS | Wednesday 11am to 2pm local | Thursday 11am to 2pm |
| Slack | Tuesday or Wednesday 9am to 11am local | Thursday 9am |

**Notes.**

- "Local" means the candidate's timezone, not the sender's.
- Mondays and Fridays consistently underperform across 2025 to 2026 vendor data for B2B recruiting outreach.
- Sunday 2pm has shown strong engagement for passive senior leadership (Gem 2025), likely because senior candidates clear inboxes on weekend afternoons. Use selectively.
- Send-time variance is small (~5 to 8% of total reply-rate variance per Aurium 2026); do not over-optimize. Hook quality and channel mix matter more.

---

## Alternative cadences (use only with explicit reason)

| Cadence | When to use | Caveat |
|---|---|---|
| 2-5-12 (front-loaded) | High-urgency roles where speed matters more than candidate experience | Unstudied at scale; equivalent reply totals to 3-7-7 in informal data |
| 1-4-9-16 (longer decay) | Passive senior leadership campaigns | Effectively equivalent to 3-7-7 |
| 5-touch or 7-touch | Almost never; specific to staffing redeploy pools | Gem 2025 shows no reply lift past stage four |
| Single-touch | Never | 70% of cold campaigns stop after one message; 55% of replies arrive on follow-ups |

The default is 3-7-7. Deviate only with a documented reason.

---

## Stop conditions

ZeeEngage must immediately stop the cadence when:

- Candidate replies positively (route to human within 15 minutes business hours, 4 hours overnight).
- Candidate opts out (suppress from all future ZeeEngage campaigns for that company; permanent).
- Candidate explicitly declines ("not interested", "remove me", "stop").
- Candidate has not opened any of four touches and is in a Tier 0 pool (consider re-enrolling in a different campaign after 90-day gap).

---

## Cadence compliance with regulations

- **EU AI Act**: Disclosure of AI involvement is required at first contact. The identity line in touch 1 satisfies this. Subsequent touches must maintain the same identity framing.
- **GDPR Article 22**: Candidates must have the right to contest automated decisions. ZeeEngage does not make hiring decisions, so this applies only at the routing step; document the decision in audit trail.
- **NYC Local Law 144**: Bias audits and pre-use notification apply to AEDT (automated employment decision tools). ZeeEngage's outreach and screening do not constitute AEDT use; the assessment phase (ZeeLens) does. Document the boundary in the audit trail.
- **CAN-SPAM and CASL** (US and Canada email): Honor opt-outs within 10 business days; one-click unsubscribe required.
- **TCPA** (US SMS): Explicit opt-in required for marketing SMS. Recruiting SMS to candidates whose phone numbers were provided in a contact list typically qualifies as transactional; include opt-out language regardless.

See references/compliance.md for full jurisdictional detail.
