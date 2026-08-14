# PYRINTU — UX SPECIFICATION
## Screen 30 — Final Post-Meetup State v1.0

**Status:** Approved for implementation planning

## Core objective
Close the meetup lifecycle cleanly after completion. Support lightweight private reflection, safety reporting, continued-connection choice, historical access, and a return to the main product without pressure or automatic follow-up.

## Opening experience
**Heading:** Meetup complete

Supporting: **Your meetup has ended. You can reflect, report anything important, or decide what you'd like to do next.**

## Completed meetup summary
Show canonical historical activity, date/time, venue, participant count, and completed status.

## Historical integrity
Once complete, core historical facts remain stable. Later preferences do not rewrite the historical meetup record.

## Reflection
Optional choices: **Good**, **Okay**, **Not for me**, **Skip**. No mandatory star rating. Reflection is private by default.

## Safety
Show **Did anything feel unsafe?** with **No**, **Yes**, and **Prefer not to say**. A Yes response can open **Report a safety concern**. Reporting remains private according to platform rules and can happen after leaving the venue.

## Issue reporting
Support appropriate categories such as harassment, inappropriate behavior, unsafe environment, boundary concern, suspicious activity, and other. Do not publicly expose the reporter or private details.

## Continued connection
If relevant, ask **Would you like to stay connected?** with **Yes**, **Maybe**, **No**, and **Skip**. These choices remain independent and private. Existing mutuality rules from the connection flow continue to apply.

## Mutuality
If both participants independently choose to continue, show **You both want to stay connected** and allow **Open connection**. One-sided interest remains private.

## No-pressure behavior
Do not use guilt, urgency, public rejection, or repeated nudges. The user can finish without making a relationship decision.

## New opportunity
If the user wants another experience, **Explore opportunities** returns to discovery/intent rather than automatically creating a meetup.

## Repeat activity
Optional choices such as **Same activity**, **Something different**, and **Not now** create future recommendation context only; they do not create a confirmed plan.

## Conversation access
Where a mutual connection exists, provide **Open connection**. Do not expose a direct connection channel without verified mutuality.

## AI role
AI may answer authorized historical questions and help draft private feedback. AI must not reveal private participant feedback, infer feelings, predict relationship outcomes, claim mutuality without verified signals, rewrite historical facts, or submit safety reports automatically.

## Completed vs cancelled vs disrupted
Keep **Completed**, **Cancelled**, and **Disrupted** distinct. For cancelled or disrupted meetups, use neutral language and route to history, reporting, or discovery as appropriate.

## No-show
Do not shame participants or label someone as having stood the other person up. Use neutral operational language such as **The meetup did not proceed as planned**.

## Connection ending
Choosing **No** saves the preference privately. Choosing **Maybe** leaves the connection unresolved without pressure. No public rejection event is generated.

## Privacy
Historical meetup access remains governed by the existing privacy model. Private participant information, feedback, and hidden interest states are not exposed.

## Safety availability
Keep **Safety Center**, **Report**, and **Block** available after completion. Users can report later if needed.

## Accessibility
- Semantic completion summary
- Accessible reflection controls
- Accessible safety/report flow
- Screen-reader-readable meetup state
- Keyboard navigation
- No color-only sentiment states
- Reduced-motion support
- Focus preservation

## Responsive behavior
### Mobile
Completed meetup → reflection → safety → connection choice → next action → Done.

### Desktop
Left: meetup summary/history. Right: reflection, safety, connection, and next action.

## Analytics
Track post-meetup view, reflection start/complete/skip, safety/report actions, connection choices, verified mutuality reveal, connection opening, opportunity exploration, feedback-draft actions, AI use, history access, and errors. Do not store private feedback text, safety-report content, or hidden participant decisions in generic analytics.

## Product boundary
Screen 30 does not become a social feed, force ratings, expose private feedback, infer relationship outcomes, automatically create another meetup, automatically reconnect people, replace discovery or connection systems, or let AI act autonomously.

Its responsibility is to **close the meetup lifecycle and return control to the user**.

## Relationship to Screen 29
Screen 29 Meetup Day-of / Live Execution → meetup completed → Screen 30 Final Post-Meetup State → reflection / safety / connection / discovery / done.

## Acceptance criteria
- Completed meetup state is explicit.
- Reflection is optional and private.
- Safety reporting remains accessible after completion.
- Continued-connection choice is independent and private.
- Mutuality is revealed only after verified independent signals.
- New meetup creation requires explicit user action.
- Historical facts remain stable.
- Completed, cancelled, and disrupted states remain distinct.
- AI remains advisory and privacy-preserving.
- No pressure or forced rating.
- Accessibility requirements are satisfied.

## Product principle
**Close the experience cleanly. Let the user decide what happens next.**
