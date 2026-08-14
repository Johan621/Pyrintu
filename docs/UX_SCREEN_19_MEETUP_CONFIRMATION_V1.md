# PYRINTU — UX SPECIFICATION
## Screen 19 — Meetup Confirmation v1.0

**Status:** Approved

## Core objective
Give every participant a final, unambiguous review of the meetup before confirmation. Show what, when, where, cost, who, optional elements, verified state, and what happens next.

## Opening
**Ready to confirm the meetup?**

Supporting: **Review the final details before you confirm your participation.**

Avoid pressure language or artificial urgency.

## Final meetup summary
Show the current structured plan: activity, date, time, venue, location, duration, cost state, participant count, and reservation state. Every value must come from current structured state.

## Confirmation states
Distinguish clearly between:
- Meetup not yet confirmed
- Meetup confirmed

## Final review checklist
Show activity, date, time, venue, estimated/confirmed cost, participant status, and safety information. Any unresolved required field must either block final confirmation or be explicitly surfaced.

## Confirmation eligibility
Conceptually:
- required plan fields complete
- required participant confirmations complete
- group/opportunity still valid
- safety eligibility satisfied
- required reservation conditions satisfied

Eligibility is deterministic; AI cannot decide it.

## Required vs optional
Required fields may include activity, date, time, venue/area, participant state, and required reservation conditions. Optional elements such as a café extension must not block confirmation unless explicitly defined as required.

## Activity
Show the main activity, duration, and confirmation state. Optional extensions must be clearly separated from the main activity.

## Date and time
Show exact confirmed values only when actually confirmed. Flexible or proposed timing must remain labeled as such.

## Venue and reservation boundary
Keep these states separate:
**Venue selected → Venue confirmed → Reservation confirmed.**
A venue being selected or confirmed does not automatically mean a reservation exists.

Possible reservation states:
- Not required
- Pending
- Confirmed
- Failed

## Cost and payment
Show estimated vs verified vs confirmed cost, including relevant mandatory fees. Never hide mandatory costs. Any payment must require explicit authorization before charging.

Example disclosure: **This reservation will charge ₹400 to the selected payment method.**

No automatic payment.

## Participant confirmation
Show aggregate status such as **4 of 4 participants confirmed** or **Waiting for 1 required confirmation**. Protect individual participant responses where privacy requires it.

## Participant changes
If someone withdraws before confirmation, re-check the meetup requirements. Never silently replace a participant without revalidation.

## Deadlines
Only show operational deadlines backed by real constraints, such as a reservation expiration. Never use fabricated countdowns.

## Final confirmation
Primary CTA: **Confirm meetup**.

Confirmation dialog:
- Repeat essential details
- State that confirmation records participation under the shown details
- Actions: **Confirm meetup** / **Review again**

## Meaning of confirmation
Confirmation means the participant's participation is recorded, the current meetup details become the active confirmed state, and material later changes may require reconfirmation.

Confirmation does not guarantee chemistry, attendance, safety, or future relationship outcomes.

## Post-confirmation state
Show **Meetup confirmed** with the complete structured summary, participant count, cost state, and reservation state.

Actions may include:
- View meetup
- Open group chat
- Add to calendar
- Set reminder preferences

## Confirmation receipt
Provide a concise receipt-like record containing date, time, venue, activity, participant count, cost state, reservation state, and a reference where supported.

## Calendar and reminders
Allow calendar integration from the confirmed structured state. Avoid excessive reminders and never turn tentative plans into misleading confirmed calendar events.

## Location privacy
Reveal only necessary meetup location details. Never expose participants' home addresses or exact private locations.

## Safety
Keep **Safety Center**, **Report**, and **Block** accessible. Provide basic public-meetup guidance. Required legal/operational acknowledgments should only be used when actually necessary.

## Post-confirmation changes
Confirmed meetups must not silently change. Material changes such as date, significant time, venue, cost, activity, or major participant changes can trigger revalidation/reconfirmation. Minor informational changes should not unnecessarily interrupt participants.

