# PYRINTU — UX SPECIFICATION
## Screen 29 — Meetup Day-of / Live Execution v1.0

**Status:** Approved for implementation planning

## Core objective
Provide a focused, low-friction day-of experience that helps participants find the confirmed meetup, access essential logistics, communicate when necessary, handle delays or changes, access safety controls, and transition cleanly into completion. This is an execution surface, not another planning interface.

## Opening experience
**Heading:** Your meetup is today

Supporting: **Here are the details you need to get there and meet safely.**

## Live status
Use clear operational states:
- Confirmed
- Today
- Starting soon
- In progress
- Completed

The current state must be obvious.

## Essential summary
Show the highest-priority details first: activity, time, venue, participant count, and reservation state.

## Countdown
A countdown such as **Starts in 42 min** may be useful close to the meetup, but should not become an anxiety-inducing mechanic and should transition away once the meetup begins.

## Arrival information
Show confirmed venue, verified address, relevant landmark, transport/parking guidance where available, and factual **Verified / Estimated / Suggested** status.

## Map and navigation
Provide **View location** and **Get directions**. External handoff should be clear where applicable. Never reveal participant home locations.

## Arrival guidance
Guidance such as arriving 10 minutes early should only be presented when supported by venue/activity requirements or clearly marked as a suggestion.

## Venue access and reservation
Show verified access instructions, reservation reference for authorized participants, and equipment requirements where supported. Never expose payment credentials or private transaction details.

## Participant display
Show only the participant information appropriate for the confirmed meetup. Do not expose home addresses, private contact details, hidden preferences, or live locations by default.

## Connection communication
Provide **Open conversation** in the meetup context.

## Quick coordination actions
Offer lightweight operational actions:
- **I'm on my way**
- **I'm here**
- **Running late**
- **Can't make it**

These signals are explicit, optional, and should not create social pressure.

## On-the-way / arrival privacy
The app may show neutral status such as **On the way** or **At venue**. Do not expose precise distance or live location by default.

## Running late
**Let the group know you're running late?**

Optional message can be edited before the user explicitly sends it. No automatic message without user action.

## Can't make it
**Can't make this meetup?**

Actions: **Cancel my participation** / **Keep meetup**. If cancellation affects validity, revalidate the confirmed state.

## Waiting and start states
Use neutral language such as **The other participant hasn't been marked as arrived** and **Meetup started**. Do not infer emotional outcomes or use shame language.

## During meetup
Keep the screen simple. Primary actions are **Open conversation**, **View venue details**, and **Safety**. Do not turn the page into a timer.

## Safety
Always accessible: **Safety Center**, **Report**, **Block**, and where appropriate **Leave meetup**. A participant may leave at any time without approval from the other participant.

## Safety-related exit
If the user indicates they do not feel safe, prioritize disengagement and safety tools. Do not force public explanation or continued interaction.

## Emergency boundary
Pyrintu must not pretend to replace emergency services. Safety escalation should follow supported geography and policy rather than invented emergency details.

## Venue / activity problems
If the venue is closed or the planned activity is unavailable, present factual problem states and actions such as **View alternatives**, **Contact venue** where supported, **Review alternatives**, or **Cancel meetup**. Never silently substitute another activity.

## External disruptions
Verified venue, transit, or weather disruptions may be surfaced as potential impacts. Do not automatically change the meetup time or cancel unless explicit product rules require it.

## Material operational changes
Material changes during the day must follow the existing change/review semantics:
Operational issue → change proposal → participant review → updated plan.
The confirmed state should not be silently rewritten.

## Day-of change examples
- time change
- venue change
- significant cost change

Each requires appropriate review/reconfirmation under the established confirmation and version rules.

## AI day-of assistant
Optional **Ask Pyrintu** can answer questions such as where the meetup is, booking reference, what changed, what to bring, or what options exist when a venue is unavailable.

AI must not:
- declare someone arrived without evidence;
- reveal live participant location;
- claim another participant is late unless verified;
- cancel or change the meetup autonomously;
- make payments without authorization;
- expose private safety reports;
- invent operational information.

