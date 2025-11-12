build a complete GitHub sourcing and candidate scoring application based on the following specifications.

##Project Overview
Build a GitHub Sourcing Tool that:
Allows users to find candidates based on specific technical skills (e.g., React, Python, ML, etc.).
Rates and ranks GitHub profiles and repositories intelligently using metadata such as:
Number of followers and stars.
Repo activity (commits, frequency, issues, PRs).
Language and technology relevance.
Project documentation quality and recency.
project security analysis and github scores
Generates personalized outreach messages for selected candidates.
Optionally enriches candidate data using enrichment APIs (Clay, Crunchbase, Clearbit, etc.).
All API keys (GitHub, enrichment tools) should be input dynamically per session, stored in-memory only, and never exposed in frontend or persisted in storage.

##Technical Requirements
Framework: Next.js 16 (App Router)
Language: TypeScript
Frontend: React + Tailwind CSS + ShadCN/UI components
API Layer: Next.js API Routes
Auth & Session: NextAuth.js (optional for managing sessions)
Data Fetching: GitHub REST & GraphQL APIs
AI Scoring: Use OpenAI or Claude API for repo evaluation & personalized outreach
Enrichment: Optional Clay / Crunchbase API (via dynamic API key input)
Security:
Hide and securely handle API keys using environment variables or temporary in-memory session storage.
Never log or expose user-provided keys.
Input Interface:
Skill search box (multi-select)
Optional keyword filters (location, followers count, stars, etc.)
API key input fields (hidden once entered)
Search button to trigger candidate sourcing
Output Interface:
Candidate list (name, GitHub link, top repositories, skill relevance score)
Repo rating summary (activity, stars, quality score)
“Generate Outreach” button → AI-generated message
“Enrich Data” button (optional if enrichment APIs are connected)

##Acceptance Criteria
Functional UI allowing:
Dynamic API key entry (hidden post-input)
Skill-based search and candidate listing
Repo scoring and ranking visualization
Personalized outreach generation for 10–15 candidates
Backend Integration:
GitHub API query by skill keywords.
AI model for scoring (e.g., via Claude/OpenAI).
Optional enrichment API integration.
Performance:
Fast response time (use async calls and caching if needed).
Security:
No persistent storage of user data or keys.
Code Quality:
Modular, commented, and production-ready.
Proper error handling for all API responses.

##Additional Guidance
Generate natural, personalized outreach messages that mention:
Candidate’s name or handle
Reference to their best repo or contribution
Specific skill match
Friendly, non-generic tone

