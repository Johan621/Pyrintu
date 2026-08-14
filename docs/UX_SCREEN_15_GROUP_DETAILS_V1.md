# PYRINTU — UX SPECIFICATION
## Screen 15 — Group Details v1.0

**Status:** Approved

## Core objective
Provide one trustworthy place for participants to understand and coordinate the group after Group Creation. The screen is the shared source of truth for group identity, participants, purpose, current plan, open decisions, activity, safety, and group state.

## Opening experience
**Heading:** Your group

Example: **Sunday Badminton + Café**

Supporting: **4 people · Ready to plan**

The state must reflect the actual group lifecycle.

## Group status
Possible states:
- Ready to plan
- Planning
- Plan proposed
- Awaiting confirmation
- Meetup confirmed
- Meetup completed
- Closed

Only display the current valid state. Do not show Meetup confirmed simply because the group exists.

## Group purpose
Show what the group is about, grounded in the original intent and opportunity.

Example: A small group interested in badminton and meeting new people through a relaxed activity.

## Participants
Show who is here. Possible group-safe participant information includes display name, profile image, selected shared interests, and relevant activity context.

Do not expose private availability, hidden preferences, private intent wording, personal contact information, or unrelated sensitive information.

## Participant profile preview
Tapping a participant opens a limited group-safe profile. Information shown must follow privacy rules.

## Group privacy boundary
Information shared inside the group may include relevant profile information, shared activity, group planning information, and meetup decisions. Private availability, hidden preferences, private intent notes, safety preferences, AI conversations, and personal contact information are not automatically visible.

## Group formation explanation
Provide **Why this group formed** with grounded explanation: everyone independently wanted to continue with the opportunity and the group met the conditions needed to form.

## Shared interests
Show lightweight conversation starters such as badminton, startups, or cafés. Do not convert this into a compatibility score.

## Group differences
Where useful, communicate group-level differences without exposing which participant has a private preference unless explicitly appropriate. Example: some participants prefer quieter environments while others are comfortable with livelier places.

## Current activity
Show the activity, duration, optional components, and whether each element is proposed or confirmed.

## Current plan
Show day, time, area, venue, and activity. Every field must have a state such as Confirmed, Proposed, Needs decision, or Unknown.

## Open decisions
Show remaining decisions clearly, e.g. exact venue, optional café stop, final arrival time. Provide one meaningful next action such as **Help plan**.

## Group decisions
Allow participants to participate in decisions without turning the experience into a generic project-management dashboard.

## Decision provenance
Show where important decisions came from, e.g. original opportunity vs participant/group planning.

## Activity state
Suggested → Shortlisted → Chosen → Confirmed.

Do not jump directly from Suggested to Confirmed.

## Plan state
No plan → Planning → Plan proposed → Participants reviewing → Confirmed.

## Group coordination
Provide a compact coordination area focused on the next meaningful action. Do not overload participants with controls.

## Group chat entry
Chat belongs to the group but is secondary to the shared group state. Show a small preview and an action to open chat. Chat is handled in Screen 18.

## Notifications
Use neutral, non-addictive update indicators. Avoid attention-grabbing counters or artificial urgency.

## Read status
Avoid unnecessary social-pressure mechanics such as mandatory read receipts or “X saw your message” behavior.

## Coordinator
An optional coordinator may help organize logistics. Coordination authority must not grant access to private participant information.

## Coordinator actions
Possible actions include suggesting plans, organizing activity options, summarizing decisions, and sending neutral reminders. A coordinator cannot access hidden data, force decisions, add people without permission, or confirm a meetup alone unless explicitly authorized by product rules.

## Group-level AI assistant
Optional **Ask about this group** capability can answer questions about current verified group state, open decisions, and planning status.

AI may summarize verified state, draft neutral coordination messages, explain why the group exists, identify conflicts, and suggest next steps. AI must not reveal private information, invent decisions, claim someone agreed when they did not, change the plan silently, add/remove participants, or guarantee the meetup.

## AI group summary
Example:
- Four participants are in the group.
- Badminton is the selected activity.
- Sunday evening is proposed.
- Exact venue still needs to be chosen.
- Café afterward is optional.

## AI planning suggestion
AI may suggest one concrete next planning step, such as reviewing shortlisted venues. Suggestions are advisory.

## Group description/title editing
Allow controlled edits. Changes should be visible to participants and must not silently rewrite the underlying opportunity or intent.

## Change history
Show a lightweight list of meaningful group-state changes, not a massive audit log.

