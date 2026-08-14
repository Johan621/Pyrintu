# PYRINTU — MASTER SPECIFICATION v1.0

**Status:** Draft for implementation planning  
**Document role:** Single source of truth for product and engineering decisions  
**Company:** Pyrintu  
**Initial market:** Hyderabad, India

---

## 0. Executive Summary

Pyrintu is an AI-native social relationship platform whose purpose is to help people build meaningful real-world relationships. The product is not designed around infinite discovery, swiping, or engagement for its own sake. It is designed around a measurable progression:

**Understand → Match → Mutuality → Experience → Relationship → Repeat**

The central product innovation is the **Mutuality Engine™**, which evaluates not only compatibility but also reciprocal willingness to invest in a connection. A second core system, **Relationship Momentum™**, helps a successful connection continue through future shared experiences.

The initial launch scope is intentionally narrow: Hyderabad, young adults roughly 18–30, small-group activity-based social experiences, and a high-quality controlled activity catalogue.

This specification is intentionally product-first. Exact implementation details, model selection, numerical weights, and infrastructure choices are not frozen until their corresponding engineering specifications are approved.

---

# 1. Company Foundation

## 1.1 Mission

> Help people build meaningful real-world relationships—not merely discover more people.

## 1.2 Product promise

> Pyrintu helps compatible people move from first connection to genuine, mutually invested relationships.

## 1.3 Category

AI-native social relationship platform.

## 1.4 Initial geography

Hyderabad, India.

## 1.5 Initial audience

Students, fresh graduates, and young professionals approximately 18–30 years old who want meaningful social connections and prefer small, activity-based interactions.

## 1.6 What Pyrintu is not

Pyrintu is not a dating-first application, traditional social-media feed, swipe-first engagement product, generic event listing site, generic messaging app, generic AI assistant, or popularity/follower platform.

---

# 2. Problem Definition

The core problem is the gap between **finding compatible people** and **building a lasting relationship**.

A social product can succeed at matching while users still experience:

- conversations that die before a plan is made;
- plans that never happen;
- first meetings with no follow-up;
- one-sided effort;
- good connections disappearing because schedules or coordination fail;
- too many low-quality options and too little confidence in which connection is worth pursuing.

Pyrintu is designed around the entire relationship-formation loop rather than only discovery.

---

# 3. Product Principles

## 3.1 Outcome over engagement

Optimize for meaningful relationship outcomes, not maximum screen time.

## 3.2 Mutuality over popularity

A connection should not be valued because of likes, followers, or message volume. Reciprocal willingness and healthy follow-through matter more.

## 3.3 Quality over volume

The product should prefer a small number of high-confidence opportunities over an infinite stream of profiles.

## 3.4 Real life over feed consumption

The central value is created when people interact meaningfully in the real world.

## 3.5 Safety over growth

No growth mechanism may knowingly compromise user safety or privacy.

## 3.6 AI must be grounded

The system must not invent users, availability, locations, events, compatibility evidence, or other facts.

## 3.7 Human control

AI recommends and orchestrates; users remain in control of consequential social decisions.

## 3.8 Minimum necessary data

Only information necessary for the experience should be collected and exposed.

---

# 4. Core Product Systems

## 4.1 Mutuality Engine™

### Objective

Determine whether a potential connection is not only compatible but mutually actionable.

### Conceptual signal groups

- interest compatibility;
- activity compatibility;
- availability overlap;
- group-size preference;
- location compatibility;
- budget compatibility;
- explicit willingness;
- response consistency;
- plan acceptance;
- follow-through;
- reciprocal initiative;
- post-experience willingness to continue.

The exact mathematical model and feature weights are deliberately not frozen in this document.

### Principle

> Compatibility without mutual willingness is weak value.

---

## 4.2 Relationship Momentum™

### Objective

Convert a successful initial connection into repeated, mutually wanted interaction.

### Conceptual progression

1. Connection created.
2. Interaction occurs.
3. Both parties provide feedback.
4. Both parties indicate whether continuation is wanted.
5. Pyrintu identifies compatible future opportunities.
6. Repeat interaction occurs.
7. Reciprocal relationship strength increases.