## AI disruption handling
Example: if the venue is closed, AI should explain the verified state and available user-controlled options without automatically cancelling or replacing the meetup.

## Notifications
Use neutral operational notifications such as **Your meetup starts in 1 hour**, **A meetup detail changed**, **The venue reported an issue**, and **Your connection sent a message**. Avoid pressure such as "Hurry! They're waiting!".

## Notification frequency
Use limited day-of notifications: one upcoming reminder, immediate operational changes, and messages according to user settings. Avoid repeated reminders.

## Calendar
Show calendar status and allow users to open/update their calendar. Do not claim external synchronization succeeded unless it actually did.

## Completion transition
The meetup may transition to **Completed** using deterministic product rules such as participant action, activity completion, or scheduled operational state. Do not infer emotional outcome.

## Manual completion
Where supported, **End meetup** may be offered with a clear confirmation. Do not force completion at an exact time when the activity may reasonably continue.

## No-show
Avoid shaming language such as "no-showed you". Use neutral operational language such as **The meetup did not proceed as planned** and provide issue/report/complete/return options as appropriate.

## Offline
**You're offline. Some meetup information may be out of date.** Actions requiring live verification remain unavailable. Pending signals must remain visibly unconfirmed until server acknowledgement.

## Error states
Use factual, retryable errors for location, arrival status, and meetup-change updates. Never display a false successful state.

## Race conditions
If participants modify the meetup concurrently:
> **The meetup changed while you were updating it.**

Action: **Review latest details**. No silent overwrite.

## Reliability
Day-of actions must be idempotent, including on-the-way, arrived, late notice, leave/cancel, end meetup, and operational change acceptance. Repeated taps must not create duplicate events or notifications.

## Accessibility
- Clear day-of status
- Semantic meetup summary
- Screen-reader-readable arrival state
- Accessible quick actions
- Accessible safety controls
- Keyboard navigation
- Accessible disruption states
- No color-only state meaning
- Reduced-motion support
- Focus preservation
- Accessible confirmation dialogs

## Responsive behavior
### Mobile
Today's meetup → Time / Venue → Navigation → Arrival status → Quick actions → Operational changes → Safety.

### Desktop
Left: meetup details, location, arrival state, operational changes. Right: connection, quick actions, safety, AI assistant.

## Analytics
Track day-of view, navigation, arrival signals, running-late flow, cancellation/leave, safety actions, venue/activity problems, disruptions, change proposal/review/acceptance, AI actions, calendar access, completion, offline, race-condition, and operational error events. Do not store private live location, safety-report content, or sensitive participant behavior in generic analytics.

## Product boundary
Screen 29 does not replace confirmed meetup state, expose live participant location by default, infer emotional reactions, shame late/no-show participants, automatically cancel the meetup, replace emergency services, let AI control the meetup, or silently change the confirmed plan. Its responsibility is to make the real-world meetup easier to execute while preserving autonomy, privacy, safety, and operational accuracy.

## Relationship to Screen 28
Screen 28 Confirmed Meetup Operations → meetup day begins → Screen 29 Day-of Execution → Starting soon → On the way / Arrived → In progress → Completed → Screen 30 Final Post-Meetup State.

## Reuse existing systems
Reuse confirmed meetup state, venue/reservation state, safety controls, change/version system, connection communication, notification infrastructure, and completion lifecycle. Do not create competing definitions for Confirmed, Cancelled, Reservation confirmed, or Participant confirmed.

## Acceptance criteria
- Essential day-of information is immediately visible.
- Navigation never exposes private participant locations.
- Arrival signals are explicit and optional.
- Running-late communication requires user action.
- Safety exit is always accessible.
- Venue/activity disruptions are handled without silent substitution.
- Material day-of changes trigger appropriate review.
- AI remains operationally advisory.
- Offline and race-condition states are explicit.
- Day-of actions are idempotent.
- No emotional pressure or shame language.
- Completion transitions into Screen 30 cleanly.
- Accessibility requirements are satisfied.

## Product principle
**I know where to go, what I need to do, and what I can do if something changes.** The day-of experience supports execution without taking control away from the participant.
