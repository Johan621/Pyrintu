# PYRINTU — UX SPECIFICATION
## Screen 21 — Meetup Day-of v1.0

**Status:** Ready for implementation planning

## Core objective
Provide a calm, operational experience on the day of a confirmed meetup: help participants arrive, handle verified changes, communicate safely, and understand the current meetup state without creating pressure.

## Opening experience
**Heading:** Today’s meetup

Show the confirmed activity, time, venue, and current status from the structured meetup state.

Example:
- **Badminton + Café**
- **Today · 6:30 PM**
- **Smash Arena · Gachibowli**
- **Status: Confirmed**

## Primary actions
- **Get directions**
- **View confirmed plan**
- **Open group chat**
- **Safety Center**

Only show actions supported by current state.

## Day-of status
Possible states:
- Confirmed
- Starting soon
- Arrived / in progress
- Disrupted
- Completed
- Cancelled

Do not infer arrival solely from opening the screen or location access.

## Arrival guidance
Show concise, factual guidance such as:
- suggested arrival time
- entrance/check-in instructions
- venue rules
- equipment requirements

Unknown information remains explicitly unknown.

## Directions
Provide map/directions actions using the confirmed venue only. Never expose participant home locations or infer private travel routes.

## Meet-at venue guidance
If useful, show a neutral coordination point:
> **Meet inside the venue at the main entrance.**

Do not require users to share live location.

## Group coordination
Provide a lightweight day-of coordination strip:
- **Open group chat**
- **Ask about arrival**
- **Report a problem**

Do not create pressure such as “Everyone is waiting for you.”

## Late arrival
Allow a participant to indicate:
- **Running late**
- **Can't make it**
- **Need help**

These are operational signals, not public judgments.

Where appropriate, surface an aggregate message such as:
> **One participant has indicated they may be late.**

Do not expose private reasons unnecessarily.

## Meetup changes
If the confirmed venue, time, activity, or participant composition changes materially:
> **Your meetup details changed.**

Show the previous and new values and provide **Review updated meetup**.

Material changes may require reconfirmation under Screen 19 rules.

## Venue disruption
If a venue becomes unavailable:
> **The confirmed venue is no longer available.**

Actions:
- **Review alternatives**
- **View updated plan**

Never silently substitute a venue.

## Activity disruption
If the activity changes or is cancelled:
> **The activity changed.**

Action: **Review meetup**

The UI must reflect the new structured state rather than preserving stale confirmation language.

## Weather / external conditions
Show only verified external information.

Example:
> **Conditions may affect your meetup.**

Actions depend on available verified alternatives. Do not invent forecasts or automatically cancel without explicit product rules.

## Safety
Keep **Safety Center**, **Report**, **Block**, and **Leave/cancel participation** accessible.

Provide concise public-meetup guidance without overwhelming the user.

## AI assistance
Optional **Ask Pyrintu** can answer:
- Where is the venue?
- What should I bring?
- What changed today?
- What is still confirmed?
- What should I do if I am running late?

AI must use the current structured meetup state and verified operational information.

AI must not:
- invent logistics
- reveal private participant data
- predict another participant’s behavior
- mark attendance automatically
- change meetup state
- send messages without explicit authorization

## Notifications
Useful day-of notifications:
- meetup starting soon
- material plan change
- venue disruption
- cancellation
- safety/moderation update

Avoid repetitive low-value alerts and artificial urgency.

## Calendar
Allow access to the confirmed calendar entry. Updates must follow the structured meetup state.

## Check-in / arrival confirmation
If the product later supports explicit check-in, it must be user initiated and clearly labeled.

Do not infer attendance automatically from passive location signals.

## Completion handoff
When the meetup is over:
> **Meetup completed**

Provide **View meetup history** and continue to the post-meetup experience.

## Loading states
- Loading today’s meetup…
- Checking the latest meetup details…
- Refreshing venue status…

Core confirmed details should appear first.

## Error states
### Meetup unavailable
> **We couldn't load the latest meetup details.**

Actions: Retry, Open group chat.

### Venue status unavailable
> **We couldn't refresh venue status.**

Keep the last known state visibly marked as potentially stale.

## Offline state
> **You're offline. Some meetup information may be out of date.**

Disable actions requiring server confirmation and never present stale data as newly verified.

## Reliability
- idempotent late/cancel/report actions
- no duplicate notifications from repeated taps
- clear pending vs confirmed operational states
- revalidate stale meetup data before material actions

## Accessibility
- semantic headings
- screen-reader-readable meetup status
- accessible directions and map actions
- keyboard-accessible controls
- no color-only state communication
- focus preservation after updates/errors
- reduced-motion support

Example screen-reader summary:
> “Today’s meetup. Badminton. 6:30 PM. Smash Arena. Four participants. Status confirmed. Get directions button. Open group chat button.”

## Responsive behavior
### Mobile
Meetup summary → Status → Directions → Arrival guidance → Changes → Group actions → Safety

### Desktop
Left: confirmed meetup and logistics. Right: current status, changes, group actions, safety, Ask Pyrintu.

## Analytics
Track day-of meetup view, directions opened, venue viewed, group opened, late signal submitted, cancellation started/completed, material-change review, disruption viewed, safety/report/block actions, AI questions, and errors. Do not send precise private location history, message content, or private participant data to generic analytics.

## Product boundary
Screen 21 does not replace the confirmed plan, expose private participant movement, infer attendance from passive location, create new commitments, or make AI the authority. It is the calm operational surface for the day of the meetup.

## Relationship to previous screens
Screen 20 Upcoming Meetup → Screen 21 Meetup Day-of → Screen 22 Meetup Completion / Post-Meetup transition.

## Acceptance criteria
- Current meetup state is obvious and derived from structured data.
- Day-of actions are factual and useful.
- No passive attendance or location inference is required.
- Material changes are surfaced and can trigger revalidation.
- Safety controls remain accessible.
- AI is grounded and read-only by default.
- Offline/stale states are explicit.
- Accessibility requirements are satisfied.

## Product principle
On meetup day, Pyrintu should become **quiet operational support**: help people arrive, adapt to verified changes, and stay safe without turning the experience into a notification machine.
