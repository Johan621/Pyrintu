# PYRINTU — UX SPECIFICATION
## Screen 12 — Match Reasoning v1.0

**Status:** Approved

## 1. Core objective

Explain the recommendation using real, user-provided and opportunity-derived signals.

The user should understand:

- What signals mattered
- How they fit together
- What is a strong fit
- What is only flexible
- What Pyrintu does not know
- What the user can decide

## 2. Opening experience

### Heading

**Why Pyrintu thinks this could work**

### Supporting text

> There isn't one perfect-match number. Pyrintu looks at several signals and explains the parts that actually matter.

## 3. Match reasoning summary

Show a human-readable summary such as:

- Strong fit
- 4 strong signals
- 1 flexible difference
- 2 things still uncertain

Do not make an arbitrary percentage the primary experience.

## 4. Reasoning categories

Organize reasoning into:

- Connection
- Social fit
- Timing
- Activity
- Environment
- Practical fit

## 5. Positive signals

Example:

### Shared interest — Badminton

> You enjoy badminton and the opportunity includes badminton.

Show the source and a human-readable strength such as **Strong**.

## 6. Social fit

Example:

### Group size fits

> You prefer small groups, and this opportunity currently has four participants.

Source: **Your social preferences + opportunity state**.

## 7. Timing fit

Example:

### Timing works

> The proposed Sunday evening time falls within the availability you provided.

If tentative, explicitly use wording such as:

> Proposed Sunday evening overlaps with your usual availability.

Do not claim definite availability when the time is only proposed.

## 8. Intent fit

Example:

### Matches your current intent

> Your current intent asks for a relaxed small-group experience this weekend.

Source: **Current intent**.

## 9. Practical fit

Example:

### Budget is compatible

> Your current intent allows up to ₹500, while this opportunity is estimated at ₹350.

Clearly distinguish estimates from confirmed values.

## 10. Differences

Show meaningful mismatches rather than hiding them.

Example:

> You usually prefer quieter environments. This venue is expected to be moderately lively.

Then explain whether the difference is within the user's flexibility or conflicts with an important preference.

## 11. Hard constraint conflicts

An opportunity should normally not appear as a positive recommendation if it violates a hard boundary.

If an explicit current-intent override allows it, show why it is appearing and make the exception traceable.

## 12. Evidence cards

Each reasoning item should be independently inspectable.

Example:

```text
Small group

Your preference: 3–5 people
Opportunity: 4 people
Source → Social Preferences
Strong fit
```

Provide contextual actions such as **Why?** and **Change preference**.

## 13. Source attribution

Every reasoning signal must identify an understandable source where applicable:

- Your profile
- Your social preferences
- Your availability
- Your current intent
- Opportunity data
- Participant state
- System eligibility

Avoid vague attribution such as “AI thinks this.”

## 14. AI explanation layer

AI may convert deterministic reasoning inputs into natural-language explanations.

Example:

> Badminton is something you enjoy, the group size is within your preferred range, and the proposed Sunday evening timing fits your current availability.

The deterministic reasoning signals remain the source of truth.

## 15. AI grounding requirement

AI explanations must be generated only from approved reasoning inputs.

AI must not invent psychological compatibility or unsupported personal traits.

Prefer:

> You both selected badminton.

Not:

> You two have similar personalities.

## 16. No fabricated reasoning

Never state a shared interest, preference, trait, or relationship quality unless supported by the actual available signal.

## 17. Reasoning hierarchy

Use human-readable categories:

- **Strong** — directly stated or deterministic and highly relevant
- **Supporting** — relevant but not decisive
- **Flexible** — preference allows variation
- **Unknown** — insufficient information

Example:

```text
Strong
✓ Activity

Supporting
✓ Shared interest

Flexible
~ Environment

Unknown
? Conversation chemistry
```

## 18. What Pyrintu cannot know

Include a visible section such as:

### What we can't know yet

Examples:

> Whether you'll enjoy the conversation.

