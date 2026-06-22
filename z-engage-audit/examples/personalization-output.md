# Example Mode 2 output — Candidate Plan

This example shows the output format for Mode 2. Engineering archetype, Tier 1 candidate.

---

## Input

**Strategy reference:** stg_pricesenz_be_2026_05 (from Mode 1 example)

**Candidate record (provided by user):**
> Name: Sofia M.
> Email: sofia.m@[redacted]
> Current role: Senior Software Engineer at Stripe (since Aug 2023)
> Location: Dallas, TX
> Public profile: Disclosed Go and AWS experience; payments background at prior employer (PayPal, 2019-2023)
> Prior Zee interaction: None

**Tier classification:** Tier 1 (contact plus public profile data, no prior interaction history).

---

## Output

# Candidate Plan

**Plan ID:** plan_sofia_m_2026_05_15
**Strategy ref:** stg_pricesenz_be_2026_05
**Candidate ref:** cand_sofia_m

---

## Tier and rationale

**Tier:** 1

**Rationale:** Contact information provided. Public profile data confirms current role (Stripe), tenure (since Aug 2023), prior employer with relevant domain (PayPal payments), location alignment (Dallas matches hybrid role requirement).

---

## Personalization anchors (up to 3)

1. **Current role and tenure.** Senior Software Engineer at Stripe since Aug 2023. Use sparingly; do not lead with it.
2. **Domain overlap.** Prior payments experience at PayPal. Strong signal for the role's payment infrastructure focus.
3. **Location alignment.** Dallas-based; matches the hybrid requirement without relocation friction.

**Not used (insufficient signal):**
- Personal projects, GitHub activity (not provided in record)
- Education (not relevant to outreach)

---

## Channel overrides

None. Default engineering channel sequence applies.

---

## Tone calibration

Direct technical with light career-anchor framing. The payments domain overlap is the strongest single hook; lead with it after the identity and role.

---

## Hard rules (do not violate)

- Do not invent detail beyond what is in the candidate record.
- Do not infer protected attributes from name (no gender or ethnicity inference).
- Do not reference the personal life (no marriage, family, age signals).
- Do not use prior employer in a way that implies poaching ethics issue ("we know Stripe is going through transitions").
- If any of the three anchors above feels uncertain at content-generation time, omit it. Specificity > completeness.

---

## First-touch signal priority

For touch 1 (email), the agent should prioritize in order:

1. Identity line (always).
2. Role and scope (always).
3. Timeline anchor from strategy (multi-region payments rewrite this quarter).
4. **One light personalization touch.** Payments domain overlap is acceptable: "Your payments background is what triggered this outreach." Phrase as a stated reason for contacting, not as fake personalization.
5. Persona line.
6. Single CTA.

---

## What to avoid in Sofia's content

- "Your impressive background" (banned phrase)
- "I noticed your profile at Stripe" (reads as data-stalking even when accurate)
- Reference to Stripe's internal situation, mergers, layoffs, or anything not directly relevant to the role
- Implication that we know more about Sofia than we do

---

## Sample first-touch framing for content generation

(For Mode 3 to consume.)

```
Identity: I'm Zee, an AI assistant working with PriceSenz's recruiting team on a Senior Backend Engineer role.

Reason for contact (light personalization): Your background in payments engineering is the reason I'm reaching out.

Role and scope: The role focuses on Go and AWS-based payments infrastructure at PriceSenz, with a multi-region rewrite shipping this quarter. Stack is Go, AWS, Postgres, Kafka.

Persona: Best fit: engineers with prior production payments experience.

CTA: Would you like to go through a few quick questions to assess fit?

Signoff: — Zee, supporting the PriceSenz recruiting team
```

Mode 3 will consume this and generate three variants (Balanced, Compact, Executive).

---

## Compliance notes

- Tier 1 enrichment from public profile data; no scraping. Source: recruiter-provided LinkedIn URL plus People Data Labs API match. Logged for audit.
- Sofia is Dallas-based; US compliance applies. EU AI Act not applicable. NYC Local Law 144 not applicable.
- Opt-out tracking active across all touches.

---

## Notes for the recruiter

- Strong fit signals based on disclosed background.
- If she responds, prioritize for early review; payments engineers with Stripe-level experience are scarce.
- Recommended escalation SLA on positive response: 15 minutes business hours (per HITL handoff rules).
