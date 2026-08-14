# PYRINTU — UX SPECIFICATION
## Screen 20 — Upcoming Meetup v1.0

**Status:** Approved for implementation planning

## Core objective
Give a participant one reliable place to prepare for and manage an already-confirmed meetup. The screen is the bridge from confirmation to the real-world event.

## Opening experience
**Heading:** Your upcoming meetup

Example: **Sunday Badminton + Café**

Supporting: **Sunday · 6:30 PM · Smash Arena**

Status: **Confirmed**

## Primary summary
Show the current confirmed state:
- Activity
- Date
- Time
- Venue
- Participant count
- Cost status
- Reservation status

All values come from the structured confirmed meetup state.

## Countdown
A compact time-to-meet indicator may be shown when useful.

Use factual language such as **Starts Sunday at 6:30 PM**. Avoid anxiety-inducing countdowns or artificial urgency.

## What happens next
Provide a simple preparation sequence:
1. Review meetup details
2. Check directions/logistics
3. Prepare for the activity
4. Join the group when ready
5. Meet at the confirmed venue

Do not create unnecessary tasks.

## Venue and directions
Show the confirmed venue and appropriate location details.

Actions:
- **Get directions**
- **View venue**
- **View map**

Do not expose participant home locations.

## Arrival guidance
Where verified or clearly framed as a suggestion:
- Suggested arrival time
- Entrance/check-in guidance
- Equipment requirements
- Venue rules

Unknown information must remain marked unknown.

## What to bring
Show activity-specific preparation only when grounded in verified requirements or explicit group information.

Example:
- Comfortable sportswear
- Required equipment, if venue specifies it

Do not invent requirements.

## Cost reminder
Show:
- Confirmed amount when known
- Estimated amount when still variable
- Optional costs separately
- Reservation/payment state

Example: **₹350 estimated per person · café optional**.

## Participant overview
Show the confirmed participant count and group-safe participant information.

Do not expose private availability, hidden preferences, private intent notes, safety settings, or personal contact details automatically.

## Group access
Provide:
- **Open group chat**
- **View group details**
- **View confirmed plan**

Chat remains conversation; the confirmed structured plan remains authoritative.

## Meetup status
Possible states:
- Confirmed
- Starting soon
- In progress
- Completed
- Cancelled
- Disrupted

Only show the state supported by current system data.

## Starting soon
When the meetup approaches:
> **Your meetup starts soon.**

Show only useful operational guidance such as venue, arrival time, and contact/report controls.

Do not create pressure with repetitive alerts.

## Day-of changes
If the venue, time, activity, or participant composition changes materially:
> **Your meetup details changed.**

Show:
- Previous value
- New value
- Reason or source when safely available

Action: **Review updated meetup**

Material changes may require reconfirmation under Screen 19 rules.

## Venue disruption
If the reservation or venue becomes unavailable:
> **The confirmed venue is no longer available.**

Actions:
- **Review alternatives**
- **View updated plan**

Do not silently substitute a venue.

## Activity disruption
If the activity is cancelled or materially changed:
> **The activity changed.**

Action: **Review meetup**

Do not mark the meetup as unchanged.

## Weather/external disruption
When verified external conditions materially affect the meetup:
> **Conditions may affect your meetup.**

Provide verified information and available next actions. Do not invent forecasts or automatically cancel without product rules.

## Cancellation
Participant action:
**Cancel my participation**

Supporting:
> **You can step back from the meetup.**

Do not use guilt language.

## Group cancellation
If the meetup is cancelled:
> **This meetup was cancelled.**

Provide the factual reason when safe and appropriate.

Action: **Find another opportunity** where applicable.

## Safety
Keep these controls accessible:
- **Safety Center**
- **Report**
- **Block**
- **Leave/cancel participation**

Provide concise public-meetup guidance.

## Contact information
Do not automatically expose phone numbers or email addresses. Existing product-approved group communication should be preferred.

## AI assistance
Optional **Ask Pyrintu** can answer:
- What time is the meetup?
- Where is the venue?
- What do I need to bring?
- What changed?
- What is still optional?

AI must answer from the confirmed structured state and verified operational information.

AI must not:
- Invent logistics
- Predict another participant's behavior
- Reveal private information
- Change the meetup state
- Confirm a reservation it cannot verify
- Send messages without explicit authorization

## AI uncertainty
When data is incomplete:
> **I don't have verified information for that yet.**

Then direct the user to the appropriate source or action.

## Notifications
Useful notifications include:
- Meetup reminder
- Material meetup change
- Venue disruption
- Cancellation
- Safety/moderation update

Avoid repeated low-value notifications and artificial urgency.

## Calendar
Provide **Add to calendar** using the confirmed structured meetup details.

If the meetup changes materially, the calendar update should follow product rules.

## Loading states
- Loading confirmed meetup…
- Checking the latest meetup details…
- Refreshing venue status…

Core confirmed information should appear first.

## Error states
### Meetup unavailable
> **We couldn't load the latest meetup details.**

Actions: Retry, Open group chat.

### Venue status unavailable
> **We couldn't refresh venue status.**

Keep the last known state clearly marked as potentially stale.

## Offline state
> **You're offline. Some meetup information may be out of date.**

Disable actions requiring server confirmation and never present stale data as newly verified.

## Reliability
- Idempotent cancellation/update actions
- No duplicate notifications from repeated taps
- Clear pending vs confirmed states
- Revalidate stale meetup state before material actions

## Accessibility
- Semantic headings
- Screen-reader-readable confirmed state
- Accessible map/directions actions
- Keyboard-accessible controls
- No color-only status communication
- Focus preservation after updates/errors
- Reduced-motion support

Example screen-reader summary:
> “Upcoming meetup. Sunday 6:30 PM. Smash Arena. Badminton. Four participants. Status confirmed. Estimated cost ₹350 to ₹400 per person. View directions button.”

## Responsive behavior
### Mobile
Confirmed meetup → Status → Venue → Directions → What to bring → Cost → Participants → Group actions → Safety

### Desktop
Left: meetup summary, venue, logistics, preparation.
Right: status, participant summary, group actions, safety, Ask Pyrintu.

## Analytics
Track meetup view, directions opened, venue viewed, calendar added, preparation viewed, group opened, AI questions, reminders opened, material-change review, disruption viewed, cancellation started/completed, safety/report/block actions, and errors. Do not send private participant data or sensitive location history to generic analytics.

## Product boundary
Screen 20 does not replace the confirmed plan, create new commitments, silently alter logistics, expose private participant information, or make AI the authority. It is the participant's operational home for an already-confirmed meetup.

## Relationship to previous screens
Screen 19 Meetup Confirmation → Screen 20 Upcoming Meetup → Day-of / Post-meetup experiences.

## Acceptance criteria
- Confirmed meetup state is obvious.
- Structured plan remains authoritative.
- Logistics are actionable but factual.
- Preparation guidance is evidence-based.
- Material changes are surfaced and can trigger revalidation.
- Cancellation remains available.
- Safety controls remain accessible.
- AI is grounded and read-only by default.
- Offline/stale states are explicit.
- Accessibility requirements are satisfied.

## Product principle
After confirmation, Pyrintu should move from **decision support** to **calm operational support**: clear details, useful preparation, minimal noise, and no hidden changes.