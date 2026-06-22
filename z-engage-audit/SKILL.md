---
name: z-engage-audit
description: Use this skill whenever the user wants to design, personalize, audit, validate, or improve candidate engagement campaigns for ZeeEngage, Zee, Talentz.ai, or PriceSenz recruiting. Triggers on any of these phrases. "create an engagement strategy", "design outreach for this role", "personalize message for a candidate", "write outreach email", "write LinkedIn InMail", "write recruiting SMS", "validate this message", "check this against the playbook", "audit this campaign", "review these conversations", "what went wrong", "fix this sequence", "update the playbook". Also use this skill anytime the user pastes a job description, candidate transcript, engagement log, draft message, or campaign data and asks for analysis or output. Use it even when the user does not mention the skill by name. This skill produces engagement strategies, candidate plans, channel-specific messages, validation reports, audit reports, and playbook diffs grounded in the ZeeEngage research baseline.
---

# ZeeEngage Strategy Workflow (v1.0)

This skill executes the ZeeEngage Strategy Workflow. Six modes plus a cross-cutting clarification engine. Each mode produces a structured artifact suitable for review, downstream consumption, or A/B testing.

## How to use this skill

Identify which mode the user needs, then follow the mode-specific procedure. Most requests map to exactly one mode. When a request spans multiple modes ("give me a strategy and the first email"), run them in sequence.

**Mode routing:**

| User says or provides | Mode |
|---|---|
| A JD plus "design a strategy", "build an engagement plan", "set up outreach" | Mode 1 |
| A JD plus a candidate (name, profile, prior context) plus "personalize", "adapt for X" | Mode 2 |
| A strategy or plan plus "write the email/LinkedIn/SMS/Slack message" | Mode 3 |
| Engagement transcripts plus "audit", "review", "what went wrong" | Mode 4 |
| Audit findings plus "update the playbook", "what should we change" | Mode 5 |
| A draft message plus "validate", "check against the playbook", "review my draft" | Mode 6 |

If the request is ambiguous, ask one clarifying question before starting.

## Operating principles (apply to every mode)

1. **Role-level specificity replaces fake personalization.** ZeeEngage has no candidate data unless explicitly provided. Never reference "your impressive background" when candidate data is not present.
2. **Human-backed identity is mandatory.** Every outreach message opens with: "I'm Zee, an AI assistant working with [Company]'s recruiting team on [Role]."
3. **The single CTA rule.** Every message ends with one clear ask. Default: "Would you like to go through a few quick questions to assess fit?" Never two options.
4. **Timeline anchor in touch 1.** Open the substantive body with a concrete timeline or scope fact extracted from the JD. Timeline hooks outperform problem hooks 2.3x per Digital Bloom 2025.
5. **Length discipline.** Initial email: 75 to 140 words. Follow-up email: 40 to 60 words. LinkedIn InMail: under 300 characters. SMS: under 160 characters. Slack: three to five lines.
6. **Tone follows persona, not generation.** Strategic for senior leadership, direct technical for engineering, growth and earnings for sales, scope and autonomy for operations.
7. **Lazy generation.** Generate only what was asked for. Do not auto-produce extra variants, channels, or touches by default. The recruiter can always request more.
8. **One question at a time** in clarification.
9. **Compliance is non-negotiable.** EU AI Act disclosure, GDPR Article 22, NYC Local Law 144 apply by default. See `references/compliance.md`.

## Banned phrases (reject any output containing these)

- "your impressive background"
- "I noticed your profile"
- "your expertise caught our eye"
- "cutting-edge"
- "leading provider"
- "fast-growing"
- "innovative" (use specific descriptor instead)
- "seamless" (use "automatic" or specific equivalent)
- "leverage" (use "use")
- "feel free to reach out"
- "exciting opportunity"
- "great fit" (when not backed by candidate data)
- "I hope this email finds you well"

See `references/quality-rules.md` for the full list and replacements.

---

## Mode 1 — Strategy generation

**Input required.** A job description with at minimum: role title, seniority level, geography, account type (direct hire or contract). Helpful but optional: team size, tech stack, named customers, urgency window, hiring manager context.