### Important behavior

Pyrintu should distinguish among:

- genuine mutual interest;
- one-sided pursuit;
- temporary scheduling conflict;
- low engagement;
- healthy ongoing relationship.

The system must not pressure users into unwanted contact.

---

## 4.3 Group Intelligence

Pyrintu should eventually optimize **group compatibility**, not only pair compatibility.

Target V1 group size: approximately 3–6 people.

A strong group should balance:

- compatible interests;
- compatible activity preferences;
- overlapping availability;
- compatible social-energy preferences;
- geographic practicality;
- group-size preferences;
- budget;
- safety constraints.

The exact optimization algorithm is a separate engineering specification.

---

## 4.4 Activity Orchestration

Initial activities should come from a controlled catalogue rather than an unrestricted marketplace.

Initial categories may include:

- café meetup;
- walk;
- badminton;
- bowling;
- board games;
- photography walk;
- study session;
- coding/startup discussion.

The activity is a mechanism for relationship formation, not the core marketplace product.

---

# 5. V1 User Journey

## 5.1 Landing

User understands the proposition immediately:

> Build real connections through experiences that actually happen.

Primary CTA: create account / join.

## 5.2 Account creation

Initial requirements:

- email and/or phone verification;
- age eligibility;
- consent to terms and privacy policy;
- basic safety acknowledgement.

## 5.3 Onboarding

Collect structured and natural-language information needed for matching.

Potential inputs:

- interests;
- preferred activities;
- availability;
- approximate area;
- group-size preference;
- social environment preference;
- budget range;
- language preference;
- connection goal.

Avoid unnecessary personal data collection.

## 5.4 Intent creation

User should be able to express a natural-language social goal.

Example:

> I recently moved to Hyderabad. I like badminton and startups. I want to meet a few people this weekend, something relaxed, under ₹500.

The system converts this into structured intent without requiring the user to understand the internal schema.

## 5.5 Candidate and group discovery

Pyrintu surfaces a small number of high-confidence opportunities.

No infinite swipe feed is part of the V1 product philosophy.

## 5.6 Mutuality confirmation

Before a connection becomes an active social plan, Pyrintu should evaluate whether there is genuine reciprocal willingness to participate.

## 5.7 Group formation

Pyrintu creates a small group where appropriate and explains why the group is a reasonable fit without exposing private scoring details.

## 5.8 Activity recommendation

Recommend a feasible activity using group preferences, timing, geography, and budget.

## 5.9 Confirmation

All participating users explicitly confirm the plan.

## 5.10 Group interaction

The group receives a private chat and practical coordination tools. AI may provide contextual icebreakers and planning support.

## 5.11 Post-experience feedback

Each member independently provides feedback such as:

- Did the experience happen?
- Did it feel comfortable?
- Would you meet this person/group again?
- What worked?
- What should change?

## 5.12 Relationship continuation

If mutual continuation is indicated, Pyrintu may recommend another activity or recurring circle.

---

# 6. V1 Functional Requirements

## Identity & account

- Account creation.
- Verification.
- Login/logout/session management.
- Account recovery.
- Age eligibility handling.

## Profile

- Interests.
- Activities.
- Availability.
- Social preferences.
- Language preferences.
- Approximate location.
- Privacy controls.

## Intent

- Create natural-language intent.
- Edit intent.
- Expire intent.
- View active opportunities.

## Matching

- Candidate generation.
- Compatibility scoring.
- Mutuality evaluation.
- Group formation.
- Explanations grounded in known profile signals.

## Groups

- Group creation.
- Invitation/acceptance.
- Group chat.
- Group status.
- Leave group.
- Report group/member.

## Activities

- Controlled activity catalogue.
- Activity recommendations.
- Scheduling.
- Approximate location selection.
- Confirmation state.

## Relationship continuity

- Post-meet feedback.
- Reconnect recommendation.
- Recurring circle creation later in V1/V1.5 depending validation.

## Safety

- Report.
- Block.
- Leave.
- Moderation queue.
- Incident status.

## Notifications

