# Candidate record schema

This file defines the structured schema that Mode 2 (candidate personalization) consumes. The skill does not parse raw resumes or LinkedIn profiles. The orchestrator (Claude Cowork, production ZeeEngage runtime, or any other caller) is responsible for parsing source documents into this schema. The skill operates on the structured record.

This separation keeps the skill focused on recruiting logic and prevents drift between skill behavior and orchestrator-specific parsing rules.

---

## Tier 0 — contact only

Minimum viable record. No personalization beyond role-level specificity.

```json
{
  "candidate_id": "string (required, unique per company)",
  "candidate_slug": "string (required, lowercase, hyphenated, e.g., 'sofia-m')",
  "tier": 0,
  "name": "string (required if known)",
  "email": "string (optional)",
  "phone": "string (optional, E.164 format)",
  "linkedin_url": "string (optional)",
  "source": "string (required, see Source field rules below)",
  "ingested_at": "ISO-8601 timestamp"
}
```

---

## Tier 1 — enrichment

Tier 0 fields plus structured enrichment from a parsed source (resume, LinkedIn, PDL, recruiter input).

```json
{
  "candidate_id": "string",
  "candidate_slug": "string",
  "tier": 1,
  "name": "string",
  "email": "string (optional)",
  "phone": "string (optional)",
  "linkedin_url": "string (optional)",
  "source": "string",
  "source_jurisdiction": "string (required, ISO-3166 country code or region, e.g., 'US-CA', 'EU-DE', 'IN')",
  "ingested_at": "ISO-8601 timestamp",

  "current_role": {
    "title": "string",
    "employer": "string",
    "start_date": "YYYY-MM",
    "tenure_months": "integer"
  },

  "prior_roles": [
    {
      "title": "string",
      "employer": "string",
      "start_date": "YYYY-MM",
      "end_date": "YYYY-MM",
      "tenure_months": "integer"
    }
  ],

  "location": {
    "city": "string",
    "state_or_region": "string",
    "country": "string"
  },

  "disclosed_skills": ["string"],

  "education": [
    {
      "institution": "string",
      "degree": "string",
      "field": "string (optional)"
    }
  ],

  "work_authorization": "string (optional, e.g., 'US-citizen', 'US-greencard', 'requires-sponsorship', 'EU-citizen')"
}
```

---

## Tier 2 — enrichment plus prior engagement

Tier 1 fields plus history of past interactions with Zee on other roles.

```json
{
  "...all Tier 1 fields...",
  "tier": 2,

  "prior_engagements": [
    {
      "role_id": "string (reference to a prior JD)",
      "role_title": "string",
      "outcome": "string (one of: responded, dropped, hired, declined, opted_out, other)",
      "objection": "string (optional, candidate's stated reason)",
      "engagement_date": "YYYY-MM-DD",
      "channel": "string (email, linkedin, sms, slack)"
    }
  ]
}
```

---

## Source field rules

The `source` field is mandatory at every tier. It captures where the candidate data came from. Accepted values:

- `recruiter-uploaded-resume` — recruiter dropped a resume file in `inbox/`
- `recruiter-typed` — recruiter typed details into chat
- `recruiter-pasted-profile` — recruiter pasted a LinkedIn or other profile
- `mcp-google-drive` — pulled from a watched Google Drive folder
- `mcp-aws-s3` — pulled from a watched S3 bucket
- `pdl-enrichment` — People Data Labs API
- `linkedin-google-api` — LinkedIn data via Google APIs
- `ats-export` — exported from a connected ATS

The source field is required for audit trail (GDPR compliance) and for the orchestrator's incremental processing logic.

---

## Required fields by tier

| Field | Tier 0 | Tier 1 | Tier 2 |
|---|---|---|---|
| candidate_id | Required | Required | Required |
| candidate_slug | Required | Required | Required |
| name | Required if known | Required | Required |
| source | Required | Required | Required |
| ingested_at | Required | Required | Required |
| source_jurisdiction | Optional | Required | Required |
| current_role | — | Required | Required |
| location | — | Required | Required |
| prior_engagements | — | — | Required |

If a Tier 1 record is missing `current_role` or `location`, downgrade to Tier 0 and inform the recruiter.

---

## Hard rules for orchestrators populating this schema

These rules are non-negotiable and apply to any system that builds a candidate record consumed by the skill.

**Never extract or infer:**

- Age, year of birth, year of graduation (as age signal).
- Race, ethnicity, national origin beyond work authorization.
- Religion or religious affiliation.
- Marital or family status.
- Sexual orientation, gender identity.
- Disability status.
- Political affiliation.
- Photograph or photo-derived attributes.
- Anything that could enable proxy discrimination.

**Never invent.**

- If a field is missing or ambiguous, leave it blank.
- Do not infer current employer from email domain.
- Do not infer location from phone area code.
- Do not infer tenure if dates are missing.

**Always log source.**

- Every field's source must be traceable in the audit trail.
- If a field is enriched (e.g., title from PDL, location from LinkedIn), tag the field with its sub-source where possible.

**Honor right-to-erasure.**

- When a candidate exercises GDPR Article 17 or equivalent, the entire record is deleted within 30 days. See `compliance.md` for the full procedure.

---

## Example records

### Tier 0 example

```json
{
  "candidate_id": "cand_johndoe_001",
  "candidate_slug": "john-doe",
  "tier": 0,
  "name": "John Doe",
  "email": "john.doe@example.com",
  "source": "recruiter-typed",
  "ingested_at": "2026-05-15T14:00:00Z"
}
```

### Tier 1 example (Sofia M., from the canonical Mode 2 example)

```json
{
  "candidate_id": "cand_sofiam_2026_05",
  "candidate_slug": "sofia-m",
  "tier": 1,
  "name": "Sofia M.",
  "email": "sofia.m@example.com",
  "source": "recruiter-uploaded-resume",
  "source_jurisdiction": "US-TX",
  "ingested_at": "2026-05-15T14:30:00Z",
  "current_role": {
    "title": "Senior Software Engineer",
    "employer": "Stripe",
    "start_date": "2023-08",
    "tenure_months": 33
  },
  "prior_roles": [
    {
      "title": "Software Engineer",
      "employer": "PayPal",
      "start_date": "2019-06",
      "end_date": "2023-07",
      "tenure_months": 49
    }
  ],
  "location": {
    "city": "Dallas",
    "state_or_region": "TX",
    "country": "US"
  },
  "disclosed_skills": ["Go", "AWS", "Postgres", "payment systems"],
  "work_authorization": "US-citizen"
}
```

---

## Schema validation

The skill validates incoming records before running Mode 2. Validation failures:

- **Missing required field for declared tier** → downgrade tier and proceed; note the gap.
- **Suspicious field content** (e.g., a `current_role.title` that looks like a name) → flag and ask for clarification.
- **Banned field present** (e.g., `age`, `birthdate`, `gender`) → reject the record and surface a compliance warning to the orchestrator. Do not proceed with Mode 2.

The orchestrator should treat schema validation errors as actionable feedback, not silent failures.