## Cancellation
Participants can cancel their participation without guilt. A cancelled meetup should be clearly marked cancelled and may offer **Find another opportunity** while preserving appropriate group/intent history.

## External disruptions
For venue failures or verified external conditions, surface factual state and offer review/alternative actions. Do not auto-cancel unless explicit product rules require it.

## AI role
AI may:
- summarize the final meetup
- explain confirmation state
- identify unresolved details
- explain changes
- draft neutral reminders

AI must not:
- declare a meetup confirmed
- override participant confirmation
- make payments
- reserve venues without explicit authorization
- claim everyone confirmed without verified state
- expose private responses
- modify confirmed details silently

## Confirmation loading
Use truthful states such as **Checking the final meetup details…**, **Confirming participant status…**, and **Verifying the reservation…** only for actual operations.

## Errors
### Confirmation failed
**We couldn't confirm the meetup yet.** Your current plan remains saved. Provide retry/review actions.

### Payment failed
The meetup is not fully confirmed until required payment succeeds.

### Participant race condition
If a participant changes state during confirmation, stop stale confirmation and ask the user to review the updated meetup.

### Venue race condition
If venue availability changes during confirmation, do not confirm the stale venue; allow another venue to be selected.

### Offline
**You're offline. We haven't confirmed the meetup.** Never show false success based only on local state.

## Idempotency / reliability
Repeated confirmation attempts must not create duplicate bookings, charges, meetup records, or notifications. Confirmation state must be revalidated before the final commit.

## Accessibility
- Semantic final-summary structure
- Fully keyboard-accessible confirmation dialog
- Screen-reader announcement of confirmation success/failure
- Accessible cost/payment disclosure
- No color-only confirmation state
- Safety actions accessible
- Focus management after dialogs and errors
- Reduced-motion support

## Responsive behavior
### Mobile
Final meetup summary → participants → venue/reservation → cost → safety → confirmation action.

### Desktop
Left: final meetup details. Right: participant state, reservation state, safety, confirmation CTA.

## Analytics
Track confirmation view, final-detail views, participant/reservation/cost views, confirmation start/success/failure, payment start/success/failure, calendar/reminder actions, material-change detection, reconfirmation, participant/venue changes, cancellation, and AI question/suggestion events. Do not collect private payment information, raw participant responses, or sensitive chat text in generic analytics.

## Performance
Load the final plan quickly; load participant and reservation state independently where possible; keep confirmation responsive; prevent duplicate submissions; revalidate stale state before final commit.

## Product boundary
Screen 19 does not guarantee safety, chemistry, attendance, or relationship outcomes. It does not silently charge, book, expose private participant responses, or let AI become the authority. It creates the final explicit participation commitment.

## Handoff
Planning → Final review → Explicit confirmation → Confirmed meetup. After confirmation, the primary user state becomes an upcoming meetup.

## Acceptance criteria
### Final clarity
- Complete final plan is visible.
- Confirmed/estimated/pending states are obvious.
- Participant state is accurate.

### Consent
- Confirmation is explicit.
- User understands what it means.
- Material changes can require reconfirmation.

### Booking/payment
- Venue reservation is separate from meetup confirmation.
- Charges require explicit authorization.
- Failed payment/reservation never appears successful.

### Privacy
- Individual responses remain protected.
- Personal location/contact information is not exposed unnecessarily.

### AI
- AI explains structured state.
- AI cannot confirm, book, or pay autonomously.

### Reliability
- Race conditions are handled.
- Offline confirmation cannot create false success.
- Duplicate confirmation is prevented.

### Safety
- Safety controls remain accessible.
- Cancellation remains possible.

### Accessibility
- Keyboard accessible.
- Screen-reader compatible.
- No color-only state communication.

## Product principle
**I know exactly what I'm agreeing to, nothing was confirmed behind my back, and the confirmed meetup remains visible as structured state.**