- Match/opportunity notification.
- Group invitation.
- Confirmation reminder.
- Event reminder.
- Feedback request.
- Safety/security notifications.

---

# 7. Explicitly Out of Scope for First MVP

- dating-first features;
- public social feed;
- creator monetization;
- large event marketplace;
- open activity marketplace;
- nationwide launch;
- native mobile apps before product validation;
- complex subscriptions before value validation;
- advertising;
- public relationship scores;
- public popularity rankings.

---

# 8. Trust & Safety

## 8.1 Principles

Safety must be a product-level system, not a support afterthought.

## 8.2 Initial controls

- account verification;
- block;
- report;
- leave group;
- moderation;
- privacy controls;
- limited location exposure;
- abuse/spam controls;
- safety escalation;
- community guidelines.

## 8.3 Sensitive data

Safety reports and private relationship signals require stricter access control than normal profile data.

## 8.4 AI safety

AI must not:

- fabricate evidence;
- infer sensitive personal attributes unnecessarily;
- reveal private relationship data;
- pressure a user to continue an unwanted relationship;
- bypass deterministic safety rules.

---

# 9. AI System Principles

AI components must use a layered architecture:

**LLM reasoning + deterministic rules + structured state + safety controls + evaluation**

Candidate roles:

### Intent Agent
Natural language → structured intent.

### Match Reasoner
Explain compatible signals and identify conflicts.

### Group Architect
Construct and rank group candidates.

### Activity Planner
Recommend practical experiences.

### Conversation Helper
Generate contextual, non-manipulative icebreakers.

### Relationship Agent
Recommend healthy continuation when mutuality supports it.

### Safety Agent
Assist moderation and abuse/spam triage.

AI should not be allowed to invent facts or silently override system state.

---

# 10. AI Evaluation Requirements

Every production AI capability must have:

- golden test cases;
- regression tests;
- structured output validation;
- confidence/uncertainty behavior;
- safety test cases;
- prompt/model version tracking;
- cost and latency measurement;
- human review path for uncertain or high-impact outputs.

A feature is not production-ready because the model returns plausible text.

---

# 11. Product Analytics

Core event taxonomy should include:

- signup;
- onboarding_complete;
- intent_created;
- candidate_viewed;
- match_offered;
- match_accepted;
- mutuality_confirmed;
- group_created;
- activity_selected;
- activity_confirmed;
- meetup_completed;
- feedback_submitted;
- second_interaction;
- circle_created;
- retained_30d;
- report_created;
- block_created.

The analytics implementation must respect privacy requirements and data minimization.

---

# 12. North-Star Metric

Proposed north-star concept:

> **Meaningful Relationship Creation**

The exact threshold defining a meaningful relationship must be validated and specified before public KPI reporting.

Supporting metrics:

- match → first interaction;
- first interaction → meetup;
- meetup → second interaction;
- reciprocal initiation;
- group recurrence;
- 30-day relationship retention;
- safety incident rate;
- user satisfaction.

Do not optimize V1 around DAU or session length alone.

---

# 13. Business Model Direction

Business model is intentionally not fully frozen before validation.

Possible future mechanisms include:

- premium membership;
- premium matching/continuity features;
- curated experiences;
- community products;
- organizational/community partnerships.

Pricing must be validated rather than assumed.

---

# 14. System Architecture Direction

Recommended initial architecture is a modular monorepo with clear service boundaries.

Conceptual components:

- Web client;
- Admin client;
- API service;
- Matching service;
- AI service;
- Moderation service;
- Notification service;
- PostgreSQL;
- Redis where required;
- shared types/validation/UI packages;
- observability and evaluation infrastructure.

The architecture should remain modular without premature microservice complexity.

---

# 15. Engineering Principles

## Contract-first

Product requirements are translated into explicit technical contracts before implementation.

## Small changes

AI coding tasks must be limited in scope and independently testable.

## Type safety

Shared domain types and validation schemas must be centralized.

## Deterministic business rules

Important business logic must not exist only inside prompts.

## Observability

Production behavior must be inspectable through logs, metrics, traces, and audit events where appropriate.

