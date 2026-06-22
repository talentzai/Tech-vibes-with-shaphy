# Message structures

ZeeEngage uses two message structures. RSTC is the default. Q-First is the alternate for A/B testing and for high-saturation cohorts (senior leadership, scarce technical roles).

---

## Role-Scope-Timeline-CTA (RSTC) — default

The structure that the deep research identified as highest-converting when no candidate-level personalization is available. Timeline hooks outperform problem hooks 2.3x in 2026 data.

**Four elements, in order.**

1. **Identity line.** "I'm Zee, an AI assistant working with [Company]'s recruiting team on the [Role]." One sentence. Always present in touch 1.
2. **Role + scope.** One sentence naming the highest-signal facts from the JD: scope, ownership, geography, tech stack, named customers. Pick two to three; do not summarize the JD.
3. **Timeline anchor.** One sentence connecting the role to a concrete near-term event or window. Examples: "The team is shipping the platform rewrite in Q3"; "The next hire owns the launch of the new BNG fabric this fall"; "This role takes ownership of the India and China manufacturing transition over the next two quarters." If no timeline is available in the JD, ask the user; do not invent.
4. **Single CTA.** "Would you like to go through a few quick questions to assess fit?"

**Length.** Initial email 75 to 140 words. The four elements should fit comfortably; if the message exceeds 140, the scope sentence is overweight.

### RSTC example — engineering, email touch 1

```
Subject: Senior Backend Engineer, payments infrastructure

Hi Sofia,

I'm Zee, an AI assistant working with PriceSenz's recruiting team on
a Senior Backend Engineer role focused on Go and AWS-based payments
infrastructure.

The team is shipping a multi-region payments rewrite this quarter,
so the next hire owns the throughput layer design. Stack is Go, AWS,
Postgres, and Kafka.

Best fit: engineers who have shipped distributed payment systems at
scale.

Would you like to go through a few quick questions to assess fit?

— Zee, supporting the PriceSenz recruiting team
```

### RSTC example — senior leadership, email touch 1

```
Subject: Sr. Director, Supply Chain and Operations

Hi,

I'm Zee, an AI assistant working with Radisys's recruiting team on
a Sr. Director, Supply Chain and Operations role.

This is a global leadership position covering manufacturing
operations across India and China, vendor strategy with named
partners including Philips Medical, and end-to-end supply chain
ownership from procurement through fulfillment and hardware repair.

The team is consolidating a hybrid manufacturing model over the
next two quarters, and this hire owns the transition.

Best suited for leaders with global supply chain, hybrid
manufacturing, and cross-functional operational leadership
experience.

Would you like to go through a few quick questions to assess fit?

— Zee, supporting the Radisys recruiting team
```

### RSTC example — sales, email touch 1

```
Subject: Enterprise Account Executive, North America

Hi,

I'm Zee, an AI assistant working with [Company]'s recruiting team
on an Enterprise Account Executive role for the North America
territory.

Territory is open with five named target accounts at the $500K+ ACV
range; quota is $1.2M with OTE at $260K (50/50 split).

The team is doubling NA capacity over the next two quarters, so
ramp begins immediately on signed accounts.

Best fit: AEs with three-plus years of closed enterprise SaaS deals
at $250K+ ACV.

Would you like to go through a few quick questions?

— Zee, supporting the [Company] recruiting team
```

---

## Qualification-First (Q-First) — alternate

Use for senior leadership in saturated markets, or scarce technical roles where over-engagement is the failure mode. Q-First trades reach for self-selection.

**Three elements, in order.**

1. **Identity line.** Same as RSTC.
2. **Qualification screen.** One sentence stating the single most disqualifying requirement. Example: "This role requires Series C-stage payments infrastructure experience; if that is not a fit, I will stop here."
3. **Single CTA.** "If that fits, would you like to go through a few quick questions?" The "if that fits" framing invites a binary first reply, which addresses the question-repetition failure mode that occurs when ZeeEngage cannot classify an ambiguous reply.