> Whether the group dynamic will feel natural.

> Whether you'll want to meet again.

Pyrintu explains opportunity fit; it does not claim certainty about future relationships.

## 19. What would change this recommendation?

Explain meaningful changes to recommendation evidence.

Examples:

> If your availability changes, the opportunity may no longer be a fit.

> If the group grows beyond six people, it may conflict with your preferred size.

> If the activity changes from badminton to something else, the strongest shared-interest signal disappears.

## 20. Reasoning timeline

Where useful, show causal progression:

```text
Your intent
    ↓
Your preferences
    ↓
Availability
    ↓
Opportunity formation
    ↓
Current recommendation
```

## 21. Why not another opportunity?

Do not expose proprietary ranking mechanics.

Use high-level truthful explanations such as:

> This opportunity appears ahead of another one because it fits your requested timing more closely.

## 22. Avoid ranking manipulation

Do not use language such as “perfect match,” “best match ever,” or pressure to accept.

Prefer:

> Strong fit for your current intent.

## 23. User control

Provide paths to:

- Change my preferences
- Edit my intent
- Update availability

Each action should route to the correct source of the signal.

## 24. “I disagree”

Provide:

### This doesn't feel right

Optional reasons:

- That's not my preference
- Pyrintu misunderstood me
- The opportunity changed
- This signal isn't important to me
- Something else

Feedback should be optional and actionable.

## 25. AI correction

When a correction may be local or global, ask which scope the user intends.

Example:

> I don't actually care about quiet environments for this plan.

Then:

> Should this change only this opportunity, or your general preference?

Actions:

- This opportunity only
- Change my general preference

Do not silently mutate permanent preferences from a one-off correction.

## 26. Privacy

Reasoning must never expose another participant's private preference or unrelated personal information.

Use generalized evidence where necessary.

## 27. Participant-level reasoning

When appropriate, explain why a participant is relevant using permitted signals such as:

- Shared activity
- Compatible group preference
- Relevant broad location

Do not expose hidden availability, private constraints, safety settings, or private intent wording unless explicitly permitted.

## 28. Match reasoning vs identity

A compatibility explanation is not a character judgment or safety guarantee.

Do not imply that someone is trustworthy because an algorithm matched them.

## 29. Mutuality reasoning

When relevant:

> This opportunity is stronger because several participants have independently expressed interest.

Do not expose private individual decisions unnecessarily.

## 30. Current state

Show factual current state such as:

```text
Recommendation state
Strong fit

Mutuality
Forming

Plan
Proposed

Venue
Not confirmed
```

Do not present predicted or proposed states as completed facts.

## 31. AI question mode

Provide:

### Ask about this recommendation

Example questions:

- Why is the group size a good fit?
- Which of my preferences mattered most?
- What doesn't fit perfectly?
- What is still unknown?

Answers must use the same deterministic reasoning context.

## 32. AI answer structure

Example:

> **Why is this a strong fit?**
>
> Three things stand out:
>
> **1. Activity** — You selected badminton.
>
> **2. Group size** — You prefer 3–5 people and this opportunity has four.
>
> **3. Timing** — The proposed Sunday evening falls within your stated availability.
>
> One difference is the venue's expected activity level.

## 33. AI uncertainty

When the reasoning engine lacks sufficient evidence:

> Pyrintu doesn't have enough information to say that yet.

Do not substitute unsupported probabilistic language for missing evidence.

## 34. Loading state

Examples:

> **Putting together the reasoning…**

> **Preparing a clearer explanation…**

Deterministic reasoning should load independently from AI-generated prose.

## 35. Error state

### Reasoning unavailable

> **We can't show the full explanation right now.**

Show deterministic summary signals where possible.

Action: **Try again**.

### AI explanation unavailable

> **The explanation assistant isn't available right now.**

Core reasoning remains usable.

## 36. Recovery

If opportunity or participant data changes:

> **This recommendation changed.**

