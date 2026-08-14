# PYRINTU — UX SPECIFICATION
## Screen 28 — Confirmed Meetup Operations & Changes v1.0

**Status:** Approved for implementation planning

## Core objective
Provide a reliable operational surface for a confirmed meetup. Show the canonical confirmed meetup, current logistics, operational status, changes, exceptions, safety, and recovery without silently altering confirmed state.

## Opening experience
**Heading:** Your meetup is confirmed

Supporting: **Here are the current details and anything you need to know before you meet.**

## Confirmation summary
Show canonical current values for activity, date, time, venue, participants, and status.

## Operational status
Support explicit states such as Confirmed, Operationally ready, Changed / Needs review, Cancelled, and Completed. The current state must be obvious.

## Plan vs operational details
Separate the confirmed meetup plan from operational metadata such as reservation reference, arrival instructions, venue contact, parking, equipment, access instructions, and cancellation policy.

## Canonical plan
Provide **View full plan** and ensure there is one authoritative confirmed version.

## Reservation state
Distinguish Confirmed, Pending, Changed, Cancelled, and Unavailable. Never claim a live reservation without current evidence.

## Material changes
Material changes include date, substantial time change, venue, activity, significant cost, or participant composition. Such changes transition the meetup to **Needs review** rather than silently remaining confirmed.

## Minor changes
Small operational updates, such as parking entrance or contact-note changes, may update without invalidating confirmation when product rules allow. Label them as operational detail updates.

## Change impact
When a change occurs, show **What changed** and **Does this affect your confirmation?** Explain whether the old confirmation remains valid or needs review.

## Reconfirmation
For material changes:
> **The meetup details changed**

Supporting: **Please review the updated plan before continuing.**

Actions: **Review changes** / **Decline updated meetup**.

Do not automatically preserve old confirmation for a material new version.

## Change history
Provide a concise decision-relevant history such as Confirmed → Venue changed → Plan updated → Awaiting review.

## Participant changes
If a participant leaves or a new participant is added, revalidate the meetup. Avoid exposing private reasons unnecessarily.

## Date/time/activity/venue/cost changes
Handle each as a material change where applicable, with neutral messaging and renewed review. Cost increases must be explicit.

## Payment changes
Any additional payment requires explicit authorization. Never silently charge.

## Cancellation
A confirmed meetup may be cancelled by participant choice, venue/activity unavailability, safety requirements, or system rules. Use neutral factual language and do not expose private reasons unnecessarily.

## Cancellation consequence
Show **Meetup cancelled** and allow **View what changed**, **Return to connections**, or **Find another opportunity**. Never automatically create a replacement meetup.

## External disruptions
For venue closures, event cancellation, transit disruptions, or other verified disruptions, show factual information and offer **Review options**. Do not auto-cancel unless explicit product rules require it.

## Travel and logistics
Show concise, verified or clearly estimated arrival, transit, parking, accessibility, equipment, and entry guidance. Never expose participant home locations or unnecessary distance-to-home data.

## Safety
Keep **Safety Center**, **Report**, and **Block** accessible before and after confirmation.

## Connection communication
Provide **Open connection**. Structured meetup state remains authoritative. A chat message proposing a change does not itself modify the confirmed meetup.

## Operational proposal
A participant can propose a material change, such as moving the time. The other participant reviews it through the structured change flow. Acceptance updates the canonical state only after required rules pass.

## Change versioning
Use a clear sequence such as Confirmed v3 → Proposed change → Review v4 → Participant confirmations → Confirmed v4.

## AI operational assistant
AI may summarize current meetup details, explain changes, answer factual logistics questions, and summarize verified operational state.

AI must not:
- mark a changed meetup confirmed;
- claim a reservation is active without current evidence;
- make payments;
- cancel a meetup without authorization;
- silently accept operational changes;
- reveal private participant reasons;
- invent venue or travel information.

## Reminders and calendar
Support reasonable reminders and **Add to calendar**. Calendar state should reflect the latest confirmed state and should not be claimed synchronized unless successful.

## Offline and errors
Offline state must clearly indicate that information may be stale and disable actions requiring server confirmation. Errors are factual and retryable without losing the latest valid meetup state.

## Race conditions and reliability
Concurrent changes must not silently overwrite one another. State-changing actions must be idempotent so repeated taps do not duplicate cancellations, reservations, payments, calendar events, notifications, or meetup versions.

## Accessibility
- Semantic confirmed-state hierarchy
- Accessible change history
- Screen-reader-readable operational status
- Keyboard-accessible actions
- Accessible dialogs and reservation/payment states
- Accessible errors
- No color-only state meaning
- Reduced-motion support
- Focus preservation after state transitions

## Responsive behavior
### Mobile
Meetup status → confirmed plan → operational details → changes → reservation → safety → actions.

### Desktop
Left: confirmed meetup, operational details, change history. Right: reservation, current status, actions, safety, AI assistant.

## Analytics
Track confirmed meetup views, operational details, reservation status, change detection/review/accept/decline, version creation, participant/venue/time/date/activity/cost changes, cancellation, disruptions, calendar/reminder actions, AI operational assistance, safety actions, offline and race-condition events. Do not store private cancellation reasons, payment credentials, private participant context, or sensitive location data in generic analytics.

## Product boundary
Screen 28 does not replace final confirmation, silently change confirmed details, automatically cancel a meetup, expose private participant reasons, automatically pay for changes, expose private home locations, or let AI manage the meetup autonomously. Its responsibility is to keep a confirmed meetup accurate, transparent, and operationally trustworthy until it happens or is legitimately cancelled.

## Relationship to Screen 27
Screen 27 Shared Final Review → Confirmed Meetup → Screen 28 Confirmed Meetup Operations → changes / logistics / exceptions → Meetup Day-of.

## Reuse existing systems
Reuse canonical confirmation state, activity plan, reservation state, participant state, safety controls, change/version model, and notification infrastructure. Do not create competing definitions of Confirmed, Cancelled, participant acceptance, or reservation confirmation.

## Acceptance criteria
- Confirmed meetup state is always obvious.
- Operational details are separated from the core plan.
- Material changes invalidate stale confirmation where required.
- Minor operational updates are distinguished from material changes.
- Reservation and participant agreement remain separate.
- Cost changes are transparent.
- Payments require explicit authorization.
- Cancellation is neutral and controlled.
- AI can explain changes but cannot act autonomously.
- Private reasons and personal locations remain protected.
- Offline and race-condition states are explicit.
- Actions are idempotent.
- Safety controls remain accessible.
- Accessibility requirements are satisfied.

## Product principle
**This meetup is real, and I can trust the information I'm seeing.** When something changes, Pyrintu tells the user exactly what changed and whether another decision is required.
