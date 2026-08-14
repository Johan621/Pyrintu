# PYRINTU — UX SPECIFICATION
## Screen 24 — Connection Home / Re-engagement v1.0

**Status:** Approved for implementation planning

## Core objective
Give mutually connected users one calm place to communicate, see shared context, start a new activity, plan another meetup, and manage privacy and safety. The connection home is a bounded coordination surface, not a social feed.

## Entry condition
Full access requires a verified mutual connection:

User A → continued interest + User B → continued interest → Mutual connection.

One-sided interest cannot open the direct connection home.

## Opening experience
**Heading:** Your connection

Supporting: **You both chose to stay connected after your meetup.**

## Connection summary
Show current, permitted context such as:
- Connection status
- How the connection started
- Shared interests
- Last interaction

Do not expose private preference or hidden recommendation information.

## Connection states
- **Active**
- **Quiet**
- **Paused**
- **Ended**
- **Blocked**

Only show the state supported by current system data.

## Primary actions
Keep three primary actions:
- **Message**
- **Plan something**
- **Explore**

Avoid competing primary actions.

## Conversation
Show a compact conversation preview and **Open conversation**. Direct conversation remains subject to privacy, moderation, reporting, blocking, and message controls.

## Shared context
Show mutually visible shared interests to support conversation and activity discovery. Never turn shared context into a compatibility score.

## Previous meetup
Show a concise historical reference with **View meetup**. Historical facts remain unchanged.

## New activity and meetup
**Plan something together** starts a new planning lifecycle. A future meetup is a separate object from the completed meetup:

Connection Home → New activity / intent → Planning → Participant review → Confirmation → New meetup.

The old meetup is historical context, not a reusable mutable object.

## Explore activities
Offer suggestions such as:
- Board games
- Coffee + walk
- Badminton again
- Startup event

Suggestions are optional. The previous activity is context, not a mandatory constraint.

## Recommendation logic
Recommendations may use mutually visible interests, previous activity preferences, recent shared context, user-selected goals, and planning constraints. Private information requires permission.

## AI assistance
Optional **Ask Pyrintu** can:
- Suggest a casual activity
- Suggest something inexpensive
- Suggest something different from the prior meetup
- Explain why an activity was suggested
- Draft a conversation opener

AI must not:
- infer attraction or emotional intent;
- reveal private preferences;
- expose hidden recommendation signals;
- message automatically;
- create a meetup without authorization;
- claim what the other person wants;
- manufacture shared interests;
- predict relationship outcomes.

Example draft:
> “Had fun last time. Want to try something different next weekend?”

Actions: **Use** / **Edit** / **Cancel**. Nothing is sent automatically.

## New meetup proposals
One participant may choose **Plan something together** and share a proposal. The other participant sees **A new meetup idea was shared with you** and can:
- **Review**
- **Maybe later**
- **Decline**

A proposal is not a meetup and is not automatically accepted.

## Proposal lifecycle
Draft → Shared → Under review → Accepted → Planning → Confirmed.

## Proposal rejection and Maybe later
Use neutral language such as **This idea wasn't accepted** or **Maybe later**. Never frame the decision as a personal rejection event and avoid repeated prompts.

## Multiple proposals
Prefer one active meetup proposal at a time to keep the connection state understandable.

## Privacy
Do not automatically reveal phone numbers, personal email, exact home locations, hidden preferences, or private recommendation signals.

Platform-approved communication is the default. Contact sharing, if supported, requires explicit confirmation.

## Location privacy
Use only the location information required for planning. Do not expose exact home locations or distance-to-home information.

## Connection settings
Provide access to:
- **Pause connection**
- **End connection**
- **Block**
- **Report**
- **Safety Center**

## Pause connection
**Pause this connection?**

Supporting: **You can pause future interaction without permanently ending the connection.**

State: **Connection paused** with **Resume connection**.

## End connection
**End this connection?**

Supporting: **You can stop future interaction. No explanation is required.**

State: **This connection has ended.**

Ended connections do not show messaging or meetup-creation controls.

## Block
Blocking is stronger than ending. Communication and visibility rules apply according to product policy. Do not expose a block as a social announcement.

## Report
**Report this connection** with reasons such as harassment, inappropriate behavior, suspicious behavior, safety concern, or other. Reporting remains confidential under platform policy.