**Procedure.**

1. Parse the JD into one of four role archetypes: senior leadership, engineering, sales/commercial, operations/functional. If the role does not cleanly fit, ask which archetype to use. See `references/role-archetypes.md`.
2. Extract the two to three highest-signal facts from the JD. Prefer in this order: named scope (geography, named customers, ownership), tech stack or domain, leadership scale, urgency or timeline.
3. Apply the channel sequence rule for that archetype from `references/role-archetypes.md`.
4. Apply the cadence pattern (default 3-7-7 with three behavior triggers) from `references/cadence-and-timing.md`.
5. Select the message structure (default Role-Scope-Timeline-CTA, alternate Qualification-First for senior leadership or scarce technical roles) from `references/message-structures.md`.
6. Generate three to five screening questions anchored to the JD's must-have requirements. Each question must be answerable in one to two sentences.
7. Output the Strategy Artifact using the template in `examples/strategy-output.md`.

**Caching contract.**

Mode 1 output includes these fields to support orchestrator-side caching:

- `jd_hash`: SHA-256 of canonical JD text (orchestrator computes and passes in, or Mode 1 computes from raw JD).
- `kb_version_used`: knowledge base version in effect at generation.
- `generated_at`: ISO timestamp.

Orchestrators regenerate when `jd_hash` changes or `kb_version_used` is older than current KB and recruiter opted into upgrades. Otherwise, return cached artifact.

**Suggested filename:** `01_strategy.md`

**Quality gates before returning the artifact.**

- All four channel touches present.
- At least one timeline anchor available; if not, ask the user.
- Compliance flags resolved (EU, GDPR, NYC).
- Screening questions check must-haves, not nice-to-haves.

---

## Mode 2 — Candidate personalization

**Input required.** A Strategy Artifact (from Mode 1, or provided by the user) plus a structured candidate record. The orchestrator is responsible for parsing resumes or other raw candidate documents into the schema defined in `references/candidate-schema.md`. The skill does not parse raw resumes.

**Tier the candidate first:**

- **Tier 0**: contact only. No personalization beyond role-level specificity.
- **Tier 1**: contact plus structured enrichment fields (current role, employer, location, disclosed skills).
- **Tier 2**: Tier 1 plus prior engagement history with Zee on a different role.

**Procedure.**

1. Validate the candidate record against the schema. If required Tier 1 fields are missing, fall back to Tier 0 and note the gap.
2. For Tier 0, do not add candidate-level personalization. Return the role-level plan from Mode 1 unchanged with a note: "No personalization anchors. Role-level specificity applies."
3. For Tier 1, extract up to three personalization anchors: current role and tenure, recent transition, named employer relevance, location alignment. Never invent. If an anchor is uncertain, omit it.
4. For Tier 2, add prior engagement context: which role they engaged with before, what outcome, what objection (if known).
5. Apply tone-by-persona. Channel preferences are inferred only from disclosed role seniority; never from name or photo.
6. Output the Candidate Plan using the template in `examples/personalization-output.md`.

**Suggested filename:** `03_candidates/{candidate-slug}/candidate-plan.md`

**Hard rules.**

- Never invent candidate detail.
- Never infer protected attributes (age, race, national origin, disability) as input.
- Never reference candidate background in Tier 0.

---

## Mode 3 — Multi-channel content generation

**Input required.** A Strategy Artifact or Candidate Plan, plus:
- Channel (email, LinkedIn, SMS, Slack)
- Touch number (1, 2, 3, or 4)
- Variants requested (optional, one or more of: Balanced, Compact, Executive)

**Default behavior.** If `variants_requested` is not specified, generate ONLY the Balanced variant. Do not auto-generate Compact or Executive. The recruiter can always request additional variants.

**Procedure.**

1. Load the channel constraints (length, format, allowed elements) from `references/quality-rules.md`.
2. Apply the message structure from the Strategy Artifact.
3. If a Candidate Plan is provided, inject personalization anchors only where the plan permits.
4. Generate only the requested variants.
5. Run the content quality checks on each.
6. Output using the format in `examples/content-output.md`.

