# PYRINTU — UX SPECIFICATION
## Screen 22 — Meetup Completion / Post-Meetup Transition v1.0

**Status:** Approved for implementation planning

## Core objective
Close a completed meetup cleanly and transition the participant into reflection, safety reporting, future preferences, continued connection, or moving on.

## Opening experience
**Heading:** How did it go?

**Supporting:** Your meetup is complete. Take a moment to reflect on the experience.

Avoid mandatory ratings or pressure-oriented language.

## Completed meetup summary
Show the structured historical state:
- Activity
- Date
- Venue
- Participant count
- Completion state

Do not rewrite historical facts when current preferences change.

## Completion state
Possible lifecycle:
Scheduled → Started → In progress → Completed → Closed

Only mark the meetup completed using the product's defined operational rules; scheduled end time alone must not create a false completion state.

## Reflection
Offer optional private reflection states:
- It went well
- It was okay
- It wasn't a good fit

These are private outcome signals, not public judgments about participants.

## No forced rating
Do not require stars or a numerical score.
Primary: **Done**
Optional: **Share feedback**

## Private feedback
Feedback is private by default and must not be exposed as participant ratings.

## Safety feedback
**Anything felt unsafe?**
Options: Yes / No / I'd rather not say

If Yes: **Report a safety concern**

Reporting remains available after the meetup and must not publicly identify the reporter.

## Participant continuation preference
Optional: **Would you be comfortable meeting this group again?**
- Yes
- Maybe
- No

Treat this as an independent private signal. One participant's positive answer is not mutuality.

## Repeat opportunity
**Do something like this again?**
- Same activity
- Similar activity
- Something different

This may refine or create an intent, but must not automatically create another meetup.

## Existing intent
If the underlying intent remains active:
> Your current intent is still active.

Action: **View my intent**

## New intent
Action: **Create a new intent**

Do not alter historical meetup data when creating a new intent.

## Meetup history
Completed meetups become historical records with stable details.

Example:
**Past Meetup — Badminton + Café — Sunday — 4 participants — Completed**

## Group closure
After completion the group may transition from Active → Completed → Archived according to product rules.

## Post-meetup group chat
The group conversation may remain available for follow-up or become read-only according to retention rules.

Show: **This meetup is complete.**

## Continued connection
Optional: **Keep the connection going**

Possible responses: Yes / Maybe later / No

Do not automatically establish an ongoing relationship from a completed meetup.

## Continued mutuality
Only independent continued-interest signals from the relevant participants can establish mutuality. Do not infer mutuality from chat frequency, tone, or AI interpretation.

## No-contact outcome
If the user chooses No:
> Your preference is saved privately.

No public rejection event should be generated.

## Feedback categories
Optional private feedback:
- Activity: Great fit / Okay / Not for me
- Venue: Great / Fine / Could be better
- Planning: Easy / Some friction / Difficult
- Overall: Positive / Neutral / Negative

## Improvement suggestions
**What should Pyrintu do better?**
Possible categories:
- Better venue options
- Better activity suggestions
- Easier planning
- Better timing suggestions
- Better group fit
- Other

Optional; users can skip.

## Disrupted meetup
A meetup may end as **Disrupted** rather than Completed.

Show:
> This meetup ended unexpectedly.

Actions: **Tell us what happened**, **Report a safety concern**

## No-show handling
Do not publicly label absent participants negatively. Use neutral operational language and privacy-preserving attendance signals.

## AI assistance
Optional **Ask Pyrintu** may answer questions about the completed meetup using verified historical and user-owned data.

AI may draft private feedback, but must not submit it automatically.

AI must not:
- reveal private feedback or safety reports
- infer another participant's feelings
- claim everyone enjoyed the meetup
- create relationships automatically
- send follow-up messages without explicit authorization
- rewrite historical meetup facts

## Successful completion
**Heading:** Meetup complete

**Supporting:** Thanks for taking part. Your feedback can help Pyrintu improve future opportunities.

Primary: **Done**
Optional: **Share feedback**

## Negative/neutral outcomes
Neutral and negative reflections should be acknowledged without blame or guilt and should not trigger public participant judgments.

## Post-meetup reporting
Users may report issues after returning home. Do not impose an arbitrary short reporting window unless required by policy.

## Loading states
- Loading your completed meetup…
- Saving your feedback…
- Updating your preferences…

## Error states
### Feedback save failed
> We couldn't save your feedback.

Actions: **Try again**, **Skip**

### History unavailable
> We couldn't load your meetup history.

Action: **Retry**

A feedback failure must not erase the completed meetup.

## Offline state
> You're offline. Your feedback hasn't been saved yet.

Never claim feedback was submitted until server confirmation.

## Reliability
Important operations should be idempotent:
- save feedback
- report concern
- change continued-interest preference
- archive meetup

Repeated taps must not create duplicate records or reports.

## Accessibility
- Semantic headings
- Accessible reflection controls
- Clear completion state
- Keyboard-accessible feedback
- Screen-reader-readable status
- No color-only sentiment states
- Accessible report flow
- Accessible dialogs
- Reduced-motion support
- Focus preservation after saves/errors

## Responsive behavior
### Mobile
Meetup summary → Completion state → Reflection → Optional feedback → Continue-connection choice → Safety → Done

### Desktop
Left: meetup summary and history.
Right: reflection, feedback, continued connection, safety.

## Analytics
Track completion view, feedback started/submitted/skipped, activity/venue/planning/overall feedback, safety report started/submitted, continuation preference, history view, group reopen, AI summary/feedback draft usage, disruption view, and relevant errors. Do not send raw feedback text, safety reports, or private participant information to generic analytics.

## Product boundary
Screen 22 does not automatically create another meetup, publicly rate participants, reveal private feedback, infer mutual continued interest, permanently close safety/reporting channels, rewrite historical meetup data, or make AI responsible for relationship decisions.

Its job is to close the completed meetup cleanly and transition the user into the next appropriate state.

## Relationship to previous screens
Screen 19 Meetup Confirmation → Screen 20 Upcoming Meetup → Screen 21 Meetup Day-of → Screen 22 Meetup Completion → Screen 23+ post-meetup / continued connection experiences.

## Acceptance criteria
- Completed state is explicit.
- Feedback is optional and private by default.
- Safety reporting remains available.
- Continued interest is independent and private.
- Mutual continued interest requires independent signals.
- Historical meetup data remains stable.
- AI is grounded and read-only unless explicitly authorized.
- No forced rating or social pressure.
- Offline and save failures are recoverable.
- Accessibility requirements are satisfied.

## Product principle
After the meetup, Pyrintu should feel like: **That experience is complete. I can reflect, keep what was useful, report anything important, and decide what happens next.**