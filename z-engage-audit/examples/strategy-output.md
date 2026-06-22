# Example Mode 1 output — Strategy Artifact

This example shows the output format for Mode 1. Engineering archetype, mid-level role. The artifact opens with YAML frontmatter for orchestrator-side caching and indexing.

---

## Input

**Job description (provided by user):**
> Senior Backend Engineer at PriceSenz. Location: Dallas, TX (hybrid). Stack: Go, AWS, Postgres, Kafka. Owns design of throughput layer in payments infrastructure. Team is in the middle of a multi-region rewrite landing this quarter. 5+ years backend, payments experience preferred. Reports to Director of Engineering. Direct hire role.

---

## Output

```yaml
---
strategy_id: stg_pricesenz_be_2026_05
jd_hash: a3f5b2c8e1d4f9...        # SHA-256 of canonical JD text
archetype: engineering
seniority: senior_ic
account_type: direct_hire
geography: dallas_tx
kb_version_used: kb_2026_05_15
generated_at: 2026-05-15T14:32:00Z
---
```

# Strategy Artifact

**Strategy ID:** stg_pricesenz_be_2026_05 (see YAML frontmatter above for full caching metadata)

---

## Role classification

- **Title:** Senior Backend Engineer
- **Archetype:** Engineering
- **Seniority:** Senior IC
- **Account type:** Direct hire
- **Geography:** Dallas, TX (hybrid)
- **Urgency:** Quarterly milestone (multi-region rewrite shipping this quarter)

---

## High-signal facts extracted from JD

1. **Tech stack.** Go, AWS, Postgres, Kafka.
2. **Domain.** Payments infrastructure with multi-region throughput requirements.
3. **Timeline anchor.** Multi-region payments rewrite shipping this quarter; next hire owns throughput layer design.

---

## Channel sequence

| Touch | Day | Channel | Purpose |
|---|---|---|---|
| 1 | 1 | Email | Stack and domain-specific outreach |
| 2 | 3 | LinkedIn InMail | Second touch; reinforce stack signals |
| 3 | 10 | Email | Technical reframe (e.g., migration off monolith) |
| 4 | 17 | Email | Pattern-interrupt breakup |

## Behavior triggers

| Trigger | Condition | Action |
|---|---|---|
| Open twice no reply | Same message opened 2x in 24h | Advance next touch by 24h; switch channel |
| Click no reply | Any link clicked, no reply in 4h | Send one-line acknowledgment within 4h |
| Partial reply | Any inbound message | Suspend cadence; enter conversational state |

## Send times

- Email: Tuesday 9am local (Dallas: CT)
- LinkedIn InMail: Wednesday 11am local
- Follow-up email: Tuesday or Thursday 9am local

---

## Message structure

**Default:** RSTC (Role-Scope-Timeline-CTA)

**Tone:** Direct, technical, specific. Name the stack and the work. Avoid marketing language.

---

## Screening questions (4)

1. Have you operated Go-based services at production scale (100K+ QPS)?
2. Have you designed for multi-region failover with Postgres and Kafka?
3. Do you have direct experience with payment systems (PCI scope, idempotency, settlement)?
4. Are you open to a hybrid role in Dallas (3 days on-site)?

---

## Compliance flags

- **EU AI Act:** Not applicable (US-based role and candidates assumed).
- **GDPR:** Apply if EU-based candidates appear in contact list.
- **NYC Local Law 144:** Not applicable (Dallas-based).
- **TCPA:** Apply for SMS touches; include opt-out language.

---

## Quality gates passed

- [x] All four channel touches present
- [x] Timeline anchor available in JD
- [x] Compliance flags resolved
- [x] Screening questions check must-haves only
- [x] Archetype benchmarks loaded (response rate target: 6 to 10%)

---

## Next steps

1. Recruiter reviews and approves strategy.
2. Mode 2 runs per candidate for personalization (Tier 0 or Tier 1 depending on enrichment availability).
3. Mode 3 generates message variants per touch and channel.
4. ZeeEngage runtime consumes the strategy and executes.
5. Mode 4 audits after 30-day rolling window.
