# PYRINTU — UX SPECIFICATION V1.0
## Screen 11 — Match Details

**Status:** Approved / locked UX contract

## Purpose

Turn a Discovery opportunity into a clear, trustworthy, inspectable potential connection. The user should understand what is happening, who is involved, why Pyrintu brought the opportunity together, what is known versus still proposed, and what action means without feeling committed by simply viewing the screen.

## Core flow

`What is happening → Who is involved → Why this exists → Shared signals → Differences → What happens next → User decides`

## Opening experience

**Heading:** `This could be a good fit.`

**Supporting text:** `Here's the opportunity, the people involved, and why Pyrintu brought it together.`

Show an actual opportunity-state badge such as `Forming` or `Ready`.

## Opportunity summary

Show immediately:

- date/time or honest time range
- activity
- broad location
- group size
- estimated cost when relevant
- current opportunity state

Primary actions:

- `View plan`
- `I'm interested`

Secondary:

- `Not interested`
- `Save opportunity`

Explicitly state: viewing does not commit the user. `I'm interested` means the user wants Pyrintu to continue exploring the opportunity; it is not meetup confirmation.

## Why Pyrintu brought this together

Show evidence-based reasons such as:

- activity matches an expressed interest
- group size matches a social preference
- timing fits availability
- environment matches the current intent
- estimated cost fits the current intent budget

Do not use unsupported claims or arbitrary numerical match scores as the primary explanation.

## Match reasoning preview

Show a compact summary such as `Strong fit for your current intent` followed by a count of meaningful signals and any flexible difference. Provide `See full reasoning` to Screen 12 — Match Reasoning.

## Participant overview

Show relevant, permitted participant information only. Example fields may include display name, photo where permitted, relevant shared interests, broad location, and opportunity-relevant social context.

Never automatically reveal:

- exact address
- private contact information
- private availability
- hidden safety preferences
- unrelated profile information

## Why each person is relevant

Where useful, show evidence-based contextual summaries such as shared activity or interests. Never invent bios, traits, intentions, or personality claims.

## Shared interests

Show concrete shared signals such as badminton, startups, or cafés. Avoid turning these into a compatibility score.

## Differences

Show meaningful differences honestly. Example: the user prefers quieter spaces while the group selected a moderately lively café. Explain when the difference remains within the user's stated flexibility.

## Group composition

Show group size and, when useful, why that size was selected based on actual product logic. Do not fabricate social claims.

## Activity and connection objective

Separate the activity from the social objective.

Example:

**Activity:** Badminton

**Connection:** Meet people interested in startups and sports

## Proposed plan

Show planned stages and honest certainty:

- activity duration
- optional follow-on activity
- exact time only when confirmed
- `Proposed, not confirmed` when still tentative

## Location

Prefer broad location first, e.g. `Gachibowli, Hyderabad`. Do not reveal a precise meetup location prematurely. State when the exact venue will be confirmed later.

## Cost

Clearly distinguish `Estimated` from `Confirmed`. Never fabricate venue pricing.

## What is known vs not confirmed

Provide a trust section:

### What we know

- current intent
- availability
- shared interests
- group preferences

### What isn't confirmed yet

- exact venue
- final time
- final participant commitment

This section prevents predictions from being presented as facts.

## Mutuality preview

When supported by actual product state, show aggregate evidence such as `3 people have independently expressed interest.` When the opportunity is still forming, say so. Never claim that everyone wants to meet or expose individual decisions unnecessarily.

## Interest action

Before recording interest, explain:

`You're telling Pyrintu you'd like to explore this opportunity. You aren't confirming the meetup yet.`

After success:

**Heading:** `You're interested`

Supporting text: `We'll keep you updated if the opportunity reaches the next step.`

Allow `Remove interest`.

## Not interested

Provide optional lightweight reasons:

- timing
- activity
- group size
- location
- cost
- environment
- something else

Do not require a reason.

Dismissal feedback may improve future ranking but must not silently rewrite a permanent preference.

## Save

`Save opportunity` means save for later review, not reserve a place. The UI must make that distinction explicit.

## Safety preview

Provide a compact `Before you meet` section with practical guidance such as using a public place, reviewing the group, keeping contact details private until comfortable, and reporting or leaving if something feels wrong. Provide direct access to Safety Center.

Safety-critical controls must remain accessible, including `Report`, `Block`, and `Leave opportunity` where applicable. They must never be hidden by onboarding or AI UI.

## Trust indicators

Only show verifiable signals with defined meanings, such as `Identity verified` or `Profile completed`. Do not use vague labels like `Trusted Person` without an auditable definition.

## AI behavior

AI may:

- summarize why the opportunity fits
- explain shared signals
- summarize group composition using verified data
- answer questions about the opportunity from verified product data
- suggest useful questions the user may want to consider