Action:

**Review updated reasoning**

Do not silently present stale reasoning against a changed opportunity.

## 37. First-time guide

Existing Guide 05:

**Target:** `Why this match?`

**Message:** `Pyrintu will show the real signals behind a recommendation rather than giving you a mysterious score.`

Use contextual guidance rather than an intrusive tutorial.

## 38. Accessibility

Requirements:

- Semantic reasoning groups
- Source labels accessible to screen readers
- Confidence category announced
- Unknown/uncertain states accessible without color
- Expandable explanations keyboard accessible
- Correction actions accessible
- Focus preserved after changes
- Reduced-motion support
- No information conveyed only through color or visual hierarchy

Example screen-reader output:

> Strong fit. Activity: badminton. Source: current intent. Supporting signal: group size matches social preference. Unknown: conversation chemistry.

## 39. Responsive behavior

### Mobile

```text
Recommendation summary
↓
Strong signals
↓
Supporting signals
↓
Flexible differences
↓
What is unknown
↓
Participant reasoning
↓
What would change this
↓
Ask Pyrintu
↓
Actions
```

### Desktop

```text
LEFT
Reasoning breakdown

RIGHT
Opportunity snapshot
+
Current state
+
Ask Pyrintu
```

## 40. Analytics

Track:

```text
match_reasoning_viewed
reasoning_signal_viewed
reasoning_source_viewed
reasoning_unknowns_viewed
reasoning_difference_viewed
reasoning_change_impact_viewed
reasoning_preference_edit_started
reasoning_intent_edit_started
reasoning_availability_edit_started
reasoning_disagree_started
reasoning_disagree_submitted
reasoning_ai_question_started
reasoning_ai_question_completed
reasoning_ai_failed
reasoning_updated_after_opportunity_change
```

Never send raw participant private data or raw AI conversations into generic analytics.

## 41. Performance

- Deterministic reasoning renders without waiting for AI.
- Cached explanation signals may be used where safe.
- AI text loads asynchronously.
- Interactions remain responsive.
- No full-page reload.
- Updated opportunity state invalidates stale reasoning.

## 42. Product boundary

Screen 12 does not decide:

- whether the user should accept
- whether another person is “good”
- whether the meetup will succeed
- whether a relationship will develop

It explains the evidence behind the current recommendation.

## 43. Relationship to scoring systems

Technical architecture may later define internal scores for eligibility, compatibility, availability fit, and opportunity quality.

This UX contract does not expose raw model mechanics by default.

```text
Internal computation
        ↓
Human-readable evidence
        ↓
User understanding
```

## 44. Acceptance criteria

### Explainability

- User can see the actual signals behind a recommendation.
- Signals have understandable sources.
- Strong, supporting, flexible, and unknown states are distinguishable.

### Accuracy

- No invented facts.
- No fabricated psychological compatibility.
- Unknown information remains unknown.

### Transparency

- Differences are shown.
- User can see what would change the recommendation.
- Important signals can be traced back to their source.

### Privacy

- Private participant information is not exposed.
- Reasoning does not reveal hidden preferences.

### AI

- AI is grounded in deterministic reasoning inputs.
- AI cannot create unsupported claims.
- AI failure does not remove core reasoning.

### User control

- User can disagree.
- User can change the relevant source.
- Temporary corrections do not silently modify permanent preferences.

### Accessibility

- Fully keyboard accessible.
- Screen-reader compatible.
- No color-only meaning.

## 45. Pyrintu trust moment

The intended experience is:

> **Pyrintu isn't asking me to trust a score. It showed me the evidence, including what doesn't fit and what it doesn't know. Now I can decide.**

This prepares the user for:

```text
Discovery
   ↓
Match Details
   ↓
Match Reasoning
   ↓
Screen 13 — Mutuality
```

**Approved status:** Screen 12 approved in product review and recorded as the canonical detailed UX contract for this screen. Implementation remains separate from UX specification and technical architecture.
