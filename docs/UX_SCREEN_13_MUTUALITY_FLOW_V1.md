# PYRINTU — UX SPECIFICATION
## Screen 13 — Mutuality Flow v1.0

**Status:** Approved — UX V1

---

# 1. Core objective

Create a respectful mechanism for determining whether people are independently willing to continue toward a shared opportunity.

The core model is:

```text
Individual interest
        +
Independent interest from others
        +
Opportunity eligibility
        ↓
Mutuality
        ↓
Proceed / continue forming / stop
```

Mutuality is not “someone liked you.” It means enough people independently want to participate in the same opportunity under compatible conditions.

---

# 2. Opening experience

### Heading

# **You're interested. Let's see if the interest is mutual.**

Supporting text:

> **Pyrintu will give everyone space to decide independently. No one needs to respond immediately.**

---

# 3. Independence principle

Every person makes their decision independently.

Do not show pressure-oriented language such as “3 people already said yes. You should join.”

Prefer:

> **Your response is private until the opportunity reaches the appropriate mutuality state.**

---

# 4. User response options

### Interested

> I'd like to continue exploring this.

### Maybe

> I'm open, but I need more information.

### Not interested

> This isn't right for me.

The meaning of each state must be explicit.

---

# 5. Maybe is not Yes

```text
Interested
→ positive signal

Maybe
→ unresolved signal

Not interested
→ negative signal
```

A Maybe does not count as full mutual confirmation.

---

# 6. Private response

When the user responds:

> **Your response is recorded privately.**

Do not immediately expose individual response decisions to other participants unless the product reaches an explicitly approved disclosure stage.

---

# 7. Mutuality state model

```text
Exploring
   ↓
Responses forming
   ↓
Potentially mutual
   ↓
Mutual
   ↓
Ready to plan
```

Alternative termination paths:

```text
Exploring
   ↓
Not enough mutual interest
```

or:

```text
Potentially mutual
   ↓
Opportunity changed
```

---

# 8. State — Exploring

No meaningful responses yet.

> **We're giving everyone time to decide.**

No countdown and no social-pressure language.

---

# 9. State — Responses forming

Some responses exist, but the mutuality threshold has not been reached.

> **The opportunity is still forming.**

> **Enough information isn't available yet to know whether it will move forward.**

Do not expose unnecessary individual responses.

---

# 10. State — Potentially mutual

Enough positive signals exist to suggest that the opportunity may proceed, but required conditions are not yet complete.

> **This is looking promising.**

> **Several participants are independently interested, but one or more conditions still need to be resolved.**

Action:

**Review what remains**

---

# 11. State — Mutual

The system has satisfied the predefined mutuality conditions.

# **This opportunity is mutually supported.**

> **The required participants have independently indicated that they want to continue.**

Do not say “Everyone likes everyone.”

---

# 12. State — Ready to plan

Mutuality has been achieved and the opportunity can progress toward planning.

# **You're ready for the next step.**

> **The group has enough mutual interest to start working out the plan.**

Primary action:

**Continue**

Destination: **Screen 14 — Group Creation** or the appropriate downstream state once technical architecture defines exact transitions.

---

# 13. Not enough mutuality

# **This one isn't forming right now.**

> **Not enough mutual interest came together for this opportunity. Your current intent is still active.**

Primary:

**Find another opportunity**

Secondary:

**View my intent**

Never frame this as personal rejection.

---

# 14. Avoid social rejection framing

Avoid:

> “Nobody chose you.”

> “People weren't interested in you.”

Prefer:

> **This opportunity didn't reach the conditions needed to move forward.**

---

# 15. No visible popularity ranking

Do not create social status competition with popularity counts.

Where counts are genuinely necessary, use neutral wording:

> **4 participants currently involved**

not:

> **Popular with 4 people**

---

# 16. Participant response privacy

Default:

### Individual responses are private.

The user may see aggregate state such as:

> **3 participants are interested.**

But not a person-by-person breakdown unless explicitly approved later.

---

# 17. Minimum disclosure principle

Reveal only the information necessary to explain the current state.

Example:

> **The group is still forming because one required participant hasn't responded yet.**

Do not reveal unrelated personal behavior or reasons for non-response.

---

# 18. Response timing

Do not create artificial urgency.

Where appropriate:

> **No response needed immediately.**

