# PYRINTU — UX SPECIFICATION
## Screen 27 — Shared Meetup Final Review v1.0

**Status:** Approved for implementation planning

## Core objective
Provide both connected participants with a final, synchronized review of the new meetup before it becomes confirmed. Both participants review the same canonical plan version; shared planning agreement is not final confirmation.

## Opening experience
**Heading:** Ready to confirm your meetup?

Supporting: **Review the final plan together before confirming.**

No artificial urgency or pressure.

## Plan identity
Show the current plan version and status, e.g. **New Meetup · Plan version v3 · Ready for final review**.

## Final summary
Display the canonical current values for:
- Activity
- Date
- Time
- Venue
- Duration
- Estimated/confirmed cost
- Participant count
- Reservation state

Every value must come from the current structured plan.

## Field states
Distinguish states such as **Confirmed for review**, **Verified**, **Estimated**, and **Pending**. Never hide uncertainty.

## Readiness checklist
Show required checks such as activity, date, time, venue, group requirements, participant review eligibility, and any reservation/payment conditions. If a required item is unresolved, confirmation is blocked or explicitly conditional.

## Participant review
Each participant confirms independently. One participant's state must not be inferred from the other's behavior. Use aggregate status where possible and do not expose unnecessary private hesitation details.

## Planning vs confirmation
**Agreed during planning** is not equivalent to final confirmation. The user must explicitly confirm the current plan version.

## Final fields
Activity, date/time, venue, cost, reservation, optional elements, logistics, accessibility, and safety are shown with their factual current states. Changes route back to planning/review rather than silently mutating the final plan.

## Cost and payment
Estimated vs confirmed costs must be explicit. Any reservation payment requires explicit authorization. Never charge automatically.

## Reservation boundary
Distinguish venue selected, venue verified, reservation pending, reservation confirmed, and reservation failed. Participant agreement is separate from operational reservation state.

## Optional elements
Optional additions such as an afterward café visit are clearly marked as optional and do not block the primary meetup unless intentionally made required.

## Change request
Either participant can request changes to activity, date, time, venue, cost, or other details. Use neutral language such as **This meetup is no longer ready for final confirmation** and return the plan to the appropriate review state.

## Version integrity
Material changes create a new plan version and invalidate stale final confirmation. Example: v3 ready for review → venue changed → v4 needs review. No participant may confirm an obsolete version.

## Concurrent changes
If the plan changes while someone is reviewing or confirming:
> **The meetup changed while you were reviewing it.**

Action: **Review updated plan**.

The confirmation operation must revalidate plan version, participant state, reservation state, and required constraints against current server state before committing.

## Revalidation
Before final confirmation, revalidate applicable:
- venue availability/reservation status;
- participant eligibility/confirmation state;
- required constraints;
- current plan version.

Show factual loading states such as **Checking the latest meetup details…**.

## Unavailability or participant changes
If the venue becomes unavailable or the participant set changes:
> **The group changed before confirmation.**

or
> **This venue is no longer available.**

Return to planning or venue selection. Never silently confirm stale state.

## Final confirmation
Primary action: **Confirm meetup**.

Supporting: **Confirm that you will participate in the meetup shown above.**

Confirmation dialog should restate the essential current plan and explain that confirmation applies to that plan version and material changes may require review again.

## What confirmation means
It records the user's participation in the displayed plan version. It does not guarantee attendance, outcome, or permanent commitment.

## Partial confirmation
If only one participant confirms:
> **Your confirmation is saved.**
> **The meetup is waiting for the remaining required confirmation.**

Do not call it fully confirmed until actual confirmation conditions are satisfied.

## Operational confirmation
If both participants confirm but reservation is pending, show a distinct state such as **Participant-confirmed — operationally pending**. When reservation/payment succeeds, update to **Meetup confirmed** using canonical server state.

## Payment failure
> **Payment couldn't be completed.**

Supporting: **The meetup is not fully confirmed until the required reservation is completed.**