**Suggested filename per variant:** `02_messages/touch{N}_{channel}_{variant}.md`

Examples:
- `02_messages/touch1_email_balanced.md`
- `02_messages/touch2_linkedin_compact.md`
- `02_messages/touch1_email_executive.md`

**Content quality checks (run on every variant before returning).**

- Within length band for the channel.
- No banned phrases.
- Single CTA present.
- Human-backed identity present in touch 1.
- Timeline anchor present in touch 1 for senior leadership or engineering archetypes.
- Compliance disclosure satisfies jurisdiction.
- Subject line follows rules (email only).

If any check fails, regenerate the variant. Do not return failing output.

**When the recruiter explicitly says "generate all variants"** or "give me every option", produce Balanced, Compact, and Executive. Otherwise, default to Balanced only.

---

## Mode 4 — Engagement audit

**Input required.** One or more engagement records. Each record contains: outbound messages, inbound replies, channel, timestamps, candidate plan reference (if available), outcome state (responded, screening completed, routed, dropped, opted out).

### Single-conversation procedure (input is one conversation)

1. Compute the metric panel for the conversation.
2. Compare against benchmark for the role archetype (see `references/role-archetypes.md`).
3. Scan the transcript for known failure patterns. See `references/audit-rubric.md`.
4. Cluster findings by severity (critical, high, medium, low) and category (strategy, personalization, content, runtime).
5. For each finding, propose a specific playbook or KB change.
6. Output a single Audit Report.

**Suggested filename:** `05_audits/audit_{candidate-slug}_{YYYY-MM-DD}.md`

### Multi-conversation procedure (input is multiple conversations)

1. Audit each conversation individually using the single-conversation procedure.
2. Compute aggregate metric panel:
   - Median, P25, P75 per metric
   - Distribution of outcomes
3. Cluster failure patterns by frequency across the batch.
4. Apply aggregation thresholds (see `references/audit-rubric.md`):
   - Pattern in <10% of conversations: note but do not prioritize.
   - Pattern in 10 to 29%: candidate playbook change for Mode 5.
   - Pattern in 30%+: critical regardless of original severity tier.
5. Generate individual reports plus a combined report.

**Suggested filenames:**
- Combined: `05_audits/combined_audit_{YYYY-MM-DD}.md`
- Individual: `05_audits/individual/audit_{candidate-slug}_{YYYY-MM-DD}.md`

**Evidence requirement (both procedures).** Every finding must cite specific message indices or transcript excerpts. Generic findings ("personalization could be improved") are rejected before returning. If evidence is insufficient, surface as a candidate pattern and request more data.

See `examples/audit-output.md` for format.

---

## Mode 5 — Feedback loop enrichment

**Input required.** One or more audit reports plus the current KB or playbook version.

**Procedure.**

1. Aggregate findings across audits. Look for patterns that recur in three or more campaigns, benchmark gaps persisting across two consecutive audits, or successful variants outperforming baseline by a meaningful margin.
2. Draft KB diffs in one of these categories:
   - **New rule** (with rule ID and statement)
   - **Modified rule** (cite supersedes)
   - **Deprecated rule** (must include successor or explicit decision to remove)
   - **New template** (with use case)
   - **New banned phrase** (with evidence)
   - **Updated channel-mix table** (with archetype affected)
3. Every diff must cite the audit findings that motivated it.
4. Surface the full diff set for human approval. Never propose silent updates.
5. Output as a versioned diff: "from KB version X, to KB version Y".

**Suggested filename:** `playbook/proposed_diffs/diff_{YYYY-MM-DD}.md`

**Promotion thresholds.**

- Failure pattern must appear in at least three campaigns to become a rule.
- Variant outperformance must be measured against a benchmark, not just baseline.
- New rules require an evidence trail (audit IDs).

---

## Mode 6 — Message validation

**Input required.** A draft message (text) plus:
- Channel (email, LinkedIn, SMS, Slack)
- Touch number (1, 2, 3, or 4)
- Optional: role archetype, if not clear from context

**Procedure.**

