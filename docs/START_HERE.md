# PYRINTU — START HERE

Welcome to the Pyrintu company workspace.

This repository is the working source of truth for building Pyrintu from zero to production.

## What Pyrintu is

Pyrintu is an AI-native social relationship platform focused on helping compatible people move from first connection to mutually invested real-world relationships.

Core product principles:

- Mutuality over superficial matching.
- Real-world outcomes over screen-time metrics.
- Relationship continuity over one-time interactions.
- Safety and trust over engagement.
- AI assists and orchestrates; it does not invent facts or silently make consequential decisions.

## Read these documents in this order

### 01 — Company + Product Foundation
`docs/MASTER_SPECIFICATION_V1.md`

This is the current master specification. It contains the company mission, target user, problem, product boundaries, Mutuality Engine™, Relationship Momentum™, V1 scope, trust principles, AI principles, north-star metric, and product success definition.

### 02 — Market Presence
`docs/MARKET_PRESENCE_STRATEGY_V1.md`

This describes how Pyrintu will eventually establish a presence in India: brand, website, SEO, social, communities, PR, analytics, and city-by-city growth.

Important: marketing launch is deliberately later than core product validation.

### 03 — UX Specification
`docs/UX_SPECIFICATION_V1.md`

This will define the product screen-by-screen. It is the next active workstream.

It will include first-time-user guided onboarding, highlighted actions, empty states, errors, safety states, AI behavior, and acceptance criteria.

## Build order

```text
01. Foundation / Master Specification        DONE
02. Market Presence Strategy                 DONE
03. UX Specification                         NEXT
04. System Architecture
05. Database Schema + API Contracts
06. Development Environment
07. Core MVP
08. Mutuality Engine™
09. Relationship Momentum™
10. Safety + Trust
11. Analytics + Admin
12. AI Evaluation + Testing
13. Staging
14. Private Beta
15. First Real Users
16. Public Launch
17. SEO + Social + PR at scale
18. Monetization refinement
19. India city expansion
20. Scale
```

## First-time-user experience requirement

Pyrintu V1 must include a guided first-time experience.

The guide will:

1. Explain what Pyrintu does in plain language.
2. Highlight the exact UI element the user should interact with.
3. Explain why that action matters.
4. Allow the user to complete the action immediately.
5. Progress only after the required action is completed or the user skips it.
6. Avoid overwhelming the user with a long tour.
7. Reappear contextually for important features that were not used.
8. Never block safety-critical controls such as Report, Block, Leave Group, or emergency/safety help.
9. Respect accessibility preferences and reduced-motion settings.
10. Persist onboarding progress so the user can resume after leaving the app.

Example:

**Step 1 — Tell Pyrintu about you**

Highlight: `Create your profile`

Message: `This helps Pyrintu understand the kinds of people and experiences that may fit you.`

**Step 2 — Tell us what you want**

Highlight: `Create an Intent`

Message: `Describe the kind of connection or experience you want in your own words.`

**Step 3 — Review your opportunity**

Highlight: `View Match`

Message: `See why Pyrintu thinks this person or group could work for you.`

**Step 4 — Check mutuality**

Highlight: `Continue`

Message: `A match only matters when both people want to invest in the connection.`

The exact copy, timing, triggers, skip behavior, accessibility, analytics events, and implementation details will be defined in the UX Specification.

## AI coding rule

No AI coding agent should invent architecture, product behavior, database fields, API contracts, or security rules.

Every implementation task must reference the current specification and have explicit acceptance criteria.

## Definition of a healthy build step

A step is complete only when:

- the requirement is documented;
- the implementation matches the requirement;
- tests cover the expected behavior;
- edge cases are considered;
- the result is reviewed;
- the repository remains reproducible.
