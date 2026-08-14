# PYRINTU — UX SPECIFICATION
## Screen 18 — Group Chat v1.0

**Status:** Approved

## Core objective
Give the group a simple, safe place to communicate around the shared opportunity and plan. Chat supports questions, coordination, suggestions, updates, and human conversation. It must not become an infinite feed, popularity system, pressure mechanism, or replacement for the structured plan.

## Opening experience
**Heading:** Group conversation

Supporting: **Talk about the plan, ask questions, and coordinate together.**

At the top, show a compact plan reference with group name, participant count, and current plan state, with **View plan** linking to Screen 17.

## Chat header
Show group name, participant count, and current group state. Actions: **Group details**, **Safety**, **More**.

## Structured plan reminder
When conversation discusses a plan detail, surface a contextual reference to the current structured plan. Chat messages are conversation; structured plan fields are state. A message such as “6:30 works for me” must not silently become a confirmed plan change.

## Message composer
Placeholder: **Write a message…**. Keep the composer simple. Optional actions include Attach, Mention, and AI help.

## Text messaging
Support ordinary group messages with sender, time, and content. Avoid unnecessary engagement signals.

## No social-feed mechanics
Do not introduce follower counts, post counts, popularity rankings, engagement scores, reaction totals designed to drive participation, or infinite content discovery.

## Reactions
Lightweight reactions may be allowed, but they remain secondary. Do not expose “most reacted” or “top contributor” mechanics.

## Replies
Allow replies to messages where useful to preserve context.

## Message editing and deletion
Users may edit their own recent messages where supported. Show **Edited** after editing. Deletion must accurately distinguish **removed for everyone** vs **removed only for me** based on actual implementation.

## Media and links
Allow controlled sharing of images, venue screenshots, links, and appropriate documents. Link previews must identify the source and distinguish user-shared information from verified Pyrintu data.

## Chat-driven plan change proposals
A participant message such as “Let's make it 7 PM” must not automatically change the plan. Optionally detect **Possible plan change** and provide **Review proposed change**. The flow is Conversation → Proposal → Group review → Structured plan update.

## Lightweight coordination actions
Where relevant provide structured actions such as **Suggest time**, **Suggest venue**, **Suggest activity**, and **Ask a question**.

## Polls
Simple polls may help with coordination. Example: choosing between times. Poll results inform the plan but **Most votes ≠ automatically confirmed plan**. Structured confirmation remains separate.

## Poll privacy
Use aggregate responses where appropriate. Avoid unnecessary exposure such as identifying each participant’s sensitive vote.

## Neutral reminders
Coordinator or Pyrintu reminders must be neutral, e.g. “The group still needs to choose a venue.” Never use guilt or social-pressure language.

## Notifications
Useful notifications may include new group messages or plan changes. Avoid trivial or attention-grabbing notifications. Allow notification preferences such as all messages, important updates only, mute, and custom settings.

## Mentions
Mentions may notify participants, but the system must not facilitate pressure or harassment. Abuse signals belong to moderation.

## AI assistance
Optional **Ask Pyrintu** support can summarize what has been decided, identify what still needs a decision, turn a discussion into a plan proposal, or draft a neutral coordination message.

## AI chat summary
Summaries must be grounded in actual messages and structured plan state. Example summary: four participants are in the group; badminton is selected; Sunday evening is preferred; two venues are under consideration; exact venue remains undecided; café afterward is optional.

## AI plan extraction
When messages contain possible plan updates, AI may identify them as proposed changes. Example: venue, time, or estimated cost. The user must explicitly **Review changes**; no automatic mutation is allowed.

## AI message drafting
AI may draft a neutral message. The user must review and explicitly send it. AI must not speak for the user without explicit action.

## AI behavior boundaries
AI must not impersonate participants, send messages automatically without explicit authorization, pressure participants, claim someone agreed when they did not, expose private participant information, summarize private messages to unauthorized people, change structured plan state silently, fabricate facts, or act as moderator unless explicitly invoked for moderation functionality.

## Private context protection
Broader Pyrintu information must not leak into chat. Prefer decision-relevant group-safe wording over exposing another participant’s private preferences or behavior.

## Safety controls
Always accessible: **Report**, **Block**, **Leave group**, and **Safety Center**.

## Reporting
Message-level Report may include harassment, inappropriate content, spam, safety concern, suspicious behavior, or other. Reporting should not publicly identify the reporter unless policy requires it.

## Blocking
Participants can block another participant from a message or participant menu. Blocking follows platform privacy/contact rules and does not become a public group vote or announcement.

## Leaving the group
Provide **Leave group** with: “You can leave without explaining why.” Leaving does not silently delete the underlying intent.

## Moderation states
Possible states: Normal, Limited, Message removed, Participant restricted, Group paused, Group closed. User-facing moderation messages should be factual and non-shaming.

