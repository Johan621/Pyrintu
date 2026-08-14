# PYRINTU — UX SPECIFICATION
## Screen 10 — Discovery / Opportunities v1.0

**Status:** Approved / ready to lock

## Core Objective

Help the user discover a small set of relevant, realistic opportunities based on:

`Profile + Social Preferences + Availability + Current Intent + Confirmed AI interpretation + Opportunity constraints + Safety rules`

Discovery is opportunity-first, not feed-first. Pyrintu should surface a small number of genuinely relevant opportunities rather than maximizing scrolling.

## Opening Experience

### Heading

`A few opportunities that fit what you're looking for.`

### Supporting text

`Pyrintu focuses on quality over endless options. Here are the opportunities that currently look most relevant to your intent.`

## Current Intent Context

Show the active intent in a compact context bar.

Example:

`Looking for: Badminton + new people | This weekend | Hyderabad | Small group`

Action:

`Edit intent`

Discovery must remain connected to the user's current request.

## Discovery Header

Recommended structure:

`Your current intent`

`3 opportunities worth considering`

Avoid quantity-driven labels such as `247 matches found`.

## Opportunity Card

Each opportunity should feel like a real possibility, not a generic recommendation card.

Example information:

- Sunday · 6:30 PM
- Badminton + Café
- 4 people
- Relaxed environment
- Hyderabad
- ₹350 estimated, when relevant
- Current formation status

Primary action:

`View opportunity`

## Essential Card Information

Each card should contain, where applicable:

### When

Example: `Sunday · 6:30 PM`

### What

Example: `Badminton + Café`

### Group size

Example: `4 people`

### Location context

Example: `Hyderabad` or a relevant area.

### Estimated cost

Example: `₹350 estimated`

### Opportunity status

Examples:

- `4/4 spots forming`
- `3/5 interested`
- `Waiting for one more person`

Do not use manipulative scarcity language such as `Hurry! Only 1 spot left!`.

## Why This Fits

Every meaningful recommendation should provide:

### `Why this fits you`

Example:

- `Badminton` matches an activity you enjoy.
- `Small group` matches your preferred group size.
- `Sunday evening` fits your availability.
- `Relaxed environment` matches your current intent.

Reasoning must reference actual user-provided or system-grounded signals.

## Match Score Boundary

An internal numerical score may exist, but it must not be the primary user-facing experience.

Avoid primary presentation such as `91% Match` because it creates false precision.

Prefer:

- `Strong fit`
- `Good fit`
- `Very relevant to your intent`

Detailed reasoning belongs to the later Match Details / Match Reasoning experiences.

## Opportunity Quality

An opportunity should only appear when it clears a minimum quality threshold.

Conceptually:

`Intent fit + Availability fit + Social fit + Realistic formation + Safety eligibility = Discovery candidate`

If an opportunity fails an essential constraint, do not promote it merely to fill the screen.

## Ranking Principles

Prioritize:

1. Relevance — how well the opportunity fits the current intent.
2. Feasibility — whether it can realistically happen given availability and constraints.
3. Mutuality potential — whether enough participants have compatible willingness.
4. Safety eligibility — whether the opportunity satisfies current safety rules.
5. Freshness — whether the opportunity is still current.

The exact ranking algorithm belongs to technical architecture.

## Freshness

Opportunities must not remain visible after they become stale.

Possible states:

- `Starts in 2 hours`
- `Opportunity expired`

Expired opportunities should disappear from active discovery where possible, or clearly show their inactive state if the user is already viewing them.

## Opportunity States

An opportunity can be:

- Forming
- Ready
- Almost ready
- Full
- Expired
- Unavailable

### Forming

Participants are still being assembled.

### Ready

All required conditions are satisfied.

### Almost ready

Close to becoming actionable.

### Full

Capacity is reached.

### Expired

Relevant time window passed.

### Unavailable

Opportunity can no longer be accepted.

## Commitment Boundary

Discovery should not force commitment.

Primary card action:

`View opportunity`

Do not use `Accept Now` as the default card action.

Viewing does not imply commitment.

## Secondary Actions

Where appropriate:

- Save
- Not interested
- Hide similar opportunities

These actions should remain lightweight.

## Not Interested

When selected:

`Not interested in this opportunity?`

Optional reasons:

- Wrong timing
- Wrong activity
- Group too large
- Too far
- Too expensive
- Environment doesn't fit
- Something else

Users may dismiss without providing a reason.

## Learning From Dismissal

Dismissal may improve future ranking, but one rejection must not automatically rewrite permanent user preferences.

Example:

Rejecting one badminton event because it is too expensive must not imply that the user dislikes badminton.

Keep event-specific feedback separate from stable profile preferences.

## Current Intent Overrides

If the active intent conflicts with an existing preference, discovery should reflect the current intent context where the product allows an override.

Example:

`This opportunity is larger than your usual group preference because your current intent allows a networking event.`

