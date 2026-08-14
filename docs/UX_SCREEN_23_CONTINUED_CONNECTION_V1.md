# PYRINTU — UX SPECIFICATION
## Screen 23 — Continued Connection v1.0

**Status:** Approved for implementation planning

## Core objective
Help participants decide privately whether they want to continue a connection after a completed meetup. The screen asks “Would I like to continue this connection?” and does not infer or expose what another person feels.

## Opening experience
**Heading:** Would you like to stay connected?

Supporting: **The meetup is complete. You can choose what you'd like to do next.**

No pressure, countdown, or expectation that continuation is required.

## Private decision
Choices:
- **Yes** — I'd like to stay connected.
- **Maybe** — I'm open to another interaction later.
- **No** — I don't want to continue this connection.
- **Skip for now**

The initial choice is private.

## Privacy and mutuality
One-sided interest is never revealed. The relationship transition is:

User A → Yes + User B → Yes → Mutual continued interest.

When both independently choose to continue:

**You both want to stay connected.**

Supporting: **There's mutual interest in continuing the connection.**

Reveal only the minimum fact necessary to establish mutuality; do not expose response timing, private reflection, ratings, or internal scores.

## Maybe state
**Maybe** is neither Yes nor No. It represents uncertainty and does not create a commitment signal.

## Post-mutuality actions
After mutuality is verified, offer:
- **Keep chatting**
- **Meet again**
- **Explore another activity**
- **Stay connected for now**

Selecting **Meet again** does not automatically create a meetup.

## Direct connection boundary
A one-to-one connection becomes available only after the product’s mutuality rules are satisfied:

Group context → Private preference → Mutual interest → Direct connection.

No unilateral direct-contact transition.

## New meetup separation
A future meetup is a separate lifecycle object:

Past Meetup → Continued Connection → New Intent / Opportunity → New Group or Connection Plan → New Meetup.

Historical information remains intact.

## Activity continuity
Offer:
- Same activity
- Similar activity
- Something completely different

Previous activity is historical context, not a mandatory constraint.

## Contact information
Do not automatically reveal phone numbers, email addresses, or home addresses. Use platform-approved communication by default.

If supported:
**Share your contact information**

Before disclosure:
> Share your phone number with this connection?

Actions: **Share** / **Not now**.

## Connection profile
Show only information the person has chosen to make visible in this context, such as display name, profile image, shared interests, relevant activity history, and user-approved bio. Never expose private system reasoning.

## Connection reasoning
Do not show compatibility scores. Use grounded facts such as:
> You connected through a shared interest and both chose to continue after the meetup.

## AI role
AI may:
- summarize how the connection began;
- suggest conversation starters;
- suggest new activities;
- explain current connection status;
- help draft a message;
- help create a new meetup intent.

AI must not:
- infer the other person’s feelings;
- reveal private decisions;
- claim mutuality before both signals exist;
- send messages automatically;
- create a meetup without authorization;
- pressure the user to continue;
- predict relationship outcomes.

Example AI draft:
> “I enjoyed the badminton session. Would you be up for trying another activity sometime?”

Actions: **Use** / **Edit** / **Cancel**. Nothing is sent automatically.

## Safety
Keep **Report**, **Block**, and **Safety Center** accessible after mutuality.

**Stop this connection** is available at any time. Supporting: **You can stop future interaction at any time.** No explanation required.

## Notifications
Useful examples:
- **You both chose to stay connected.**
- **Your connection has a new message.**
- **A new meetup plan was shared with you.**

Avoid emotionally manipulative wording such as “Someone likes you!”. Notification detail should respect privacy settings.

## Reconnection
A later **Reconnect** action may require a fresh independent signal; do not assume old interest remains current.

If an interest signal becomes stale according to product rules:
> **This connection signal is no longer current.**

## Historical integrity
Past meetup facts remain fixed. Later preferences add current state without rewriting historical records.

## No automatic second meetup
Choosing **Yes** to continued connection does not create a group, invite, reservation, booking, or meetup automatically.

## Mutual interest arriving later
Independent responses may occur at different times. If A chooses Yes and B later chooses Yes, mutuality can then be revealed.

## Race conditions
If the connection changes while the user responds, revalidate before revealing mutuality:
> **This connection changed while you were responding.**

Action: **Review connection**.

## Offline
> **You're offline. We haven't saved your preference yet.**

Actions: **Retry** / **Skip for now**.

Do not display mutuality until the saved state is confirmed.

## Error states
### Preference save failed
> **We couldn't save your preference.**

Actions: **Try again** / **Done without saving**.

### Connection unavailable
> **We couldn't load the latest connection state.**

Action: **Retry**.

## Reliability
Idempotent operations are required for saving preferences, stopping connections, sharing contact details, starting a new intent, and starting a new meetup plan. Repeated taps must not duplicate records.

## Accessibility
- Semantic headings
- Accessible Yes / Maybe / No controls
- Screen-reader-readable mutuality state
- Clear privacy language
- Keyboard accessibility
- Accessible connection actions
- Accessible block/report controls
- No color-only state communication
- Reduced-motion support
- Focus preservation after state changes

Example screen-reader summary:
> “Continued connection. Meetup completed. Your preference has not been selected. Yes, Maybe, No, and Skip for now options.”

## Responsive behavior
### Mobile
Meetup summary → Continued-connection choice → Result → Next action → Safety.

### Desktop
Left: meetup context and connection summary. Right: private decision, current state, next actions, safety.

## Analytics
Track screen view, choice started, Yes/Maybe/No/Skip selection, mutuality revealed, connection opened, message started, new meetup started, new intent started, contact sharing, stop connection, reconnect, AI actions, report/block actions, save failures, and state changes. Do not store raw private reflection, hidden interest states, or sensitive connection content in generic analytics.

## Product boundary
Screen 23 does not guarantee friendship or romance, predict relationship outcomes, expose one-sided interest, automatically create another meetup, automatically exchange contact details, force continued interaction, or make AI the relationship authority.

## Relationship to future screens
Screen 22 Meetup Completion → Screen 23 Continued Connection → future connection / re-engagement experiences.

## Acceptance criteria
- Post-meetup choice is private by default.
- Yes / Maybe / No are equally valid.
- One-sided interest is never exposed.
- Mutuality requires independent signals and is revealed only when verified.
- Contact sharing is explicit.
- New meetup creation requires user action.
- AI cannot infer feelings or relationship outcomes.
- Blocking/reporting remain available.
- Reconnection does not rely blindly on stale consent.
- Historical meetup facts remain stable.
- Race conditions and offline states are explicit.
- No artificial urgency.
- Accessibility requirements are satisfied.

## Product principle
After a meetup, Pyrintu should say: **“You decide what happens next.”** The system facilitates independent choices and reveals mutuality only when both sides have independently expressed it.