## Suspicious behavior
Safety systems may restrict content or participation. Ordinary users should not be exposed to unsupported algorithmic judgments about another participant.

## Group pause
If safety or moderation requires intervention: **This group is temporarily paused while an issue is reviewed.** Avoid speculation about who caused the pause.

## Closed group
If the group ends, show **This group is closed.** The conversation may become read-only according to retention and privacy rules.

## Plan confirmation indicator
When Screen 19 confirms the meetup, the chat should reflect structured state with a clear indicator such as **Meetup confirmed** and a link to **View confirmed plan**.

## Major plan changes
When the structured plan changes, show a system message such as “The meetup time changed from 6:30 PM to 7:00 PM.” with **Review plan**. This structured event is authoritative once confirmed and differs from a participant merely proposing a change in chat.

## Group announcements
Meaningful structured changes may appear as system messages, e.g. Activity confirmed, Venue changed, Plan awaiting review, Meetup confirmed, Meetup cancelled. System messages should be visually distinct from participant messages.

## Conversation search
Optional **Search conversation** may help users find terms such as venue, cost, or day. Search must respect visibility and deletion rules.

## Pinned information
A limited pinned **Group essentials** area may show activity, date, time, venue, and plan status. It links to Screen 17 rather than becoming a duplicate source of editable truth.

## No duplicated state
Pinned information must update from structured plan data. Do not maintain a separate manually edited “final plan” message that can diverge from Screen 17.

## Chat loading
Show **Loading conversation…** and render recent messages first. Do not block the initial experience on old history.

## Pagination
Load recent messages first and older history progressively when scrolling upward.

## Offline state
Show clearly that messages may not send until connected. Outgoing messages may be marked Sending, Pending, or Failed. Never display a failed message as delivered.

## Send failure
Show **Message couldn't be sent.** with **Retry** and **Delete** while preserving typed content where possible.

## Duplicate-send protection
Repeated taps must not create duplicate messages. Implementation should use an idempotent message identifier or equivalent mechanism.

## Message ordering
Messages must remain correctly ordered across late arrivals and connectivity changes. Show pending state rather than falsely indicating server acceptance.

## Accessibility
- Semantic message groups
- Sender and timestamp announced appropriately
- Keyboard-accessible composer
- Accessible attachments
- Reply context announced
- System messages distinguishable to screen readers
- Notification state accessible
- Report/Block/Leave controls accessible
- Reduced-motion support
- No color-only moderation state

Example screen-reader message: “Meera, 6:42 PM: I found a court near the metro.”

## Responsive behavior
### Mobile
Group header → Plan preview → Messages → Composer. Safety and settings remain one tap away.

### Desktop
Left: conversation. Right: group essentials, plan status, participants, open decisions, safety. The right rail is contextual, not a second feed.

## Analytics
Track chat view, message start/send/failure/edit/delete, replies, reactions, attachments, polls, plan-change detection/review/application, AI summaries, AI drafting, AI failures, notification opens/mutes, reports, blocks, leaving, and moderation states. Do not send raw message content or private conversations to generic analytics.

## Performance
- Recent messages load first.
- Older history loads progressively.
- Message sending feels immediate while clearly showing pending state.
- AI operates asynchronously.
- Attachments upload independently.
- Plan state loads separately from historical chat.
- No full-page reload after sending.

## Product boundary
Screen 18 does not become the primary planning source of truth, automatically confirm plans from messages, automatically book venues, reveal private participant data, replace structured decisions, create social popularity metrics, or pressure participants to reply. Its job is **conversation around a shared plan**.

## Relationship with Screen 17
Screen 17 is the structured Activity Plan. Screen 18 is the conversation around it. Chat can propose changes; the structured plan records approved state.

## Relationship with Screen 19
When the plan reaches the required state, Screen 19 handles Meetup Confirmation. Chat then reflects the confirmed structured state.

## Acceptance criteria
### Conversation
- Participants can communicate naturally.
- Replies and lightweight reactions are available.
- Media/link sharing is controlled.

### Planning integrity
- Chat does not silently change the plan.
- Proposed changes are reviewable.
- Structured plan remains the source of truth.

### AI
- AI summaries use verified conversation/plan data.
- AI cannot impersonate users.
- AI cannot expose private context.
- AI cannot act without explicit authorization.

### Privacy
- Private information is not unnecessarily exposed.
- Individual response states remain protected.

### Safety
- Report, Block, Leave, and Safety Center remain accessible.
- Moderation states are factual and non-shaming.

### Reliability
- Sending, pending, and failed states are clear.
- Duplicate sends are prevented.
- Offline behavior is honest.

### Accessibility
- Keyboard accessible.
- Screen-reader compatible.
- System messages and moderation states are distinguishable without color.

## Product principle
**Conversation is not the source of truth.** Chat supports the group; the structured plan remains authoritative.
