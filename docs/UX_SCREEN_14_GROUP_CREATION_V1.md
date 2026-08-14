# PYRINTU — UX SPECIFICATION
## Screen 14 — Group Creation v1.0

**Status:** Approved

## 1. Core objective

Create a Pyrintu group from a mutually supported opportunity while preserving consent, participant privacy, clear expectations, group purpose, group size, safety, and reversibility before meetup confirmation.

The screen answers:

> What group are we creating, who is it for, and what happens next?

## 2. Opening experience

### Heading

**Your group is ready to take shape.**

Supporting text:

> The required mutual interest is in place. Let's confirm the group details before we create it.

Avoid language implying permanent commitment.

## 3. Group identity

Every group has a clear purpose.

Example:

**Badminton + Café — Sunday**

> A small group for badminton and relaxed conversation.

Title is generated from actual opportunity data and may be edited where appropriate.

## 4. Group description

**What this group is about**

Example:

> A small group interested in playing badminton and meeting new people in a relaxed setting this Sunday.

Keep descriptions concise and grounded in verified opportunity data. Avoid unsupported personality claims.

## 5. Group purpose

Show:

- Activity
- Social objective
- Timing
- Location area

Example:

```text
Activity
Badminton

Purpose
Meet new people through a shared activity

When
Sunday evening

Area
Gachibowli
```

## 6. Participants

Show the confirmed group roster, for example:

```text
4 participants

You
Aarav
Meera
Rohan
```

Only disclose information appropriate to group formation.

## 7. Participant consent state

Participants must satisfy the required group-entry conditions. Internally this may include `mutuality_confirmed`, `group_eligible`, and `consent_current`.

User-facing copy:

> All required participants have independently agreed to continue.

Do not expose internal state names unnecessarily.

## 8. Group size

Show current size and any capacity:

**Current size: 4**

**Maximum: 5**

If the group can grow, make that explicit.

## 9. Group size lock

When the formation threshold is reached:

> Group size is currently set at four.

If expansion is permitted:

> One additional participant may be added if everyone remains eligible and the group still fits its intent.

No silent expansion.

## 10. Additional participants

Where supported:

### Can this group grow?

- Keep this group closed
- Allow one more participant

Require explicit permission where appropriate.

## 11. Why someone was included

### Why these people are here

> Everyone independently expressed interest in this opportunity, and the group meets the required activity, timing, and participation conditions.

No unsupported psychological compatibility claims.

## 12. Group-level fit

### Why this group works

Example signals:

- Shared activity
- Compatible group size
- Overlapping availability
- Mutual interest
- Current intent alignment

Do not reduce this to an opaque score.

## 13. Group expectations

### What to expect

> You'll be able to discuss the activity, coordinate details, and decide together whether the proposed plan works.

Always state:

> Joining the group does not automatically mean the meetup is confirmed.

## 14. Group vs meetup

```text
Group
People + shared context + coordination

Meetup
Specific time + place + activity plan
```

The group may exist before final meetup details.

## 15. Group status

Possible states include:

- Forming
- Ready to plan
- Planning

Use only the actual deterministic state. Do not say “Confirmed” unless the meetup is actually confirmed.

## 16. Group creation action

Primary CTA:

**Create group**

Before creation:

> You'll be added to this Pyrintu group with the participants shown above.

Secondary:

**Review details**

## 17. Explicit confirmation

Confirmation should show:

- participants
- group purpose
- group size
- current plan status

Example:

> **Create this group?**
>
> 4 participants  
> Badminton + café  
> Sunday evening  
> Gachibowli  
> Meetup details still being planned

Actions:

**Create group**

**Go back**

## 18. Group created state

Success:

# **Your group is ready.**

> Everyone can now coordinate here.

Primary:

**Open group**

Secondary:

**View opportunity**

Destination: Screen 15 — Group Details.

## 19. Immediate group experience

Do not automatically force the user into chat. Group entry should first expose:

- group purpose
- participants
- current activity
- planning state

Then offer:

**Open group**

**View plan**

## 20. Group description editing

Allow description edits where appropriate, but do not silently change the underlying intent or opportunity.

## 21. Group title editing

Limited renaming is acceptable. Avoid names that misrepresent the opportunity.

## 22. Group ownership

Avoid a single-person owner model for ordinary social groups. Prefer participants as the group entity, with narrowly scoped administrative capabilities only where needed.

## 23. Group roles

Possible roles:

- Participant — default
- Coordinator — optional logistics support
- Moderator — reserved for authorized Pyrintu operational/safety functions

Coordinator access must not expose private participant data.

## 24. Coordinator selection

Where coordination helps:

> Would you like someone to help coordinate the plan?

Options:

- Let Pyrintu suggest
- We'll choose later

Do not infer unsupported personality traits such as “natural leader.”

## 25. Group coordination

The group may later decide:

- exact time
- exact venue
- activity details
- transportation considerations
- optional post-activity plans

Screen 14 creates the group container; it does not solve every planning detail.

## 26. Group safety

Provide visible safety guidance:

> Meet in a public place and keep personal information private until you are comfortable.

Actions:

**Safety center**

**Report**

**Leave group**

These controls stay accessible.

## 27. Leave-before-meetup

Message:

> Leave this group?
>
> You can leave without explaining why. Your current intent will remain available unless you choose to change it.

Actions:

**Leave group** / **Stay**

## 28. Group collapse

If membership falls below requirements:

> This group no longer meets the conditions needed to continue.

Possible actions:

- Reform the group
- Find another opportunity
- End group

Do not auto-replace people without explicit product rules.

## 29. Participant replacement

If another participant is needed:

> The group needs another participant to continue.

Do not expose who left or why unless separately authorized.

Potential action:

**Look for another eligible participant**

## 30. Revalidation

