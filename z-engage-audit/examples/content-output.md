# Example Mode 3 output — Multi-channel content

This example shows the output format for Mode 3. Engineering archetype, Tier 1 candidate, email touch 1.

**Default behavior.** Mode 3 generates only the Balanced variant unless additional variants are explicitly requested. The recruiter can ask for Compact or Executive at any time. The all-variants example is at the bottom of this file for reference.

---

## Default request — Balanced variant only

### Input

**Strategy reference:** stg_pricesenz_be_2026_05
**Candidate plan reference:** plan_sofia_m_2026_05_15
**Channel:** Email
**Touch number:** 1
**Variants requested:** (not specified, defaults to Balanced only)

### Output

**Variant:** Balanced
**Suggested filename:** `02_messages/touch1_email_balanced.md`

**Subject:** Senior Backend Engineer, payments infrastructure

**Body (98 words):**

```
Hi Sofia,

I'm Zee, an AI assistant working with PriceSenz's recruiting team
on a Senior Backend Engineer role. Your background in payments
engineering is the reason I'm reaching out.

The role focuses on Go and AWS-based payments infrastructure. The
team is shipping a multi-region rewrite this quarter, so the next
hire owns the throughput layer design. Stack is Go, AWS, Postgres,
and Kafka.

Best fit: engineers with prior production payments experience.

Would you like to go through a few quick questions to assess fit?

— Zee, supporting the PriceSenz recruiting team
```

**Quality check:**

- [x] Length: 98 words (within 75 to 140 band)
- [x] Identity line present
- [x] No banned phrases
- [x] Timeline anchor present (multi-region rewrite this quarter)
- [x] Persona line present
- [x] Single CTA
- [x] Approved signoff
- [x] Subject under 50 characters

**Suggested send window:** Tuesday 9am CT (Dallas local).

**Closing prompt for the recruiter:**

> Generated Balanced variant only. Want me to also produce Compact (mobile-first) or Executive (director-track) variants?

---

## When the recruiter explicitly requests all variants

### Input

**Variants requested:** all (or "all variants", "every option", "Balanced, Compact, and Executive")

### Output

Three variants generated. Default deploy: **Balanced**. A/B test with **Compact** if running an experiment. Use **Executive** only if escalating to a director-track variant of the role.

#### Variant 1 — Balanced (recommended default)

**Suggested filename:** `02_messages/touch1_email_balanced.md`

(Same content as default example above.)

#### Variant 2 — Compact (mobile-first, A/B test)

**Suggested filename:** `02_messages/touch1_email_compact.md`

**Subject:** Senior Backend Engineer, payments

**Body (62 words):**

```
Hi Sofia,

I'm Zee, an AI assistant with PriceSenz recruiting on a Senior
Backend Engineer role. Your payments background is why I'm
reaching out.

Go, AWS, Postgres, Kafka. Multi-region payments rewrite shipping
this quarter; next hire owns throughput design.

Best fit: engineers with production payments experience.

Open to a few quick questions?

— Zee, supporting the PriceSenz recruiting team
```

**Use when:** Candidate cohort is mobile-first, or A/B test of length effect.

#### Variant 3 — Executive (director-track variant only)

**Suggested filename:** `02_messages/touch1_email_executive.md`

**Subject:** Senior Backend Engineer, payments infrastructure leadership

**Body (118 words):**

```
Hi Sofia,

I'm Zee, an AI assistant working with PriceSenz's recruiting team
on a Senior Backend Engineer role with technical leadership scope.
Your payments background is why this surfaced.

The role owns design of the multi-region throughput layer for our
payments infrastructure. The team is mid-flight on a regional
rewrite shipping this quarter; this hire makes the architectural
calls on partition strategy, idempotency, and settlement.

Stack: Go, AWS, Postgres, Kafka.

Best fit: engineers with production payments at scale, ready to
own architecture-level decisions.

Would you like to go through a few quick questions to assess fit?

— Zee, supporting the PriceSenz recruiting team
```

**Use when:** The role has an architect or staff-level variant, or when targeting candidates with 10+ years experience.

---

## What was rejected and why

The first draft of the Balanced variant contained "your impressive background in payments engineering" in sentence 2. This is a banned fake-personalization phrase. Regenerated with "Your background in payments engineering is the reason I'm reaching out" — same anchor, structured as a stated reason rather than flattery.

The first draft of the Compact variant had two CTAs ("Open to questions, or want me to send the JD?"). Regenerated with single CTA.

---

## Follow-up generation

Touches 2 to 4 are generated separately. Each is a new Mode 3 request specifying:

- Touch number (2, 3, or 4)
- Channel (LinkedIn, email, SMS depending on archetype channel sequence)
- Variants requested (default Balanced only)

Each follow-up references touch 1 by one phrase and introduces one new angle. No repetition of the full opener.