Actions: **Try again**, **Change payment method**, **Return to plan**.

## AI role
AI may summarize the final plan, explain unresolved fields, compare versions, compare alternatives, and answer factual questions from current structured data.

AI must not:
- approve for a participant;
- infer consent;
- confirm for another person;
- make payments;
- reserve venues autonomously;
- declare the meetup confirmed without system state;
- hide unresolved conditions;
- expose private constraints.

Example:
> **You have both confirmed the plan, but the venue reservation is still pending.**

## Notifications
Use neutral messages such as:
- **Your meetup is ready for final review.**
- **The meetup plan changed.**
- **The meetup was confirmed.**
- **The venue reservation is pending.**

Avoid artificial urgency.

## Safety
Keep **Safety Center**, **Report**, and **Block** accessible before and after confirmation.

## Accessibility
- Semantic final-plan structure
- Accessible confirmation controls
- Accessible version comparison
- Screen-reader-readable state
- Clear unresolved-field announcements
- Keyboard-accessible actions
- Accessible payment disclosure
- Accessible errors
- Accessible safety controls
- No color-only state meaning
- Reduced-motion support
- Focus preservation after confirmation/error

Example screen-reader summary:
> “Final meetup review. Version four. Board games. Sunday 6:30 PM. Board Game Café. Estimated cost ₹450 per person. Venue verified. Reservation pending. You are ready to confirm.”

## Responsive behavior
### Mobile
Plan version → final meetup summary → participant state → venue/reservation → cost → logistics → safety → confirm.

### Desktop
Left: final plan, activity, date, time, venue, cost, logistics. Right: participant confirmation, readiness, reservation, version changes, safety, confirm.

## Loading and error states
Loading examples: **Checking the latest plan…**, **Verifying venue status…**, **Checking participant confirmations…**, **Preparing final review…**.

Errors must be factual and retryable:
> **We couldn't load the latest meetup plan.**
> **We couldn't verify the latest meetup status.**

Do not allow stale confirmation where current state cannot be verified.

## Offline
> **You're offline. We haven't confirmed this meetup.**

Actions: **Retry when connected**, **Back**.

No local-only confirmation success.

## Reliability
Confirmation must be idempotent so repeated taps cannot create duplicate meetup records, bookings, payments, or notifications.

## Analytics
Track final-review view/start, plan version viewed/changed, participant confirmation start/save/pending, all-participant confirmation, reservation/payment states, full confirmation, AI summary/version-question actions, state verification failures, offline, and race-condition events. Do not store private participant hesitation, payment credentials, or sensitive conversation content in generic analytics.

## Product boundary
Screen 27 does not replace shared planning, silently edit the plan, infer consent, confirm for another participant, guarantee attendance, automatically charge users, assume reservation success, let AI determine confirmation, or expose private constraints. Its responsibility is to ensure both participants explicitly review the same final plan before the meetup crosses the confirmation boundary.

## Relationship to Screen 26
Screen 26 Shared Meetup Planning → required fields complete → Screen 27 Shared Final Review → both explicitly confirm → operational checks pass → Confirmed Meetup.

## Reuse existing confirmation logic
Reuse the canonical confirmation semantics already established for the product rather than introducing a second definition of **Confirmed**. The UX is a two-person shared review, while the underlying confirmation semantics remain consistent.

## Acceptance criteria
- Both participants review the same plan version.
- Planning agreement is distinct from final confirmation.
- Each participant confirms independently.
- Required operational conditions are revalidated.
- Reservation status is separate from participant consent.
- Payment requires explicit authorization.
- Material changes invalidate stale confirmation.
- AI cannot infer or provide consent.
- Private constraints remain protected.
- Offline/race-condition handling prevents false confirmation.
- Confirmation is idempotent.
- Safety controls remain accessible.
- Accessibility requirements are satisfied.

## Product principle
**We're both looking at exactly the same plan.** Each participant makes their own final decision, and only current verified system state can transition the meetup to confirmed.