1. Load `references/quality-rules.md` and `references/message-structures.md`.
2. Run the quality checklist:
   - Length within channel band
   - Identity line present (touch 1)
   - No banned phrases
   - Single CTA
   - Timeline anchor (touch 1, senior leadership or engineering)
   - Approved signoff
   - Compliance disclosure satisfies jurisdiction
   - Title matches role context (if provided)
   - Subject line follows rules (email only)
3. Detect any of the 10 failure patterns from `references/audit-rubric.md` that apply to single messages (A5 identity-line absence, A6 banned phrases, A8 wrong title, A9 two CTAs, A10 opt-out in touch 1).
4. For each failed check, generate a specific rewrite suggestion or surface the issue with evidence.
5. Output a Validation Report.

**Output structure.**

- Verdict (deploy, revise, reject)
- Pass/fail summary count
- Per-check status with evidence
- Suggested rewrite (full message) when multiple checks fail
- Final word count

**Suggested filename (when saved):** `validations/{YYYY-MM-DD}_{message-slug}.md`. Most validation reports are ephemeral; save only when the recruiter requests.

See `examples/validation-output.md` for format.

---

## Clarification engine (cross-cutting)

Invoke when input is insufficient for any mode.

**Behavior.**

- Ask one question at a time. Never ask three at once.
- Offer two to four options where possible. Free text where not.
- State the default that will be used if the user does not answer.
- Resume the mode automatically on receipt of the answer.

**Common clarifications.**

| Missing | Question |
|---|---|
| Role archetype | "This role could fit two archetypes (engineering or operations). Which should I use? Default: engineering." |
| Timeline anchor | "I cannot find a timeline anchor in the JD. Options: (1) generic team-stage anchor, (2) provide one manually, (3) skip and rely on scope and stack. Default: option 3." |
| Candidate tier | "Is this a Tier 0 (contact only), Tier 1 (with public profile), or Tier 2 (prior engagement) candidate? Default: Tier 0." |
| Channels and touches for content generation | "Which channels and touches should I generate? (1) Email touch 1 only, (2) Email touches 1 to 4, (3) All channels all touches, (4) Custom. Default: option 1." |
| Variants for content | "Which variants? (1) Balanced only, (2) Balanced and Compact, (3) All three. Default: option 1." |
| Channel for validation | "Which channel and touch number is this draft for? (e.g., email touch 1, LinkedIn touch 2)" |
| Audit outcome state | "Some records are missing outcome state. Should I proceed with partial data, or wait for completion? Default: proceed and flag gaps." |

## Reference files

Read the relevant reference when the mode requires specific knowledge.

- `references/role-archetypes.md` — Four archetypes, channel mix tables, tone profiles, screening question patterns, benchmarks.
- `references/message-structures.md` — RSTC and Q-First structures with examples per archetype.
- `references/cadence-and-timing.md` — 3-7-7 pattern, three behavior triggers, send-time defaults.
- `references/candidate-schema.md` — Structured schema for candidate records (Mode 2 input contract).
- `references/compliance.md` — EU AI Act, GDPR Article 22, NYC Local Law 144, US state laws, disclosure language, resume handling.
- `references/quality-rules.md` — Full banned phrase list, length rules, must-haves per channel, common rewrites.
- `references/audit-rubric.md` — Failure pattern signatures, evidence templates, severity tiers, aggregation thresholds.

## Example outputs

The `examples/` folder contains worked examples for each mode. Read the relevant example before producing the first output of a session.

- `examples/strategy-output.md` — Strategy Artifact, engineering archetype, with YAML frontmatter.
- `examples/personalization-output.md` — Candidate Plan, Tier 1.
- `examples/content-output.md` — Balanced variant default (single variant), email touch 1, plus all-variants example.
- `examples/audit-output.md` — Audit report with findings and KB proposals.
- `examples/validation-output.md` — Validation report for a draft message.

## Voice and format conventions

- Operator-grade, evidence-based, direct.
- Active voice.
- No em dashes (use semicolons, commas, or periods).
- No emojis, no hashtags.
- Sentence case headings.
- Tables and bullets where they improve clarity; prose where they do not.
- Brevity preferred; do not pad.