Show the relationship clearly when it materially affects the recommendation.

## Opportunity Diversity

Do not show many nearly identical opportunities.

When multiple high-quality options exist, provide meaningful diversity where possible:

- Activity-first vs conversation-first
- Different area
- Different time
- Different group composition
- Different relevant cost level

The goal is meaningful choice, not repetition.

## Why Not This?

When useful, explain lower prominence without exposing proprietary ranking logic.

Example:

`This one isn't shown near the top because it doesn't fit your availability as well.`

Keep explanations human and grounded.

## Empty State — No Opportunities

### Heading

`Nothing looks right just yet.`

### Supporting message

`Your current intent is clear, but we don't have an opportunity that meets your important preferences right now.`

Actions:

- Adjust intent
- Expand flexibility
- Try another time
- See what could work

Do not show `No matches found` as the only response.

## No-Opportunity Recovery

Example strict intent:

`Saturday 7 PM + badminton + small group + ₹300 maximum`

If nothing qualifies:

`Nothing currently fits all of those conditions.`

Then offer transparent relaxations such as:

- Saturday afternoon
- ₹500 budget
- More flexible group size

Each option must show what would change before the user accepts it.

## Relaxation Safeguards

Pyrintu must never silently relax the user's constraints.

Bad:

`User says ≤ ₹300 → system shows ₹900 opportunity`

Good:

`We couldn't find one under ₹300. There is a strong option around ₹450 if you're open to expanding the budget.`

Actions:

- See it
- Keep my limit

## Broadening Discovery

When the user chooses to expand flexibility, show exactly what changes.

Example:

`Current: Saturday evening`

`Expanded: Saturday afternoon or evening`

Expansion applies to discovery unless the user explicitly changes a permanent preference elsewhere.

## Discovery Filters

Keep filters lightweight:

- Time
- Activity
- Area
- Group size
- Budget
- Environment

A filter is a temporary discovery control unless explicitly saved elsewhere.

## Natural-Language Discovery Refinement

Allow users to refine without opening a complex filter panel.

Example:

`Show me something similar but quieter and closer to Gachibowli.`

Pyrintu may interpret this into:

- Environment → Quieter
- Location → Gachibowli

The user must be able to review or reject the refinement.

AI must not mutate permanent profile or social-preference data as a side effect.

## How Discovery Chooses Opportunities

Provide a compact explanation:

`We consider your current intent, preferences, availability, realistic timing, and safety requirements.`

This should be accessible without leaving discovery.

## AI Behavior

AI may:

- summarize why an opportunity fits
- understand natural-language refinement
- explain trade-offs
- suggest alternatives
- identify meaningful differences between opportunities

AI must not:

- fabricate participant information
- fabricate availability
- claim an opportunity is confirmed when it is not
- invent prices
- invent venue details
- override safety constraints
- imply mutuality that has not actually been established

## Mutuality Signal

Discovery may show a limited mutuality indicator only when supported by actual system state.

Examples:

`People in this opportunity are independently interested in meeting.`

`3 participants have confirmed interest.`

Never claim:

`Everyone wants to meet you`

unless that exact claim is supported by a verified product state.

## Participant Privacy

Discovery should minimize personal information.

Opportunity cards may show:

`4 people`

and, where useful:

`Shared interests: badminton, startups`

Detailed participant identities belong to later screens and should be disclosed only when appropriate.

## Safety Status

Possible lightweight indicator:

`Safety requirements met`

or:

`Additional verification may be required`

Do not expose internal risk scoring.

## Opportunity Formation

Some opportunities may still be forming.

Example:

`3 people interested · one more needed`

Action:

`View opportunity`

Viewing or expressing interest does not automatically confirm a meetup.

## Expressing Interest

If the user chooses:

`I'm interested`

the state becomes:

`Viewed → Interested → Waiting for mutual formation`

The UI must explicitly distinguish interest from meetup confirmation.

## After Interest

Message:

`You're interested. We'll let you know if this opportunity forms enough mutual interest to move forward.`

This is the entry point into the later Mutuality Flow.

## Undo Interest

Action:

`Remove interest`

Confirmation, when needed:

`Remove your interest from this opportunity?`

Actions:

- Remove
- Keep

No guilt-based language.

## Discovery Refresh

Opportunities may change due to:

- availability changes
- participant changes
- activity changes
- expiration
- new compatible opportunities

Indicate material changes such as:

`New opportunities are available`

Do not silently reshuffle the entire list without preserving user context.

## Ranking Labels

Avoid internal ranking language such as `Rank #1`.

Prefer useful labels backed by real state:

- Strong fit
- Very relevant to your intent
- New
- Time-sensitive
- Good alternative

## Loading State

Initial loading:

`Finding opportunities that fit…`

Optional staged states, only when they represent actual system stages:

```text
Checking your intent
↓
Checking availability
↓
Finding compatible opportunities
↓
Preparing your options
```

Do not fabricate progress.

