# Compliance rules

Compliance is non-negotiable. ZeeEngage operates under multiple overlapping regulatory frameworks. This file lists the operative rules and the disclosure language that satisfies them.

---

## EU AI Act (applies to candidates in EU or roles based in EU)

**Classification.** Recruitment AI is classified as high-risk under Annex III.

**Operational requirements.**

1. **Disclosure of AI involvement.** Candidates must be informed when AI is involved in outreach and hiring processes. Required at first contact.
2. **Meaningful human oversight (Article 14).** A human must approve advancement decisions. ZeeEngage routes; humans decide.
3. **Right to explanation (Article 86).** Candidates can request the basis for an automated decision. ZeeEngage's conversation summary and screening responses must be retrievable on request.
4. **Bias audits.** Annual independent bias audits required for high-risk systems.

**Disclosure language that satisfies EU AI Act.**

Touch 1 identity line:
> "I'm Zee, an AI assistant working with [Company]'s recruiting team on the [Role]."

Optional explicit disclosure footer (use when EU candidate confirmed):
> "Zee is an AI assistant. A human recruiter will review your responses before any next steps. You can request to interact with a human at any time by replying with 'human'."

**Enforcement timeline.** EU AI Act high-risk provisions are enforceable starting 2 August 2026. Digital Omnibus package proposed November 2025 may extend this; treat the August 2026 date as the operating target.

---

## GDPR (applies to candidates in EU or whose data is processed in EU)

**Article 22 (automated decision-making).**

Candidates have the right to:
- Be informed of automated decision-making.
- Contest automated decisions.
- Obtain human review of decisions producing legal or significant effects.

**ZeeEngage posture.** ZeeEngage does not make hiring decisions. Screening responses are routed to a human recruiter for review. Document this boundary in the audit trail; surface it to candidates on request.

**Data subject rights to support.**
- Access (Article 15)
- Rectification (Article 16)
- Erasure (Article 17, "right to be forgotten")
- Restriction (Article 18)
- Portability (Article 20)
- Objection (Article 21)

**Retention.** Candidate data collected via ZeeEngage must follow Talentz.ai's published retention policy. Default: delete personal data 12 months after last interaction unless candidate consents to longer retention or company has documented business justification.

**Lawful basis.** Legitimate interest is the default lawful basis for cold outreach to professional contacts. Document the legitimate interest assessment per role.

---

## NYC Local Law 144 (applies to candidates and roles in NYC)

**Scope.** Automated Employment Decision Tools (AEDTs) used in hiring decisions.

**Requirements.**
1. Bias audit by independent auditor within one year prior to use.
2. Pre-use notification to candidates (at least 10 business days before AEDT use).
3. Public summary of audit results.
4. Notification of categories of data used and source.

**ZeeEngage posture.** Outreach and screening collection do not constitute AEDT use under Local Law 144's current interpretation. The assessment phase (ZeeLens) is the AEDT touchpoint. Document the boundary clearly in any audit trail visible to NYC candidates.

If ZeeEngage's screening recommendations are interpreted by a recruiter as a hiring decision input, the AEDT classification may apply. Treat this as an open compliance question and consult counsel before deploying screening-based ranking in NYC roles.

---

## US state laws (overview)

| State | Law | Relevance to ZeeEngage |
|---|---|---|
| Illinois | Artificial Intelligence Video Interview Act (2020) | Applies to video assessments (ZeeLens), not ZeeEngage |
| Maryland | HB 1202 (2020) | Facial recognition consent for video interviews |
| Colorado | AI Act (2024, effective 2026) | High-risk AI requirements similar to EU |
| Texas | TX SB 1893 (2024) | Government use; commercial impact limited |
| California | AB 1018 (2024, ADMT regulations) | Automated decision-making transparency |

**Operational rule.** For US-wide campaigns, satisfy the strictest applicable state's requirements. In practice, this means: disclose AI involvement at first contact, maintain human review at routing, support data subject rights at parity with GDPR.

---

## SMS-specific compliance

**TCPA (US).** Express written consent required for marketing SMS. Recruiting SMS to candidates whose phone numbers were obtained from a list provided by a recruiter typically falls under transactional use. Include opt-out language ("Reply STOP to opt out") regardless.

**CASL (Canada).** Express consent required. Include sender identification and opt-out in every SMS.

**Mandatory SMS template.**
```
Hi, this is Zee from [Company] recruiting re: [Role]. Quick fit
check? Reply STOP to opt out.
```

---

## Opt-out handling