When a real external deadline exists:

> **This opportunity closes Sunday at 5 PM because the activity reservation expires then.**

Only factual urgency is allowed.

---

# 19. Reminder policy

Reminders must be neutral.

Good:

> **Your response is still open for this opportunity.**

Bad:

> **Everyone is waiting for you!**

Bad:

> **Don't miss your chance!**

---

# 20. Maybe flow

If the user chooses **Maybe**:

### **What would help you decide?**

Optional choices:

- More information about the people
- More information about the activity
- Confirm the timing
- Confirm the location
- Understand the cost
- I'll decide later

---

# 21. Maybe → Interested

The user can later change:

**Maybe → Interested**

Message:

> **Your response has been updated.**

---

# 22. Maybe → Not interested

Likewise:

**Maybe → Not interested**

No penalty and no ranking suppression because the user changed their mind.

---

# 23. Interested → Withdraw

Users can withdraw before final commitment.

### **Stop participating in this opportunity?**

> **You can step back at any point before the meetup is confirmed.**

Actions:

**Withdraw**

**Keep my interest**

No guilt language.

---

# 24. What happens after withdrawal

> **You're no longer part of this opportunity.**

> **Your current intent remains unchanged unless you choose to update it.**

---

# 25. Deterministic mutuality rules

The exact rules for reaching mutuality are deterministic and belong to technical architecture.

Conceptually:

```text
Required participant count
+
Required positive response count
+
Eligibility
+
Opportunity validity
=
Mutual
```

AI may explain the result but cannot change the threshold.

---

# 26. AI role

AI may:

- explain the current mutuality state
- answer questions
- explain what remains unresolved
- summarize the next step
- help the user identify what information they need

AI must not:

- pressure the user to say yes
- predict another person's answer
- reveal private responses
- invent mutual interest
- change the mutuality threshold
- claim a relationship exists
- guilt users into responding

---

# 27. AI question example

User:

> “Is this group confirmed?”

AI response:

> **Not yet. The opportunity has enough interest to keep forming, but the required mutuality conditions haven't been met.**

> **You don't need to do anything else right now unless you'd like to change your response.**

---

# 28. AI grounding

AI answers must use structured state such as:

```text
current_state
required_participants
eligible_participants
positive_response_count
maybe_response_count
pending_response_count
opportunity_valid
```

The AI must not infer those values from chat history alone.

---

# 29. Privacy explanation

### **How responses work**

> **Your response is handled privately. Pyrintu uses it to determine whether the opportunity can move forward.**

Action:

**Learn more**

---

# 30. Safety

Safety controls remain accessible throughout mutuality:

**Report**

**Block**

**Leave opportunity**

Withdrawal does not require a reason.

---

# 31. Mutuality and safety are separate

A group reaching mutuality does not mean everyone is safe.

Mutuality means only that the product's defined participation conditions have been satisfied.

Safety eligibility and moderation remain separate systems.

---

# 32. Opportunity changes after responses

If the activity, timing, or other material opportunity property changes:

> **This opportunity changed.**

> **Because the plan changed, we'll confirm that the current participants still want to continue.**

Prior response consent must not be carried forward blindly.

---

# 33. Participant changes

If someone leaves:

> **The group changed.**

> **Pyrintu is checking whether the opportunity still meets the conditions needed to continue.**

Possible results:

**Still mutual**

or:

**Needs another participant**

---

# 34. Expiration

If the opportunity expires:

> **This opportunity is no longer available.**

Action:

**Find another opportunity**

A response must not automatically transfer to another opportunity.

---

# 35. User dashboard state

Show:

```text
My response
Interested

Opportunity
Forming

Mutuality
Not yet reached
```

---

# 36. Notifications

Neutral notifications include:

### Response recorded

> **Your interest is recorded.**

### Mutuality reached

> **The opportunity is now mutually supported.**

### Opportunity changed

> **The opportunity changed and needs another look.**

### No longer forming

> **This opportunity didn't reach the conditions needed to continue.**

Avoid celebratory or pressure language when mutuality has not actually been established.

---

# 37. First-time guide

Existing Guide 06:

### Target

**Continue**

### Message

> **A match is only useful when both people want to invest effort. This is what makes Pyrintu different.**

---

# 38. Accessibility

Requirements:

