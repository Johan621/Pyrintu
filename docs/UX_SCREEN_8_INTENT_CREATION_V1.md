# PYRINTU — UX SPECIFICATION
## Screen 8 — Intent Creation v1.0

**Status:** Approved / ready to lock

## 1. Core Objective

Allow the user to express: `What kind of connection or experience am I looking for right now?`

Intent combines, where relevant:

- what
- who
- when
- where
- activity
- environment
- budget / constraints
- purpose

The user should not have to manually fill every field.

## 2. Opening Experience

### Heading

`What do you want right now?`

### Supporting text

`Tell Pyrintu in your own words. We'll help turn it into something actionable.`

### Reassurance

`You don't need to know exactly what you want yet.`

## 3. Primary Interaction

Large natural-language input.

Example placeholder:

`I'm new to Hyderabad, like badminton and startups, and want to meet a small group this weekend.`

Primary action: `Understand my intent`

Secondary action: `Build it manually`

Natural language is the easiest path, but structured controls remain available.

## 4. Profile vs Intent

`Your profile = you`

`Your intent = what you're looking for now`

A user's interests may remain stable while an intent can change weekly or daily.

## 5. Natural-Language Intent

Example input:

`I'm new to Hyderabad, like badminton and startups, and want to meet a small group this weekend somewhere relaxed, under ₹500.`

Possible extracted signals:

- Location → Hyderabad
- Group → Small
- Activity → Badminton
- Interest → Startups
- Environment → Relaxed
- Budget → ≤ ₹500
- Timing → This weekend

Then show:

### `Here's what I understood`

Every extracted signal is editable.

Actions for each signal:

- Edit
- Remove
- Add

## 6. AI Interpretation Boundary

AI produces an interpretation, not truth.

AI must never silently finalize an intent.

The user must review extracted signals before confirmation.

## 7. Ambiguity and Confidence

When a term is ambiguous, surface the ambiguity.

Example:

`When this weekend?`

Options:

- Saturday
- Sunday
- Either
- I'll decide later

AI must not invent precise dates, times, budgets, locations, or constraints.

## 8. Progressive Clarification

Ask only the high-value question needed to create a useful intent.

Example:

`I want to play badminton with some people this weekend.`

Possible next question:

`Where would you like this to happen?`

or:

`What part of the city works for you?`

Do not present a long questionnaire.

## 9. Intent Modes

Offer useful starting points:

- Meet people
- Do something
- Explore
- Build
- Learn

These are entry points, not a rigid taxonomy.

## 10. Desired Connection

### `Who would you like to do this with?`

Possible options:

- Someone new
- A few new people
- People who share my interests
- Activity partners
- Professional peers
- A small community
- Not sure yet

Do not require unnecessary demographic targeting.

## 11. Group Size

If relevant:

### `How many people feels right?`

Options:

- 2 people
- 3–4 people
- 5–6 people
- Small group
- Flexible

The current intent may refine, but should not silently rewrite, the user's general social preference.

## 12. Activity

### `What would you actually enjoy doing?`

Examples:

- Badminton
- Café
- Walk
- Board games
- Startup discussion
- Study session
- Food exploration
- Workshop
- Sports
- Open to ideas

Custom activity entry is supported.

## 13. Environment

### `What kind of place feels right?`

Examples:

- Quiet
- Relaxed
- Lively
- Outdoor
- Indoor
- Café
- Park
- Sports venue
- No preference

Do not assume environment solely from activity.

## 14. Location

### `Where should this happen?`

Possible controls:

- Use my city
- Choose an area
- Near a landmark
- I'm flexible

Avoid exact residential addresses. Exact meetup location can be decided later.

## 15. Timing

### `When would you like this?`

Options:

- Today
- Tomorrow
- This weekend
- Next week
- A specific date
- I'm flexible

Intent timing combines with Availability; it does not overwrite availability automatically.

Conceptually:

`Intent timing + Availability = Possible opportunity windows`

## 16. Budget

Ask only when relevant.

### `Anything you'd like to keep within?`

Options:

- Free
- Under ₹300
- Under ₹500
- Under ₹1000
- Flexible
- Set my own

Clearly distinguish user budget from estimated activity cost.

## 17. Constraints

### `Anything important we should avoid?`

Examples:

- Crowded places
- Long travel
- Late-night events
- Expensive activities
- Large groups
- Outdoor activities
- Alcohol-centered environments

Relevant boundaries from Social Preferences may be inherited, but the current intent can express additional constraints.

## 18. Intent-Specific Override

If the intent conflicts with a stable preference, explicitly surface the difference.

Example:

User preference: `Small groups`

Current intent: `20–30 person startup networking event`

Prompt:

`This is different from your usual preference. Should we allow larger groups for this intent?`

Actions:

- Use this intent only
- Keep my usual preference
- Change my preference

The intent must not silently mutate the user's profile.

## 19. Intent Strength

### `How strongly are you looking for this?`

Options:

- Just exploring
- I'd like this if something fits
- I'm actively looking
- I'd really like to make this happen

This helps distinguish exploration from genuine opportunity readiness.

## 20. AI Suggestion of Activities

When the user is flexible about the activity, AI may suggest options.

Example:

`You want to meet startup people this weekend but you're flexible about the activity.`

Prompt:

`Would you like Pyrintu to suggest an activity too?`

Actions:

- Yes, suggest
- I'll choose
- Keep it open

## 21. AI Clarification

AI may ask one high-value question at a time.

Example:

`Would you prefer a casual small-group conversation or an activity where you meet people naturally?`

Avoid multi-question interrogation.

