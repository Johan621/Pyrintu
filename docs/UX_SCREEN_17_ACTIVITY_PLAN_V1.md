# PYRINTU — UX SPECIFICATION
## Screen 17 — Activity Plan v1.0

**Status:** Approved

## Core objective
Turn the selected activity into a concrete, reviewable plan covering activity, date, time, venue, location, duration, cost, logistics, alternatives, and participant review without prematurely confirming the meetup.

## Opening experience
**Heading:** Let's make the plan real.

Supporting: Review the activity, timing, venue, and practical details before the group confirms anything.

## Current activity
Show the selected activity prominently, e.g. **Badminton · 60–90 minutes · Selected by the group**. Allow **Change activity** and preserve valid planning information where possible.

## Plan summary
Show date/time/area/activity/duration/cost/venue state. Every important field has a state.

## Plan state model
Unknown → Suggested → Proposed → Verified → Confirmed.

Use labels such as Confirmed, Proposed, Verified, Estimated, Needs decision, or Unknown. Do not turn flexible or approximate information into false certainty.

## Date and time
Allow specific date/time or supported flexible windows. Do not convert natural language such as “this weekend” into a precise date without clarification. Show whether timing is proposed, verified, or confirmed. Offer a small number of realistic alternatives when useful.

## Venue
Show candidate venues with name, broad location, activity suitability, current availability state, accessibility information where available, and cost. Distinguish **Verified**, **Unverified**, **Unknown**, and **Expired** availability. Never claim live availability without reliable evidence.

## Location privacy
Show the venue and relevant area, not participant home locations or private addresses. Travel information must be approximate or verified and must not expose unnecessary personal location data.

## Cost
Show estimated/verified/confirmed cost and known cost components. Surface unavoidable booking fees, equipment, and optional components. If the plan exceeds the current budget target, state the conflict and offer alternatives or explicit budget adjustment. Never silently relax budget constraints.

## Duration and optional components
Show expected duration and distinguish the main activity from optional extensions such as a café afterward. Optional components are not commitments until explicitly accepted.

## Logistics
Where reliable information exists, show arrival guidance, transport context, parking, accessibility, operating hours, and similar logistics. Unknown information must remain explicitly unknown.

## Plan checks
Show deterministic checks such as group size, availability overlap, cost compatibility, selected activity, venue suitability, and accessibility/safety eligibility. Surface conflicts without blaming individual participants.

## Alternatives
Provide a small set of workable alternative plans with meaningful differences in time, venue, cost, or travel. Avoid overwhelming the group with exhaustive options.

## Why this plan
Explain why the current plan is a strong fit using actual group/activity signals. Avoid opaque scores and unsupported claims.

## Natural-language planning
Allow requests such as “make it earlier and keep it under ₹400.” Parse them into explicit criteria, show the interpretation, and require the user to apply the refinement. Do not mutate group constraints silently.

## AI role
AI may suggest time/venue combinations, summarize trade-offs, translate natural-language requests, explain plan fit, identify conflicts, and suggest alternatives. AI must not invent availability, prices, venue policies, participant data, or bookings; cannot confirm the meetup or override group constraints; and must not expose private participant information.

## Group decision flow
Suggested plan → Group review → Plan proposed → Participant confirmation → Plan confirmed.

AI cannot declare confirmation. The confirmation threshold is deterministic.

## Participant review
Participants can review date, time, venue, cost, activity, and optional components. Responses may include **Works for me**, **Need a change**, or **Can't do this**. Individual responses should not be exposed unnecessarily; use neutral aggregate language such as “The plan needs one more response.”

## Change requests
For **Need a change**, ask what needs attention: time, venue, cost, activity, accessibility, or something else. The group should see that a change was requested without unnecessary attribution to a person.

## Plan versioning
Material changes create a new plan version. Show the current version and distinguish old from current details. Major changes include date, significant time/location changes, material cost increases, activity changes, or major group-composition changes.

## Major-change revalidation
When a material change occurs, show **The meetup plan changed. Please review the updated details.** Prior acceptance must not automatically carry forward when the change is material.

## Booking boundary
**Plan confirmed** and **Reservation confirmed** are separate states. If a reservation is required, show its status independently. Any booking or charge requires explicit authorization and a clear pre-action statement.

## Booking failure
If reservation fails, keep the meetup plan saved but mark the venue as unconfirmed. Offer retry or another venue.

## Empty states
If no workable plan exists, say so clearly and offer alternatives, constraint adjustment, or continued planning. If no current venue availability can be verified, do not manufacture availability.

## Loading states
Examples: **Building the plan…**, **Checking venue availability…**, **Comparing time options…**, **Checking group constraints…**. Only show stages that correspond to actual work.

## Error states
Availability verification failure → mark availability unknown and offer retry. Plan save failure → preserve previous valid version. Participant response failure → retry. AI failure → offer manual planning.

## Offline state
Clearly indicate that information may be stale and disable live-verification actions. Local changes may be marked **Pending sync** but must never appear confirmed until server confirmation.

## Safety and privacy
Do not expose participant private availability or preferences. Keep Report, Block, Leave group, and Safety Center accessible. Safety eligibility is separate from meetup confirmation.

## Accessibility
Use semantic form structure; accessible date/time controls; keyboard-selectable venues; screen-reader-readable plan states; accessible comparison, errors, and confirmation states; visible focus; no color-only meaning; reduced-motion support.

Example screen-reader summary: “Activity plan version two. Sunday 7 PM. Venue B. Estimated cost ₹380. Availability verified. Plan proposed. Three participants have accepted.”

## Responsive behavior
### Mobile
Activity → Date → Time → Venue → Cost → Travel/accessibility → Plan checks → Alternatives → Participant review → Next step.

### Desktop
Left: current plan, venue, time, cost, logistics. Right: plan checks, alternatives, participant review, AI planning assistance.

## Analytics
Track plan view, date/time selection, venue view/selection, availability checks/failures, cost view, alternatives, constraint conflicts/relaxation, natural-language refinement, AI suggestions, participant review/acceptance/change/decline, plan versioning, major-change reconfirmation, confirmation, booking, save errors, and AI failures. Do not send private participant response details or sensitive participant data to generic analytics.

## Performance
Current activity and plan load first. Venue availability and alternatives may load progressively. AI is asynchronous. Edits remain responsive. Stale availability is revalidated before final confirmation.

## Product boundary
Screen 17 does not automatically book a venue, charge a user without explicit authorization, confirm a meetup solely because a plan exists, expose private availability, silently relax constraints, guarantee availability, or guarantee attendance. It creates the reviewable meetup plan.

## Handoff
Screen 16 Activity Selection → Screen 17 Activity Plan → Screen 18 Group Chat → Screen 19 Meetup Confirmation.

Structured plan remains the source of truth; chat remains conversation.

## Acceptance criteria
- Proposed, verified, and confirmed states are distinguishable.
- Time, venue, cost, duration, logistics, and accessibility are transparent.
- Availability is verified or explicitly unknown.
- Participants can review and request changes.
- Material changes trigger revalidation.
- Booking and plan confirmation are separate.
- Charges/reservations require explicit authorization.
- AI is grounded and cannot invent operational facts or book autonomously.
- Private participant availability/preferences are not exposed.
- Previous valid plan state is recoverable after failures.
- Offline changes cannot appear confirmed.
- Screen is keyboard accessible and screen-reader compatible.

## Product principle
The plan should make the real-world commitment inspectable: **what we are doing + when + where + what it costs + what is verified + who has reviewed it + what still needs confirmation**.