- response options use semantic radio/button controls
- state changes announced to screen readers
- aggregate counts accessible without color
- dialogs keyboard accessible
- withdrawal and safety controls reachable by keyboard
- no social-pressure animations
- reduced-motion supported
- timeout warnings accessible
- focus preserved after response changes

Example screen-reader output:

> “Your response: Interested. Opportunity state: Responses forming. Mutuality has not yet been reached.”

---

# 39. Responsive behavior

### Mobile

```text
Opportunity summary
↓
Your response
↓
Mutuality state
↓
What happens next
↓
Privacy explanation
↓
Optional clarification
↓
Safety controls
```

Keep the user's current response visually prominent.

### Desktop

```text
LEFT
Opportunity + mutuality state

RIGHT
Your response
+
What happens next
+
Privacy
+
Safety
```

---

# 40. Analytics

Track:

```text
mutuality_viewed
mutuality_response_viewed
mutuality_interested_selected
mutuality_maybe_selected
mutuality_not_interested_selected
mutuality_interest_confirmed
mutuality_interest_withdrawn
mutuality_response_changed
mutuality_help_viewed
mutuality_reminder_sent
mutuality_state_changed
mutuality_reached
mutuality_failed
mutuality_opportunity_changed
mutuality_participant_changed
mutuality_expired
mutuality_ai_question_started
mutuality_ai_question_completed
```

Do not send individual private response values into generic analytics.

---

# 41. Performance

- response selection should feel immediate
- local UI state may update optimistically where safe
- server confirmation follows
- stale response state must be reconciled
- AI explanations load asynchronously
- core mutuality state does not depend on AI

---

# 42. Error state

### Response save failed

> **We couldn't record your response.**

> **Your previous response is still active.**

Actions:

**Try again**

### State unavailable

> **We couldn't refresh the opportunity status.**

Action:

**Retry**

### Opportunity changed during response

> **This opportunity changed before your response could be saved.**

Action:

**Review updated opportunity**

---

# 43. Recovery

Do not lose the user's selected response because of a transient network error.

Distinguish:

```text
Selected locally
↓
Pending sync
↓
Confirmed
```

from:

```text
Selected locally
↓
Sync failed
↓
Retry
```

Pending is not the same as confirmed.

---

# 44. Product boundary

Screen 13 does not:

- create the final group
- choose the meetup location
- confirm the meetup
- guarantee chemistry
- guarantee safety
- reveal private responses
- make the user responsible for getting others to respond

It establishes whether the opportunity has enough independent willingness to proceed.

---

# 45. Handoff to Screen 14

When mutuality is reached:

```text
Mutuality
      ↓
Group Creation
      ↓
Group Details
      ↓
Activity
      ↓
Meetup
```

Screen 14 defines how the actual group becomes a concrete Pyrintu group.

---

# 46. Acceptance criteria

### Independence

✅ Each participant can respond privately.

✅ One participant's response does not pressure another.

### State accuracy

✅ Interested, Maybe, and Not Interested have distinct meanings.

✅ Mutuality is reached only through deterministic conditions.

✅ Opportunity changes can invalidate prior mutuality.

### Privacy

✅ Individual responses are not unnecessarily exposed.

✅ Aggregate state is used where appropriate.

### Safety

✅ Report, Block, and Leave remain accessible.

✅ Mutuality does not imply safety certification.

### AI

✅ AI explains state rather than deciding state.

✅ AI cannot reveal private responses.

✅ AI cannot pressure users.

### User control

✅ Users can change their response.

✅ Users can withdraw before final commitment.

✅ Withdrawal does not silently delete intent.

### Reliability

✅ Response failures are recoverable.

✅ Pending vs confirmed state is explicit.

### Accessibility

✅ Response controls are keyboard and screen-reader accessible.

---

# 47. The Pyrintu moment

The user should feel:

> **“I can express interest without putting myself or anyone else under pressure.”**

And later:

> **“The opportunity moved forward because people independently wanted it—not because Pyrintu pushed them.”**

The product principle is:

```text
Compatibility
      ↓
Interest
      ↓
Independent responses
      ↓
Mutuality
      ↓
Shared commitment
```

---

## Approval status

**Screen 13 approved by product review.**

The specification is intentionally UX-only. Technical threshold definitions, data schemas, matching implementation, and notification infrastructure belong to later architecture work.