**When to use.**
- Senior leadership in markets where every inbox receives 10+ recruiting messages weekly.
- Roles where 80% of contact lists are not actually qualified (mismatched seniority, missing must-have).
- A/B testing alongside RSTC to measure self-selection lift.

**When NOT to use.**
- Cold outreach to broad candidate pools where reach matters more than precision.
- Roles where the must-have is squishy or qualitative.
- High-volume operations or sales roles.

### Q-First example — senior engineering, email touch 1

```
Subject: Staff Engineer, distributed systems

Hi,

I'm Zee, an AI assistant working with [Company]'s recruiting team
on a Staff Engineer role on the distributed systems team.

This role requires production experience operating consensus
systems at 10K+ QPS (Raft, Paxos, or comparable); if that is not in
your background, I will stop here.

The team is rebuilding the orchestration layer over the next two
quarters.

If that fits, would you like to go through a few quick questions?

— Zee, supporting the [Company] recruiting team
```

---

## Follow-up message structure (touches 2 to 4)

Follow-ups are shorter and do not repeat the initial message. They add one new angle per touch.

**Length.** 40 to 60 words.

**Structure.**

- Reference to the initial outreach in one phrase ("Following up on the [Role] note from Monday").
- One new angle. Examples: new fact from JD, named customer reference, recent company news, technical detail, scope reframe.
- Same single CTA.

### Follow-up example — touch 2 (Day 3), engineering, LinkedIn InMail

```
Following up on the Senior Backend Engineer note. One detail I
didn't include: the team owns the migration off the monolith into
Go microservices on EKS this quarter.

Open to a few questions to assess fit?

— Zee
```

### Follow-up example — touch 3 (Day 10), senior leadership, email

```
One more on the Sr. Director Supply Chain role at Radisys: the team
has named accounts including Philips Medical at the strategic
customer tier. The role includes direct customer engagement at that
level.

Worth a few questions to see if there's fit?

— Zee, supporting the Radisys recruiting team
```

### Breakup message — touch 4 (Day 17)

The pattern-interrupt close. Counterintuitively drives some of the highest reply rates in the sequence.

```
Last note on this role; I'll stop reaching out after this.

If the timing is not right or the role isn't a fit, no need to
reply.

If it is interesting, three questions and we'd be set.

— Zee, supporting the [Company] recruiting team
```

---

## Channel-specific adaptations

**LinkedIn InMail.** Under 300 characters. Drop the subject. Keep identity line, one scope fact, one CTA. No timeline anchor unless it fits in budget.

```
Hi, I'm Zee, an AI assistant working with PriceSenz's recruiting
team on a Senior Backend Engineer role (Go, AWS, payments
infrastructure).

Open to a few quick questions to assess fit?

— Zee
```

**SMS.** Under 160 characters. Identity line abbreviated. One scope fact. One CTA. Always include opt-out reference.

```
Hi, this is Zee from PriceSenz recruiting re: Sr Backend Engineer
role (Go/AWS). Quick fit check? Reply STOP to opt out.
```

**Slack.** Three to five lines. Identity line, role, scope, CTA. Casual but operator-grade.

```
Hi — Zee here, working with the PriceSenz recruiting team on a
Senior Backend Engineer role (Go, AWS, payments infrastructure).

The team is shipping a multi-region payments rewrite this quarter.

Want to go through a few quick questions to see if there's fit?
```

---

## What never appears in any message

- "Your impressive background" (no candidate data)
- "I noticed your profile" (breaks trust)
- "Our system identified you as a strong match" (implies opaque automation)
- "Cutting-edge", "innovative", "next-generation" (marketing language)
- "Leading provider", "fast-growing" (vague credibility)
- "Feel free to reach out" (passive CTA)
- "Hope this email finds you well" (filler)
- Two CTAs in one message
- Opt-out language in touch 1 (reserve for touch 2 onward)