**When to handle opt-out.**

Any inbound containing: STOP, UNSUBSCRIBE, REMOVE, DO NOT CONTACT, NOT INTERESTED (final), or equivalent in any channel.

**Action.**
1. Immediate suppression from all current ZeeEngage campaigns for the company.
2. Permanent suppression from future ZeeEngage campaigns for the company unless candidate explicitly re-opts in.
3. No final message ("OK, stopping" is acceptable; "are you sure?" is not).
4. Log the opt-out with timestamp and channel.

**Cross-company opt-out.** Opt-out is per-company by default. A candidate who opts out of [Company A] outreach may still receive [Company B] outreach. If candidate requests cross-company opt-out, honor it across Talentz.ai entirely.

---

## Disclosure language library

### Required in touch 1 (all candidates, all jurisdictions)

```
I'm Zee, an AI assistant working with [Company]'s recruiting team
on the [Role].
```

### Optional explicit disclosure (use for EU candidates or when uncertain)

```
A note on how this works: I'm an AI assistant. I handle the
outreach and screening step. A human recruiter reviews everything
and decides next steps. Reply with "human" anytime and I'll hand
this off.
```

### Required at handoff (any candidate routed to a recruiter)

```
I'm passing this to [Recruiter Name], who will reach out within
[SLA]. They have our full conversation, so you don't need to
repeat anything.
```

### Required on opt-out confirmation

```
Got it. I've removed you from this and future outreach for
[Company]. Best of luck out there.

— Zee
```

---

## Audit trail requirements

Every ZeeEngage conversation must log:

1. Candidate identifier and contact method.
2. Source of contact (recruiter-provided list, enrichment vendor, public list).
3. Outreach timestamps and channels.
4. Inbound messages with timestamps.
5. Intent classifications and confidence scores (for compliance review).
6. Screening responses (structured).
7. Routing decision and timestamp.
8. Human reviewer identity and decision.
9. Opt-out events with timestamp.
10. Any candidate request for human handoff or explanation.

Audit trails must be retrievable within 30 days for any active candidate and within 90 days for any candidate in the past 12 months.

---

## When in doubt

- If the regulatory question is borderline, default to the stricter interpretation.
- If a new jurisdiction is encountered (international roles, new state laws), flag to product or legal before proceeding.
- Compliance gaps surface in quarterly reviews; document and remediate.

---

## Resume handling (orchestrator responsibility)

Resumes contain personal data subject to GDPR, CCPA, and similar laws. The skill does not parse raw resumes; the orchestrator (Cowork or any other caller) is responsible. The rules below apply to whichever system ingests resumes.

**Required at ingestion.**

1. Tag the resume's source jurisdiction (EU, US, Canada, etc.) based on candidate location and source.
2. Apply the strictest applicable retention rule by default.
3. Record the source of the resume (recruiter upload, ATS export, candidate self-submission, enrichment vendor).

**Hard rules for parsing into the candidate record schema.**

- Never extract: photo, age, marital status, photo-derived attributes (perceived race, ethnicity, gender), religious affiliation, political affiliation, sexual orientation, disability status, citizenship beyond work-authorization confirmation.
- Never extract: any field that could enable proxy discrimination (e.g., year of college graduation as age signal).
- Leave fields blank if uncertain. Never invent.
- Source field is required for audit trail.

**Right-to-erasure handling.**

When a candidate exercises GDPR Article 17 (or equivalent) right to be forgotten:

1. Delete the resume file within 30 days.
2. Delete the Candidate Plan (Mode 2 output) for that candidate.
3. Anonymize or delete the candidate's references in any saved audit reports (Mode 4 output). Anonymization replaces the candidate slug with an opaque identifier; the audit findings remain available for KB enrichment.
4. Log the erasure event with timestamp, requesting party, and confirmation of completion.

**Cross-jurisdictional handling.**

When a resume comes from one jurisdiction and the role is in another, apply the stricter regulatory regime. Example: an EU-resident candidate applying for a US role triggers full GDPR protections regardless of role location.

**Retention defaults (overridable per `config/retention.json`).**

| Source jurisdiction | Default retention | Maximum retention |
|---|---|---|
| EU (GDPR) | 12 months from last interaction | 24 months with documented business justification |
| California (CCPA) | 12 months from last interaction | 24 months |
| US general | 24 months | 36 months |
| Canada (PIPEDA) | 12 months from last interaction | 24 months |

After retention period, resume files are deleted from primary storage. Derived audit data is anonymized but may be retained for KB enrichment.