## Error State

### Discovery service failure

`We couldn't load your opportunities right now.`

Actions:

- Try again
- View your intent

### Partial result failure

`Some opportunities couldn't be loaded.`

Action:

`Retry`

Do not discard successfully retrieved results unnecessarily.

## Stale-State Recovery

If an opportunity expires while the user is viewing it:

`This opportunity is no longer available.`

Action:

`Find similar opportunities`

Preserve the user's active intent rather than forcing them to start over.

## First-Time Guidance

### Guide 05 — Discovery

**Target:** Opportunity card

**Message:** `These aren't generic matches. Each opportunity is built around what you're looking for right now.`

### Guide 06 — Why This Fits

**Target:** `Why this fits`

**Message:** `Pyrintu shows the actual signals behind an opportunity so you can decide for yourself.`

Guidance is contextual and dismissible.

## Accessibility Requirements

- semantic card structure
- keyboard-accessible cards
- clear headings
- screen-reader labels for opportunity state
- `Why this fits` accessible without hover
- filters keyboard accessible
- no color-only opportunity status
- live announcement when new opportunities arrive
- accessible dismissal
- reduced-motion support
- sufficient contrast
- touch-friendly controls

Example screen-reader description:

`Badminton and café. Sunday 6:30 PM. Four people. Strong fit. Why this fits button. View opportunity button.`

## Responsive Behavior

### Mobile

Priority:

`Current intent → Top opportunity → Why this fits → Additional opportunities → Refine`

Use vertically stacked cards.

### Desktop

Possible layout:

`Current intent + filters | Opportunity list`

The information hierarchy must remain equivalent.

## Analytics Events

- discovery_viewed
- discovery_loaded
- discovery_load_failed
- opportunity_impression
- opportunity_viewed
- why_this_fits_viewed
- opportunity_saved
- opportunity_not_interested
- not_interested_reason_selected
- discovery_filter_opened
- discovery_filter_changed
- natural_language_refinement_started
- natural_language_refinement_applied
- natural_language_refinement_rejected
- opportunity_interest_started
- opportunity_interest_confirmed
- opportunity_interest_removed
- opportunity_expired_viewed
- discovery_empty_state_viewed
- discovery_relaxation_viewed
- discovery_relaxation_accepted
- discovery_relaxation_rejected

Never send private participant details or raw intent text into generic analytics.

## Performance

- fast initial shell
- cached current intent
- incremental opportunity loading where useful
- do not block discovery on AI explanations
- responsive filtering
- no full-page reload
- graceful partial results

## Ranking Boundary

The UX describes what users experience, not the exact ranking formula.

Technical architecture should later define:

`Hard constraints → Eligibility → Opportunity generation → Ranking → Explanation`

The ranking system must be independently testable.

## Recommendation Integrity

Core Pyrintu rule:

`Never recommend something just because the screen looks empty.`

No artificial filler.

If only one genuinely relevant opportunity exists, show one.

If none exist, say so honestly.

## Anti-Addiction / Anti-Dark-Pattern Requirements

Discovery must not use:

- infinite scrolling
- deceptive notification badges
- countdown timers designed to create panic
- fake scarcity
- `people are waiting for you` without factual basis
- forced swiping loops
- endless recommendation loading
- hidden rejection controls

The goal is successful connection, not time spent in discovery.

## Matching Boundary

Discovery does not perform the user's final matching decision. It presents eligible opportunities based on validated signals and constraints.

Conceptually:

`Profile + Social Preferences + Availability + User Intent + Confirmed AI interpretation → Discovery / Opportunities`

The later Match Details, Match Reasoning, and Mutuality experiences take the workflow forward.

## Acceptance Criteria

### Relevance

- Opportunities reflect the active intent.
- Important preferences are respected.
- Availability is considered.
- Safety eligibility is respected.

### Explainability

- Every promoted opportunity has understandable reasoning.
- Signals come from actual user data or verified system state.
- No fake precision.

### Trust

- No fabricated participants.
- No fabricated availability.
- No fake mutuality.
- No invented pricing.

### Choice

- User can inspect before expressing interest.
- Interest is not meetup confirmation.
- User can remove interest.

### Flexibility

- User can refine discovery.
- Relaxing a constraint requires explicit consent.

### Quality

- No filler opportunities.
- Stale opportunities are handled clearly.

### Accessibility

- Cards and controls are keyboard accessible.
- Screen-reader descriptions are meaningful.

### Privacy

- Participant information is minimized.
- Full intent is not automatically exposed.

## Final Intended Experience

```text
"These aren't random people."
        ↓
"This actually makes sense for what I want right now."
        ↓
"I can see why Pyrintu thinks it fits."
        ↓
"I decide whether to explore it."
```

## Lock Note

Screen 10 was reviewed and explicitly approved in product discussion. It is now locked as a UX contract on `feature/ux-screen-10`; implementation remains separate from the UX specification.