## 22. Intent Summary

### `Here's your intent`

Example:

> Meet a small group in Hyderabad this weekend.
>
> Activity: Badminton
>
> People: New connections + shared interests
>
> Environment: Relaxed
>
> Budget: Up to ₹500
>
> Timing: Saturday evening
>
> Flexibility: Moderate
>
> Purpose: Meet new people

Prompt:

`Does this feel right?`

Actions:

- Yes, find opportunities
- Change something

## 23. Explainability and Source Labels

Provide:

### `Why did Pyrintu choose this?`

Examples:

`Relaxed came from “somewhere relaxed.”`

`Small group matches your social preference of 3–5 people.`

`Saturday evening fits the availability you provided.`

Show source labels where useful:

- `[Your preference]`
- `[Your availability]`
- `[Your intent]`

Every important signal should have a clear source.

## 24. Preference Conflict Explanation

When the intent conflicts with an existing preference:

`This is different from your usual preference.`

Then allow the user to choose which rule applies for the current intent.

## 25. Intent Lifecycle

Intent state:

`Draft → Reviewed → Confirmed → Active`

Users can later:

- Edit
- Pause
- Cancel

Time-bound intents can expire after their relevant period.

Open-ended intents should not remain silently stale forever.

## 26. Privacy

Intent content may reveal personal circumstances.

Default:

`Use internally for matching.`

Only the minimum relevant context should be exposed to other users when an opportunity is formed.

## 27. Safety

Intent must not bypass explicit user safety preferences or boundaries.

Private reasons remain private unless the user explicitly chooses to share them.

Essential safety controls remain available.

## 28. AI Boundary

AI may:

- understand natural language
- extract structured signals
- ask clarification questions
- summarize intent
- suggest activities
- explain signal sources

AI must not:

- invent availability
- invent location
- invent budget
- silently create hard constraints
- confirm a meetup
- decide who the user should meet
- override explicit safety boundaries

## 29. AI Failure

Message:

`Pyrintu can't structure this right now.`

Actions:

- Build it manually
- Try again

Manual intent creation must remain fully usable.

## 30. Empty State

### `What are you in the mood for?`

Starter examples:

- Meet a few people for badminton this weekend.
- Find someone to explore cafés with.
- Meet people interested in startups.
- Find a small study group.

## 31. Loading States

Examples:

- `Understanding your intent…`
- `Finding the important details…`
- `Checking your preferences…`
- `Preparing your intent…`

Avoid fake progress percentages.

## 32. Error States

### Unclear intent

`We need one more detail before we can use this.`

### Network

`We couldn't save your intent.`

### AI failure

`We couldn't understand that automatically. You can build it manually.`

Every error has a recovery path.

## 33. First-Time Guide

### Guide 04 — Intent

**Target:** `Create Intent`

**Message:** `Describe what you want right now. You can type it naturally — Pyrintu will structure it for you.`

## 34. Accessibility

- large accessible text input
- keyboard navigation
- screen-reader-friendly intent chips
- editable extracted values
- accessible source labels
- status announcements
- clear focus states
- no color-only distinctions
- reduced-motion support
- touch-friendly controls

AI clarifications must remain understandable without visual animation.

## 35. Responsive Behavior

### Mobile

`What do you want? → Natural-language input → AI interpretation → Missing-information question → Intent summary → Confirm`

### Desktop

Two-column layout may be used:

- Left: intent creation
- Right: live structured intent + source explanations

## 36. Analytics

Track:

- intent_viewed
- intent_started
- intent_mode_selected
- intent_text_submitted
- ai_intent_structuring_requested
- ai_intent_structuring_completed
- ai_intent_structuring_failed
- intent_signal_edited
- intent_signal_removed
- intent_signal_added
- intent_clarification_requested
- intent_clarification_answered
- intent_conflict_detected
- intent_conflict_resolved
- intent_summary_viewed
- intent_confirmed
- intent_saved
- intent_paused
- intent_cancelled
- intent_abandoned

Never send raw intent text into generic analytics.

## 37. Performance

- fast initial text input
- asynchronous AI processing
- optimistic local editing
- no full-page reloads
- manual mode always available
- AI response must not block the editor

## 38. Matching Boundary

Screen 8 creates the user's current intent. It does not perform final matching.

Conceptually:

`Profile + Social Preferences + Availability + Intent → Opportunity / Matching system`

The matching system is specified later.

## 39. Acceptance Criteria

### Natural Language

- User can describe what they want naturally.
- AI extracts useful signals.
- Every extraction can be corrected.

### Clarification

- Only high-value missing information is requested.
- Ambiguity is resolved before important decisions.

### Context

- Profile and social preferences can inform intent.
- Intent can intentionally override a normal preference without mutating the profile.

### Explainability

- User can see where important signals came from.
- AI-generated interpretations are clearly identified.

### Privacy

- Intent is not automatically public.
- Only relevant information is shared later.

### AI Safety

- AI cannot invent critical details.
- AI cannot bypass explicit boundaries.
- AI failure does not block intent creation.

### Lifecycle

- Intent can be edited.
- Intent can be paused.
- Intent can be cancelled.
- Time-bound intents can expire.

## 40. Pyrintu Moment

The intended experience is:

`User tells Pyrintu what they want → Pyrintu says what it understood → User confirms → Intent is ready.`

The user should feel:

`I didn't have to figure out how to use the app. I just told Pyrintu what I wanted.`

## Lock Note

Screen 8 was reviewed and explicitly approved in product discussion. It is now locked as a UX contract on `feature/ux-screen-8`; implementation remains separate from the UX specification.
