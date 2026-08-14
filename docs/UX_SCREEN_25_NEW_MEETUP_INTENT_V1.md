# PYRINTU — UX SPECIFICATION
## Screen 25 — New Meetup Intent / Proposal v1.0

**Status:** Approved for implementation planning

## Core objective
Allow a mutually connected pair to express that they would like to do something together again. Collect a fresh meetup intent and turn it into a reviewable proposal before planning begins.

## Opening experience
**Heading:** What should we do next?

Supporting: **Start with what you'd enjoy. The details can be planned together.**

## Connection context
Show the connection and how it began, without forcing the prior activity as the new activity.

## New intent choices
- **Something similar**
- **Something different**
- **I have an idea**
- **I'm open**

Previous meetup details are context only.

## Previous-activity carry-over
Offer: **Use last activity as a starting point?** with **Yes** / **Choose something else**. Never silently inherit the previous activity.

## Natural-language intent
Allow a user to describe what they want. Extract only information actually expressed. Distinguish explicit information, preferences, and unknowns.

Example interpretation:
- Goal: Spend time together again
- Timing: Next weekend
- Style: Casual
- Environment: Quiet
- Activity: Not selected yet

Ask the user to review the interpretation before continuing.

## Activity direction
Offer broad directions such as Café, Walk, Board games, Badminton, Workshop, Explore outdoors, or Something else. Detailed activity selection remains downstream.

## Timing, budget, location, environment
Allow flexible or exact timing, optional budget ranges, broad areas, and environment preferences. Do not require exact home addresses.

## Accessibility
Allow relevant accessibility requirements to be provided privately for planning. Do not expose them to the connection unless the user explicitly chooses to share them.

## Proposal preview
Show a clear summary such as:

**Something casual and conversation-focused**  
Saturday evening  
Quiet environment  
Around ₹500/person  
Area: Gachibowli

Actions: **Share idea** / **Edit**.

## Proposal boundary
A meetup idea is an invitation to explore a meetup idea. It is not a booking request, confirmed meetup, or expectation that the other person accepts.

## Sharing and recipient experience
After sending: **Meetup idea shared** with neutral language. Recipient sees **A new meetup idea** and can **Review**, **Maybe later**, or **Not for me**.

## Recipient states
- Reviewing
- Interested
- Maybe later
- Declined

Recipient response is private until the appropriate proposal state is established.

## Two-sided interest gate
Planning begins only when the required conditions are satisfied:

Creator creates idea → recipient reviews → both interested → begin planning.

One-sided interest does not start planning.

## Proposal editing and versioning
Material edits such as activity direction, day/time, major budget, or substantially different location create a new proposal version and require re-review.

Use: **This meetup idea changed. Please review the updated version.**

## AI assistance
AI may suggest relevant activities and explain why they fit the user's expressed intent. It may help draft the proposal wording.

AI must not:
- assume what the other person wants;
- reveal private preferences;
- create or send a proposal without the user's action;
- choose a final venue;
- book anything;
- claim mutual agreement;
- manufacture shared interests.

AI draft actions: **Use** / **Edit** / **Cancel**. Nothing is sent automatically.

## Privacy
Creator preferences remain private unless intentionally shared. Recipient receives only information required for meaningful proposal review and planning.

## Conversation boundary
Chat does not automatically create a proposal. Where supported, a user may explicitly choose **Turn this into a meetup idea**.

## Proposal-to-plan transition
When both sides are interested:

**You're both interested. Ready to plan the details?**

Action: **Start planning**.

The existing downstream Activity Selection, Activity Plan, and Meetup Confirmation flows remain responsible for planning and confirmation.

## Safety
Keep **Report**, **Block**, and **Safety Center** accessible. Connection ending or blocking invalidates further proposal actions according to connection state.

## Empty and exit states
**Not sure yet?** can lead to **Explore ideas**, **Describe what I'm looking for**, or **Not now**.

Leaving before sharing may show **Discard this meetup idea?** with **Discard** / **Keep editing**.

No artificial urgency or repeated prompts.

## Notifications
Neutral examples:
- **Your meetup idea was shared.**
- **A new meetup idea is ready to review.**

Avoid emotionally manipulative wording. Lock-screen details should respect privacy settings.

## Reliability
Idempotency is required for creating, updating, sharing, accepting, declining proposals, and starting planning. Repeated actions must not create duplicates.

## Race conditions
If connection state changes while a proposal is being sent:

**This connection changed while you were sending the idea.**

Action: **Review connection**.

Revalidate mutual connection state before creating the proposal.

## Offline
**You're offline. This meetup idea hasn't been shared yet.**

Actions: **Retry** / **Save draft**.

Do not show the proposal as shared until server confirmation exists.

## Error states
**We couldn't share this meetup idea.** → **Try again** / **Keep draft**.

**Suggestions aren't available right now.** → **Create the idea manually**.

## Accessibility
- Semantic headings
- Accessible intent controls
- Accessible timing and budget choices
- Keyboard navigation
- Screen-reader-readable proposal states
- Accessible confirmation dialogs
- Accessible privacy explanation
- Accessible safety controls
- No color-only proposal state
- Reduced-motion support
- Focus preservation

## Responsive behavior
### Mobile
Connection context → intent input → activity direction → timing → budget → location/environment → proposal preview → share.

### Desktop
Left: intent builder and preferences. Right: proposal preview, AI suggestions, and connection context.

## Analytics
Track intent start, natural-language interpretation, edits, submission, proposal share/review/interest/maybe/decline, proposal versions, planning start, AI actions, failures, and connection-state changes. Do not store private preferences or hidden recipient responses in generic analytics.

## Product boundary
Screen 25 does not create a confirmed meetup, book or charge anything, expose private preferences, assume the previous activity, assume mutual interest, replace Activity Selection / Activity Plan / Meetup Confirmation, or let AI act autonomously.

## Acceptance criteria
- New meetup starts from fresh explicit intent.
- Previous meetup is context, not an automatic template.
- Proposal is separate from a meetup.
- Recipient independently reviews the proposal.
- One-sided interest does not start planning.
- Material changes require re-review.
- Private preferences remain protected.
- AI is advisory only.
- No booking/payment occurs here.
- Safety controls remain available.
- Offline and race-condition states are handled.
- Proposal lifecycle is explicit.

## Product principle
**I have an idea for doing something together again → They can decide whether they're interested → Only after we're both interested do we start making a real plan.**
