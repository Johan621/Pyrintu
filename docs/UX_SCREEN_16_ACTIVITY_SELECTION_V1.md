# PYRINTU — UX SPECIFICATION
## Screen 16 — Activity Selection v1.0

**Status:** Approved

## Core objective
Help the group choose an activity that fits the original intent, realistic constraints, timing, environment, accessibility needs, and group preferences while preserving group agency.

## Opening experience
**Heading:** What should you do together?

Supporting: Choose something that fits the group's interests, timing, environment, and practical constraints.

## Existing intent context
Show the current group intent in a compact context bar. Example: badminton + meeting new people, Sunday evening, small group, Hyderabad. Allow viewing the original intent.

## Group context
Show current participant count, proposed timing, area, and estimated budget where available. Mark uncertain information as Proposed, Estimated, or Flexible.

## Activity recommendations
Present a small number of useful activity options. Each recommendation must explain why it fits using actual group signals. Avoid marketplace-style volume.

## Activity sources
Clearly indicate whether an activity came from a shared interest, current intent, group exploration, or Pyrintu suggestion. AI-generated suggestions must be labeled as suggestions rather than user-stated facts.

## Categories
Lightweight categories may include Sports, Food & Cafés, Games, Outdoor, Learning, Creative, Professional, Community, and Explore.

## Natural-language activity input
Allow users to describe desired qualities such as “something relaxed where we can talk more.” Pyrintu may translate that into several suggestions. Suggestions must not silently replace the current selection.

## Group decision model
Activity choice is a group decision. Avoid single-person approval unless explicit group rules establish it. Communicate that everyone gets a chance to weigh in.

## Activity response
Participants may respond with Like, Maybe, or Not for me. Individual responses should not be exposed unnecessarily. Group-level summaries are preferred.

## Activity consensus states
Exploring → Shortlisted → Group leaning → Chosen → Confirmed.

Selected is not the same as Confirmed. Confirmation requires the defined deterministic group conditions and viable activity details.

## Activity comparison
Where multiple options are shortlisted, provide factual comparison on dimensions such as social interaction, estimated cost, travel, timing fit, and shared-interest fit. Do not invent or use pseudo-precise values.

## Constraints
Check group size, timing, location, budget, accessibility, safety requirements, availability, and activity eligibility. Hard constraints must not be silently overridden.

## Constraint conflicts
If an activity may violate an important group constraint, explain the conflict without revealing whose private preference caused it. Offer alternative actions such as choosing another activity, reviewing the constraint, or asking Pyrintu for alternatives.

## Constraint relaxation
Never silently broaden criteria. Show exactly what would change and require explicit consent before considering the relaxed option.

## Activity flexibility
Allow the group to be open to alternatives without interpreting that as removal of all constraints.

## Duration and format
Show expected duration and available formats where verified. Examples may include casual doubles vs open play, or casual conversation vs a specific café format.

## Optional second activity
Support optional extensions such as badminton plus café afterward. Optional activities are not required commitments.

## Venue preview
Show possible venues only as previews where useful. Exact venue choice belongs to the Activity Plan flow.

## Activity availability
Clearly distinguish verified availability from unknown or stale availability. Never claim an activity or venue is available without supporting data.

## AI role
AI may suggest activities, explain why they fit, summarize group preferences, compare options, identify conflicts, and translate natural-language requests into criteria.

AI must not invent venues, pricing, availability, consensus, or participant characteristics; decide for the group; or override hard constraints.

## AI uncertainty
When required information is missing, AI should state what it cannot determine and request the minimum necessary detail rather than guessing.

## Group preference summary
Use plain-language priority labels such as High, Medium, and Flexible rather than stars or pseudo-precision.

## Recommended activity
A top recommendation may be labeled **Best current fit** only when it actually satisfies the relevant criteria. Avoid “perfect activity” or equivalent certainty.

## Selection
Selecting an activity creates a Selected state and may trigger group review. It does not automatically confirm the activity.