## Reversible changes

Database migrations, feature flags, and deployment practices should support safe rollback.

## Security by design

Authentication, authorization, validation, secrets, and rate limiting are part of the architecture.

---

# 16. Repository Operating Model

Suggested monorepo:

```text
pyrintu/
├── apps/
│   ├── web/
│   └── admin/
├── services/
│   ├── api/
│   ├── matching/
│   ├── ai/
│   ├── moderation/
│   └── notifications/
├── packages/
│   ├── types/
│   ├── ui/
│   ├── config/
│   └── validation/
├── database/
├── docs/
├── tests/
│   ├── unit/
│   ├── integration/
│   ├── e2e/
│   ├── ai-evals/
│   └── security/
├── infrastructure/
├── company/
├── .github/
└── README.md
```

This is an initial foundation, not a requirement to implement every directory immediately.

---

# 17. Development Environments

Minimum environment model:

- development;
- staging;
- production.

No production deployment should depend on local-only configuration.

---

# 18. CI/CD Minimum

Before production:

- lint;
- type checking;
- unit tests;
- integration tests;
- migration checks;
- build verification;
- security checks;
- AI evaluation suite where applicable.

Deployment must support rollback.

---

# 19. Definition of Done

A feature is done only when:

1. Requirement is documented.
2. UX behavior is defined.
3. Technical contract is defined.
4. Implementation is complete.
5. Tests pass.
6. Security implications are reviewed.
7. Analytics events exist where appropriate.
8. Failure/edge cases are handled.
9. Documentation is updated.
10. Acceptance criteria are satisfied.

“Code generated successfully” is not a completion criterion.

---

# 20. AI Coding Rules

AI coding tools must:

- read the current specification before implementation;
- never invent unspecified architecture;
- never silently change APIs or database contracts;
- write tests with implementation where appropriate;
- report assumptions explicitly;
- preserve existing conventions;
- avoid unnecessary dependencies;
- avoid broad refactors during focused tasks;
- never claim a feature works without verification.

Recommended coding loop:

**spec → task → implementation → tests → review → merge**

---

# 21. Product Validation Gate

Before a large V1 build, Pyrintu must validate the core thesis in the target market.

Minimum research questions:

- Do people experience the stated relationship-formation problem?
- Do they want small-group real-world experiences?
- Does mutuality-based matching improve outcomes?
- Will users return after a successful connection?
- What safety concerns prevent participation?
- What is the smallest compelling experience?

Validation evidence must be documented in `company/market-research/`.

---

# 22. Current Status

### Locked

- Mission.
- Product category.
- Initial geography.
- Initial audience.
- Core product principle.
- Mutuality Engine™ concept.
- Relationship Momentum™ concept.
- V1 user loop.
- Trust philosophy.
- AI philosophy.
- Core scope boundaries.

### Open for specification

- Exact matching formula.
- Exact mutuality scoring methodology.
- Exact relationship momentum model.
- UI wireframes.
- Database schema.
- API contracts.
- AI model/vendor selection.
- Pricing.
- Launch criteria.
- Quantitative validation thresholds.

---

# 23. Change Control

Any change to the locked product thesis requires:

1. written rationale;
2. impact analysis;
3. update to this specification;
4. review of dependent technical documents;
5. explicit version increment.

The purpose is to prevent AI-assisted development from drifting the company away from its core thesis.

---

# 24. Next Deliverables

1. `docs/product/UX_SPECIFICATION_V1.md`
2. `docs/engineering/ARCHITECTURE_V1.md`
3. `docs/engineering/DATABASE_SPECIFICATION_V1.md`
4. `docs/engineering/API_CONTRACT_V1.md`
5. `docs/engineering/AI_SPECIFICATION_V1.md`
6. `docs/engineering/SAFETY_SPECIFICATION_V1.md`
7. `docs/product/DESIGN_SYSTEM_V1.md`
8. `docs/product/ROADMAP_V1.md`
9. `docs/company/GO_TO_MARKET_V1.md`
10. `docs/engineering/AI_CODING_RULES.md`

These documents must be derived from this master specification.