Before replacement or other membership changes, re-check:

```text
Intent compatibility
Availability
Group size
Safety eligibility
Opportunity validity
Current mutuality conditions
```

Never assume the old opportunity is still valid.

## 31. Group privacy

The group is a new privacy boundary. Shared information may include relevant profile information, activity interests, and coordination details.

Do not automatically include:

- hidden availability
- private safety preferences
- unrelated profile data
- private AI conversations
- personal contact details

## 32. Contact information

Do not automatically expose phone numbers or email addresses when the group is created. Participants decide later whether and when to exchange contact details.

## 33. AI role

AI may:

- summarize why the group formed
- generate a concise group title from verified opportunity data
- draft a group description
- summarize planning constraints
- suggest coordination prompts
- answer questions about group state

AI must not:

- invent participant characteristics
- reveal private information
- declare unsupported compatibility
- automatically assign authority
- claim the meetup is confirmed when it is not
- change group membership by itself

## 34. AI-generated group description review

Any generated description must be reviewable before publication.

Example:

> **Suggested description**

Actions:

**Use** / **Edit** / **Write my own**

Use grounded wording such as:

> A small group interested in badminton and meeting new people this Sunday.

## 35. Group creation loading

> Creating your group…

Then:

> Setting up your shared space…

Avoid fake percentage progress.

## 36. Creation error

> We couldn't create the group right now.

> Your mutuality status is still safe. Nothing has been committed twice.

Actions:

**Try again** / **Go back**

## 37. Participant state changed during creation

> The group changed before it could be created.

> Pyrintu needs to check whether the opportunity still meets the group requirements.

Action:

**Review updated group**

Do not create a stale group.

## 38. Opportunity expired during creation

> This opportunity is no longer available.

> Your current intent is still active.

Action:

**Find another opportunity**

## 39. Offline state

> You're offline. We haven't created the group yet.

Action:

**Retry when connected**

Never show misleading success.

## 40. Group-created success state

```text
Group created ✓

Participants
4

Purpose
Badminton + café

State
Ready to plan
```

Primary:

**Open group**

## 41. First-time guide

Guide 07 target: **Group Details**

Message:

> See who is in the group, why the group was formed, and what the group is planning.

## 42. Accessibility

Requirements:

- accessible participant list
- semantic group summary
- clear confirmation language
- keyboard-accessible creation flow
- screen-reader announcement of success/failure
- group status announced
- safety controls always reachable
- dialogs properly focus-managed
- no color-only state indicators
- reduced-motion support

Example announcement:

> Group ready to create. Four participants. Meetup not yet confirmed. Create group button.

## 43. Responsive behavior

### Mobile

```text
Group purpose
↓
Participants
↓
Why this group
↓
Group size
↓
What happens next
↓
Privacy & safety
↓
Create group
```

### Desktop

```text
LEFT
Group identity
Participants
Purpose

RIGHT
Why group formed
Status
Privacy
Safety
Create group
```

## 44. Analytics

Track:

```text
group_creation_viewed
group_creation_started
group_participants_viewed
group_reasoning_viewed
group_size_viewed
group_additional_participant_setting_changed
group_title_edit_started
group_description_edit_started
group_ai_description_generated
group_ai_description_accepted
group_ai_description_edited
group_ai_description_rejected
group_creation_confirmed
group_created
group_creation_failed
group_creation_state_changed
group_participant_changed_during_creation
group_creation_expired
group_creation_abandoned
group_safety_viewed
group_leave_started
```

Do not send private participant data or raw generated descriptions to generic analytics.

## 45. Performance

- show the group preview immediately
- do not block preview on AI
- creation requests should be idempotent
- retries must not create duplicate groups
- stale membership must be revalidated
- success appears only after confirmed creation

The UX contract requires these properties even though implementation details belong in architecture.

## 46. Group creation state model

```text
Mutual opportunity
       ↓
Group creation review
       ↓
Creating
       ↓
Group created
       ↓
Ready to plan
```

Failure branches:

```text
Creating → State changed → Revalidation
```

or:

```text
Creating → Failed → Retry
```

## 47. Product boundary

Screen 14 does not:

- finalize the meetup
- determine the exact venue
- create the activity plan
- force users into chat
- expose private contact details
- guarantee the meetup will happen
- permanently lock group membership

It creates the shared social container.

## 48. Handoff to Screen 15

```text
Screen 14 — Group Creation
        ↓
Screen 15 — Group Details
        ↓
Activity
        ↓
Plan
        ↓
Chat
        ↓
Meetup
```

Screen 15 becomes the group's shared source of truth.

## 49. Acceptance criteria

### Consent

- Group creation occurs only after required mutuality conditions.
- Participants understand what they're joining.
- Joining the group is not presented as meetup confirmation.

### Privacy

- Only relevant participant information is shared.
- Contact details remain private by default.
- Hidden preferences are not exposed.

### Safety

- Report, Block, and Leave remain accessible.
- Safety guidance is visible.

### AI

- AI-generated content is reviewable.
- AI uses verified opportunity/group signals.
- AI cannot change membership or authority.

### Reliability

- Duplicate group creation is prevented.
- Participant changes are revalidated.
- Failed creation is recoverable.

### Group lifecycle

- Group can exist before meetup details are finalized.
- Users can leave.
- Membership changes are handled explicitly.

### Accessibility

- Keyboard accessible.
- Screen-reader compatible.
- States understandable without color.

## 50. Pyrintu moment

The intended feeling is:

> **Okay, this is now our shared space — but I'm not trapped, and the meetup isn't magically confirmed yet.**

The transition is:

```text
We independently want this
        ↓
Let's form a group
        ↓
Here's exactly who is joining
        ↓
Here's what we're doing
        ↓
Now let's plan it together
```