## Recent activity
A bounded **Recent activity** section may show meaningful events such as a new meetup plan, conversation activity, and connection creation. This is not an infinite feed.

Do not add public posts, likes, followers, popularity metrics, engagement scores, streaks, or response-rate indicators.

## Re-engagement
For quiet connections, a neutral optional prompt such as **Want to try something together again?** may appear with **Explore activities** and **Not now**. Do not repeatedly nudge dormant connections.

Users may opt out of connection-specific suggestions.

## Connection-quality boundary
Do not provide relationship health scores or compatibility percentages. Use factual states such as Active or Quiet.

## Notifications
Useful notifications include:
- **Your connection sent a message.**
- **A new meetup plan is ready for review.**
- **Your connection shared an activity idea.**

Avoid emotionally manipulative wording and artificial urgency. Notification detail should respect privacy settings.

## Historical integrity
Past meetup activity, date, venue, confirmed state, and completion status remain historical and stable.

## AI uncertainty
When shared context is insufficient:
> **I don't have enough shared context to make a useful suggestion yet.**

Actions: **Explore activities** / **Tell Pyrintu what you're looking for**.

## AI user control
AI-generated recommendations should provide **Why?** and a way to mark a suggestion as not relevant where supported.

## Loading states
- Loading your connection…
- Checking the latest connection state…
- Finding relevant activity ideas…

Core connection status should load first.

## Error states
### Connection unavailable
> **We couldn't load the latest connection details.**

Action: **Retry**.

### Recommendations unavailable
> **Activity suggestions aren't available right now.**

Action: **Explore manually**.

### Proposal failed
> **We couldn't send this meetup idea.**

Actions: **Try again** / **Cancel**.

## Offline state
> **You're offline. Some connection information may be out of date.**

Disable actions requiring server confirmation and never present unconfirmed proposal or connection-state updates as successful.

## Reliability
Idempotent operations are required for sending meetup proposals, pausing, ending, blocking, sharing contact information, and starting new meetups. Repeated taps must not create duplicates.

## Race conditions
If connection state changes while the user is interacting:
> **This connection changed while you were here.**

Action: **Review latest connection**.

Do not authorize new actions using stale mutuality state.

## Accessibility
- Semantic headings
- Accessible primary actions
- Screen-reader-readable connection status
- Keyboard navigation
- Accessible message controls
- Accessible safety actions
- No color-only connection states
- Reduced-motion support
- Clear focus management

Example screen-reader summary:
> “Your connection. Status active. Connected after Sunday badminton meetup. Primary actions: Message, Plan something, Explore.”

## Responsive behavior
### Mobile
Connection header → Status → Conversation → Shared context → Previous meetup → Plan something → Explore → Recent activity → Safety / connection settings.

### Desktop
Left: conversation, shared context, previous meetup, recent activity.
Right: connection status, plan something, explore, AI assistance, connection controls, safety.

## Analytics
Track connection-home view, message opened, previous meetup opened, shared context viewed, planning started, activity exploration, AI actions, meetup proposal lifecycle, pause/resume/end/block/report actions, contact sharing, re-engagement impressions/dismissals, and errors. Do not store private message content, hidden relationship signals, or sensitive location information in generic analytics.

## Product boundary
Screen 24 does not predict relationship quality, turn the connection into a social feed, expose private preferences, automatically schedule or confirm a meetup, automatically share contact details, repeatedly pressure inactive users, or make AI the relationship authority. It is a controlled home for an established mutual connection and a safe path toward future interaction.

## Relationship to future screens
Screen 23 Continued Connection → Screen 24 Connection Home → future messaging, activity discovery, and planning experiences.

## Acceptance criteria
- Only mutually established connections can access the full connection home.
- Connection state is explicit.
- Messaging is available without engagement pressure.
- New meetup proposals are separate from confirmed meetups.
- Proposed meetups require independent review.
- Contact sharing is explicit.
- Pause / End / Block / Report remain accessible.
- No connection-quality score or infinite social feed.
- AI recommendations use permitted shared context.
- AI cannot infer emotions or relationship outcomes.
- Quiet connections are not repeatedly pressured.
- Historical meetup information remains stable.
- Race conditions and offline states are handled.
- Accessibility requirements are satisfied.

## Product principle
A mutual connection is **a permission to continue interacting**, not a promise that the relationship will continue.