## Major change handling
Major changes such as activity, significant time/location, material cost, or group composition changes may require participant reconfirmation. Show clearly when the plan changed and ask users to review it.

## Leaving the group
Always provide **Leave group**. Users can leave without explaining why. Leaving must not silently delete the underlying intent.

## Report and block
Always accessible **Report** and **Block** controls. Reporting can target participant, group content, activity/venue, or another safety concern. Blocking should follow platform visibility/contact rules without becoming a public group decision.

## Safety center
Provide visible access to Safety Center and basic public-meetup guidance. Safety controls must remain available regardless of onboarding progress.

## Group closure
Groups may close after meetup completion, participant withdrawal, opportunity expiry, cancellation, or safety/moderation action. Closed groups should no longer be actionable.

## Re-form group
If a group collapses before the meetup, allow explicit actions such as finding another opportunity or creating a new group from the existing intent. Never recreate automatically without user participation.

## Empty activity state
If no activity is selected, clearly state that the group is ready but activity selection is still needed, with a **Choose activity** action.

## Empty plan state
If activity exists but no plan exists, show **No meetup plan yet** with a **Start planning** action.

## Loading states
Examples:
- Loading your group…
- Checking the latest group updates…
- Refreshing the plan…

Core group identity should appear quickly.

## Error states
### Group unavailable
We couldn't load the latest group details. Actions: Retry, Open chat.

### Plan update failure
We couldn't update the group plan. The previous plan remains active. Actions: Retry, Review.

## Stale-state recovery
If the group changes while viewing, show that it changed and provide a **Review latest version** action. Never silently overwrite another participant's change.

## Offline state
Clearly indicate when group information may be stale and disable actions that require server confirmation.

## First-time guide
Guide 07 targets **Group Details** with: “See who is in the group, why the group was formed, and what the group is planning.” The guide must not obscure safety-critical controls.

## Accessibility
- Semantic headings
- Accessible participant list
- Clear group status
- Screen-reader-readable plan states
- Keyboard-accessible actions
- Accessible decision controls
- Accessible safety controls
- No color-only state indicators
- Focus preservation after updates
- Reduced-motion support

Example screen-reader summary: “Sunday Badminton Group. Four participants. Status: planning. Activity: badminton, proposed. Time: Sunday 6:30 PM, proposed. Venue: not confirmed. Two decisions remain.”

## Responsive behavior
### Mobile
Group identity → Status → Participants → Purpose → Activity → Current plan → Still to decide → Chat preview → Safety → Group actions.

### Desktop
Left: group identity, participants, purpose, activity, plan. Right: group status, open decisions, chat preview, AI summary, safety.

## Analytics
Track view, participant/purpose/plan/open-decision/status views, chat preview, AI summary requests/completions, title/description edits, major-change review, change reconfirmation, leave/report/block/safety actions, and stale/error events. Do not include private participant data or raw chat content in generic analytics.

## Performance
- Group identity loads first.
- Participant data can progressively load.
- Chat preview can load independently.
- AI summary is asynchronous.
- Stale-state detection must be reliable.
- Updates should not require full-page reloads.

## Product boundary
Screen 15 does not finalize the meetup, automatically choose a final venue, confirm attendance, replace the activity-planning workflow, turn the group into a social feed, or expose hidden participant information. It is the shared source of truth, not the final planning engine.

## Relationship with other screens
Screen 14 Group Creation → Screen 15 Group Details → Screen 16 Activity Selection → Screen 17 Activity Plan → Screen 18 Group Chat → Screen 19 Meetup Confirmation.

## Acceptance criteria
### Group understanding
- User knows why the group exists.
- User knows who is participating.
- Current group status is clear.
- Confirmed vs proposed details are distinguishable.

### Coordination
- Open decisions are visible.
- Next action is clear.
- Major changes can trigger revalidation.

### Privacy
- Participant information is minimized.
- Private availability and preferences remain private.
- Contact details are not automatically shared.

### AI
- AI summarizes actual group state.
- AI cannot invent or silently change decisions.

### Safety
- Report, Block, Leave, and Safety Center remain accessible.

### Reliability
- Stale updates are detected.
- Previous valid state is preserved after failed updates.
- Offline state is clear.

### Accessibility
- Keyboard accessible.
- Screen-reader compatible.
- Status is understandable without color.

## Product principle
The group should feel like a shared coordination container, not a feed: **People + Purpose + State + Plan + Decisions + Safety**.