AI must not:

- invent participant traits
- infer private details without evidence
- claim someone is interested when they are not
- claim a venue is confirmed when it is not
- expose private participant information
- make absolute safety guarantees

## Ask Pyrintu

Optional conversational control: `Want to know something about this opportunity?`

Examples:

- `Why did you include Meera?`
- `Why is this group four people?`
- `What makes this a strong fit?`

Answers must be grounded in actual product signals and may point the user to the corresponding page section. Never claim that two people will definitely get along.

## AI fallback

If the explanation assistant is unavailable, say:

`The explanation assistant isn't available right now.`

Core opportunity details remain fully usable. AI failure must never block the screen.

## Loading states

Examples:

- `Preparing the opportunity…`
- `Loading group details…`
- `Preparing why this fits…`

Avoid indefinite skeleton/loading states.

## Error states

### Opportunity unavailable

`This opportunity changed while you were viewing it.`

Actions: `Refresh opportunity`, `Find similar opportunities`

### Participant data unavailable

`Some group details aren't available right now.`

Action: `Retry`

### Save/interest failure

`We couldn't save that change.`

Action: `Try again`

## Stale opportunity recovery

If the opportunity expires while being viewed:

`This opportunity is no longer available.`

Supporting text: `Your intent is still active. Let's find another option that fits.`

Action: `Find another opportunity`

Preserve the user's intent.

## Privacy model

Use the minimum information necessary for the current opportunity:

`Relevant + Necessary + User-permitted = Visible information`

Do not expose private profile fields simply because the system can access them.

## Product boundary

Screen 11 does not:

- finalize mutuality
- confirm a meetup
- reveal private participant commitments
- permanently select a venue
- create the final activity plan
- establish a relationship

Its job is to prepare an informed decision about whether to continue.

## Connection to Screen 12

Screen 11 answers: `What is this opportunity?`

Screen 12 answers: `Why does Pyrintu think this is a fit?`

This separation keeps Match Details understandable rather than turning it into a technical scoring dashboard.

## Accessibility

- semantic page structure
- accessible participant cards
- keyboard-accessible actions
- reasoning sections available without hover
- lifecycle state announced to screen readers
- accessible safety actions
- no color-only status indicators
- focus preserved after dialogs
- reduced-motion support
- comfortable touch targets

Example accessible summary: `Opportunity status: forming. Four participants including you. View reasoning button.`

## Responsive behavior

### Mobile

`Opportunity summary → Why you're seeing this → People → Shared interests → Differences → Activity → Plan → Cost/location → Mutuality → Safety → Interest action`

### Desktop

Two-column composition is preferred where useful:

**Left:** opportunity, people, activity, plan

**Right:** why this fits, shared signals, mutuality, safety, CTA

## Analytics events

- `match_details_viewed`
- `match_details_participant_section_viewed`
- `match_details_shared_interests_viewed`
- `match_details_differences_viewed`
- `match_details_reasoning_preview_viewed`
- `match_details_plan_viewed`
- `match_details_safety_viewed`
- `match_details_ai_question_started`
- `match_details_ai_question_completed`
- `match_details_interest_started`
- `match_details_interest_confirmed`
- `match_details_interest_removed`
- `match_details_not_interested`
- `match_details_not_interested_reason`
- `match_details_saved`
- `match_details_unsaved`
- `match_details_expired`
- `match_details_error`

Never send private participant data or raw AI conversations into generic analytics.

## Performance

- opportunity summary loads immediately
- participant data may load progressively
- AI explanation may load asynchronously
- core opportunity data must not depend on AI
- no unnecessary navigation reloads
- preserve scroll position after transient errors

## Acceptance criteria

### Understanding

- User knows what the opportunity is.
- User knows who is involved.
- User understands the current lifecycle state.
- User knows what is confirmed and what is still proposed.

### Explainability

- Actual signals explain why the opportunity exists.
- Shared interests are evidence-based.
- Differences are visible where relevant.

### Privacy

- Participant information is minimized.
- Private preferences remain private.
- Exact location is not revealed prematurely.

### Mutuality

- Interest is separate from commitment.
- Mutuality claims are evidence-based.
- Individual decisions are not unnecessarily exposed.

### AI

- AI explains rather than invents.
- AI cannot override deterministic opportunity data.
- AI failure does not block the screen.

### Safety

- Report and Block remain accessible.
- Safety guidance is visible.
- No false safety guarantees.

### Reliability

- Stale opportunities recover gracefully.
- User intent is preserved.
- Save and interest failures are recoverable.

## Lock note

Screen 11 was explicitly approved in product review. This document is the canonical detailed UX contract for Screen 11. Implementation remains separate from UX specification and must not begin until the UX contract is merged and the technical implementation task is created.
