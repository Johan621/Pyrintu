# PYRINTU — UX SPECIFICATION
## Screen 26 — Shared Meetup Planning v1.0

**Status:** Approved for implementation planning

## Core objective
Give both connected participants a shared workspace where they can collaboratively turn an accepted meetup idea into a concrete plan. Neither participant silently controls the final meetup.

## Opening experience
**Heading:** Let's plan it together.

Supporting: **Work through the details together before confirming the meetup.**

## Shared proposal reference
Show the accepted meetup idea and state **Both interested**.

## Planning state
Accepted idea → Planning → Plan ready for review → Confirmed.

## Shared planner
Core fields:
- Activity
- Date
- Time
- Venue
- Budget
- Location
- Environment

Use explicit field states so suggested, discussed, shortlisted, agreed, and confirmed are distinct.

## Planning inputs
Each participant may contribute suggestions. Suggestions are neutral and do not create ownership of a decision.

## Activity
Reuse the established Activity Selection behavior instead of creating a second activity-selection engine.

## Date and time
Show shared availability outcomes without exposing unnecessary private schedule data. Distinguish preferred, possible, agreed, and confirmed states.

## Venue
Participant-provided venues are **Participant suggestions** until verified. Availability must be factual and clearly marked verified, unknown, or otherwise supported by current data.

## Budget
Support shared budget discussion. Conflicting budget preferences are surfaced neutrally; the system does not choose an arbitrary average.

## Environment
Support mutually relevant experience preferences such as quiet, casual, conversation-focused, or activity-focused.

## Accessibility and private constraints
Private accessibility or safety constraints may influence planning without being exposed unnecessarily. Show decision-relevant conflicts neutrally rather than identifying the participant behind a private constraint.

## Planning conversation
Provide a lightweight discussion area. Chat can discuss planning, but the structured plan remains the source of truth.

## Chat-to-plan conversion
A message such as "Let's do 6 PM" may produce a **Possible plan update** requiring explicit review. Chat must not silently mutate the plan.

## Agreement
When both participants agree on a field, show **Agreed during planning**. This is not the same as final meetup confirmation.

## Plan readiness
When required fields are complete:

**Your meetup plan is ready to review.**

Supporting: **Everything required for a final confirmation is now available.**

Action: **Review final meetup**.

Do not mark the meetup confirmed here.

## Participant change requests
Either participant can request changes to time, venue, activity, budget, or another field using neutral language without blame.

## Versioning and major changes
Material changes such as activity, date, significant time, venue, or significant cost create a new plan version and require re-review. Minor informational changes need not restart the full review.

## Alternatives
Provide a small set of meaningful alternatives with transparent trade-offs rather than unexplained scores.

## AI planning assistant
AI may summarize shared constraints, suggest activities, compare options, identify conflicts, draft neutral messages, and translate natural-language changes into structured proposals.

AI must not:
- decide the final plan;
- expose private constraints;
- fabricate venue availability or prices;
- claim both participants agreed when they did not;
- reserve anything without authorization;
- confirm the meetup.

AI-generated changes are **Suggested updates**, not confirmed updates.

## Notifications
Use neutral planning notifications such as **A new planning suggestion was added**, **The meetup plan changed**, and **Your plan is ready for review**. Avoid artificial urgency.

## Connection changes
If the connection is paused, ended, or blocked during planning, pause planning and require review of the latest connection state.

## Offline and errors
Offline state must clearly indicate that information may be stale and disable actions requiring server confirmation. Failed planning updates must be retryable without losing the latest valid plan.

## Race conditions
Concurrent edits must not silently overwrite one another. Show when a field changed during editing and allow review of the latest state and the user's suggestion.

## Reliability
Idempotency is required for creating and updating suggestions, applying changes, starting planning, and other state-changing actions so repeated taps do not create duplicates.

## Accessibility
- Semantic planner structure
- Keyboard-accessible controls
- Screen-reader-readable field states
- Accessible proposal and review actions
- Accessible comparison tables
- Clear Suggested / Agreed / Confirmed distinctions
- No color-only state meaning
- Accessible errors
- Reduced-motion support
- Focus preservation after updates

## Responsive behavior
### Mobile
Shared meetup idea → Activity → Date → Time → Venue → Budget → Shared conversation → Suggestions → Plan readiness.

### Desktop
Left: structured plan. Right: planning conversation, alternatives, AI assistant, change requests, and plan status. The structured plan remains visually primary.

## Analytics
Track planner view, field starts, suggestion lifecycle, change requests, version creation, conflicts, alternatives, AI actions, plan readiness, review start, save failures, offline state, and race conditions. Do not store private constraints or sensitive planning conversation content in generic analytics.

## Product boundary
Screen 26 does not confirm the meetup, book a venue, charge a user, expose private constraints, replace Activity Selection, replace Activity Plan, replace Meetup Confirmation, turn the planner into a permanent chat room, or let AI make final decisions.

Its responsibility is to provide a shared workspace where two mutually connected participants collaboratively build a new meetup plan.

## Relationship to Screen 25
Screen 25 New Meetup Intent → Both interested → Screen 26 Shared Meetup Planning → Plan ready → Existing planning / confirmation flow.

## Acceptance criteria
- Shared planning begins only after both participants are interested.
- Both participants can contribute.
- Planning fields have explicit states.
- Suggested ≠ Agreed ≠ Confirmed.
- Private constraints remain protected.
- Structured plan remains the source of truth.
- Chat can suggest changes without silently changing the plan.
- Material changes create a new plan version and require re-review.
- AI remains advisory.
- Venue/payment/booking remain downstream operations.
- Offline and race-condition handling is explicit.
- Safety controls remain available.
- Accessibility requirements are satisfied.

## Product principle
The experience should feel like **we're building this together**, not that one participant or the AI controls the meetup.