## Confirmation
When deterministic conditions are met and the activity is viable, state that the activity is now the group's selected activity. Users should still understand that meetup confirmation occurs later.

## Activity changes
Major activity changes may require participant revalidation because they can affect timing, cost, accessibility, or preferences.

## Activity cancellation
If a selected activity becomes unavailable, preserve the group and offer alternatives rather than dissolving the group automatically.

## Empty state
If insufficient activity information exists, invite users to start with an activity, feeling, or simple description. Provide examples such as “Something active,” “Somewhere we can talk,” or “Something under ₹500.”

## No suitable activities
State honestly when nothing fits all current constraints. Offer explicit choices to adjust a preference, relax one constraint, or try another idea.

## Activity search
Provide search by activity name or concept. Search results must still respect relevant group constraints.

## Search result explanation
Where available, show activity, approximate duration, estimated cost, area, fit indicators, and verified availability. Unknown values must remain unknown.

## Accessibility
- Keyboard-accessible activity cards
- Semantic selection controls
- Accessible group response controls
- Screen-reader-readable activity states
- Clear conflict announcements
- No color-only preference state
- Touch-friendly controls
- Reduced-motion support
- Visible focus states
- Accessible comparison tables

Example: “Badminton. Strong fit. Selected by group. Estimated cost ₹350. View details button.”

## Responsive behavior
### Mobile
Group context → Recommended activity → Other options → Why this fits → Group responses → Conflicts → Search/natural language → Selected activity.

### Desktop
Left: recommendations and comparison. Right: group priorities, why this fits, current selection, and open conflicts.

## Loading states
- Finding activities that fit…
- Checking group constraints…
- Comparing available options…
- Generating a few ideas…
AI must not block manual selection.

## Error states
### Activity search failure
Could not load activity options. Offer Retry and Enter an activity manually.

### AI failure
Could not generate suggestions. Offer Choose manually.

### Availability failure
Could not verify current availability. Mark availability as Unknown rather than Available.

## Stale activity state
When information is outdated, show that clearly and offer Refresh. If an activity becomes unavailable, offer alternatives without dissolving the group.

## Analytics
Track activity-selection views, recommendation views, reasoning views, searches, natural-language refinement, suggestions, selections, unselections, group responses, conflicts, constraint relaxation, review, confirmation, changes, unavailability, AI failure, and manual fallback. Do not send raw participant preferences or private responses into generic analytics.

## Performance
- Screen shell and cached group context load immediately.
- Recommendations load progressively.
- AI runs asynchronously.
- Search remains responsive.
- Selection feels immediate.
- Stale information is reconciled before confirmation.

## Product boundary
Screen 16 does not finalize exact venue, exact meetup time, the meetup itself, reservations, private participant preferences, or group consensus by itself. It establishes the activity direction for the planning flow.

## Handoff
Screen 16 Activity Selection → selected activity → Screen 17 Activity Plan → venue/time/logistics → Screen 19 Meetup Confirmation.

## Acceptance criteria
### Activity relevance
- Suggestions are based on actual group signals.
- Important constraints are respected.
- No fabricated activity details.

### Group control
- Activity choice remains a group decision.
- Individual responses do not create social pressure.
- Selected ≠ Confirmed.

### AI
- AI suggestions are clearly labeled.
- AI explanations are grounded.
- AI cannot decide for the group.

### Practicality
- Cost, duration, location, and availability are transparent.
- Verified vs unknown information is distinguishable.

### Flexibility
- Manual search and natural-language refinement are supported.
- Constraint relaxation is explicit.

### Safety and privacy
- Private preferences are not exposed.
- Safety controls remain accessible.

### Reliability
- Stale information is handled.
- Unavailable activities can be replaced without dissolving the group.

### Accessibility
- Keyboard accessible.
- Screen-reader compatible.
- No color-only meaning.

## Product principle
Activity is the bridge from matching to real-world connection: **Group context + relevant options + transparent trade-offs + group choice → Activity selected.**
