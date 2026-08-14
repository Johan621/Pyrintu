# PYRINTU — UX SPECIFICATION
## Screen 9 — AI Intent Confirmation v1.0

**Status:** Approved / ready to lock

## Purpose

Prove that Pyrintu understood the user's intent before using it to find opportunities.

The user should be able to review the original request, inspect the structured interpretation, understand signal sources and uncertainty, correct mistakes, resolve conflicts, preview privacy, and explicitly confirm before activation.

## Core Trust Flow

`User says something → Pyrintu interprets it → Pyrintu shows the interpretation → User corrects it if needed → User confirms → Intent becomes active`

AI is an assistant, not the authority.

## Opening Experience

### Heading

`Here's what Pyrintu understood.`

### Supporting message

`Check the details before we use this to find opportunities. You can change anything that doesn't look right.`

### Reassurance

`Nothing becomes active until you confirm.`

## Original User Input

Always show the original intent in a collapsible section.

### Label

`What you told Pyrintu`

Example:

> "I'm new to Hyderabad, like badminton and startups, and want to meet a small group this weekend somewhere relaxed, under ₹500."

Action:

`Edit original`

## AI Interpretation

### Label

`What we understood`

Present structured signals as independently editable cards or chips.

Example signals:

- Location — Hyderabad
- Group — Small group
- Activity — Badminton
- Interest — Startups
- Environment — Relaxed
- Budget — Up to ₹500
- Timing — This weekend

## Signal Source / Provenance

Every important signal should show where it came from.

Examples:

- `Small group` — `[From your intent]`
- `Saturday evening` — `[From your intent]`
- `Small-group preference` — `[From your profile/preferences]`
- `After 6 PM` — `[From your availability]`

Tapping a source label opens:

### Why is this here?

Example:

> **Small group**
>
> You mentioned “small group” in your intent.

Or:

> **Saturday evening**
>
> Your intent said “this weekend” and your availability includes Saturday evening.

## Signal Confidence

Do not expose model probability numbers.

Use human-readable confidence:

- Clearly understood
- Likely
- Needs confirmation

Example:

```text
Activity
Badminton
✓ Clearly understood

Timing
This weekend
✓ Clearly understood

Environment
Relaxed
~ Likely

Day
Saturday
? Needs confirmation
```

## Ambiguity Handling

Do not silently resolve ambiguous requests.

Example:

User says `this weekend`.

Prompt:

`When did you mean?`

Options:

- Saturday
- Sunday
- Either day
- I'm flexible

The system must preserve flexibility where the user has not specified a precise value.

## Assumptions

If Pyrintu makes an inference, label it explicitly.

Example:

### Pyrintu assumption

`You may prefer a relaxed environment because you selected calmer environments in Social Preferences.`

Actions:

- Use this
- Don't use this
- Change preference

Material assumptions must never be hidden.

## No-Hallucination Contract

Pyrintu must not fabricate user intent.

AI must never invent without evidence:

- date
- time
- location
- budget
- activity
- relationship objective
- hard preference

When information is insufficient, the product should say:

`We need one more detail.`

## Missing Information

If only one important detail is missing, ask only that detail.

Example:

`Would you like somewhere near central Hyderabad, or are you flexible about the area?`

Options:

- Central Hyderabad
- Any area
- I'll choose later

Avoid multi-question forms.

## Editing a Signal

Selecting a signal opens a lightweight editor without restarting intent creation.

Example:

```text
Activity

○ Badminton
○ Café
○ Walk
○ Startup discussion
○ Other

[Save]
```

## Removing a Signal

Allow `Remove` on each signal.

When context is useful:

> **Remove “Small group”?**
>
> This came directly from your current intent.

Actions:

- Remove
- Keep

No guilt language.

## Adding a Missing Signal

Provide `Add detail` with relevant fields:

- Timing
- Location
- Activity
- Group size
- Environment
- Budget
- Purpose
- Other

## Inherited Preferences

Distinguish direct intent values from inherited preferences.

Example:

### Your usual preference

`Small groups`

### This intent

`Larger networking group`

Prompt:

`Which should we use for this intent?`

Actions:

- Use this intent
- Keep my usual preference
- Decide later

Using an intent-specific override must not mutate the stable profile or social preference.

## Preference Conflicts

If a direct intent conflicts with an important preference:

### Message

`This is different from a preference you marked as important.`

Supporting message:

`You can still use this intent, but Pyrintu wants to make sure that's what you mean.`

Actions:

- Use this intent once
- Keep my usual preference
- Change my preference

## Hard Boundary Handling

If the user has marked the conflicting preference as a hard boundary:

> **Your social preferences say this is a boundary.**

Require deliberate confirmation if the product policy allows an override.

Action:

`Continue with this intent anyway`

The screen must not silently override the boundary.

## Privacy Classification

For sensitive intent signals, clearly communicate whether the information is:

- Used by Pyrintu
- Shared later when relevant
- Private

Example:

`New to Hyderabad`

`[Used by Pyrintu]`

`[Not automatically public]`

## Privacy Preview

Provide:

### What others may eventually see

Example:

> `Looking for a small group for badminton this weekend.`

Do not automatically expose the full private context behind the intent.

This demonstrates data minimization.

## AI Explanation

Provide:

### How did Pyrintu build this?

Example:

`We combined what you wrote with the preferences and availability you chose earlier.`

Conceptual flow:

`Your intent + Your social preferences + Your availability → Intent interpretation`

## AI Processing State

During interpretation:

`Understanding your intent…`

Optional truthful stages:

- Reading your request
- Finding important details
- Checking your preferences
- Preparing confirmation

Do not use fake progress indicators.

## AI Uncertainty / Refusal

When the model cannot safely interpret a request:

> **I don't want to guess here.**
>
> One part of your request is too unclear for me to interpret reliably.

Identify the ambiguous field and request clarification.

## Manual Fallback

At all times:

`Edit manually`

must remain available.

AI must not trap the user inside an AI workflow.

## Confirmation Summary

At the bottom:

### Ready to use

Example:

> **Meet a small group in Hyderabad this weekend**
>
> Badminton  
> Relaxed environment  
> Up to ₹500  
> Saturday or Sunday  
> Moderate flexibility

Primary CTA:

`Confirm intent`

Secondary:

`Change something`

## Confirmation Semantics

On `Confirm intent`:

`Draft → Reviewed → Confirmed → Active`

The intent becomes eligible for the next stage:

`Screen 10 — Discovery / Opportunities`

## Confirmation Safeguard

Before activation:

> `Pyrintu will use this intent to look for relevant opportunities. You remain in control of which opportunities you accept.`

This reinforces recommendation versus decision authority.

## Post-Confirmation State

### Heading

`Your intent is ready.`

### Supporting text

`We'll look for opportunities that fit what you told us.`

Primary:

`See opportunities`

Secondary:

`View intent`

Destination:

`Screen 10 — Discovery / Opportunities`

## Editing After Confirmation

The user may still:

- Edit
- Pause
- Cancel

Confirmation is not permanent commitment.

## AI Feedback Loop

Repeated user corrections may help improve future interpretation, but corrections to the current intent must never silently rewrite the user's stable profile or social preferences.

Example:

Removing `Badminton` from the current intent must not remove `Badminton` from the user's profile.

## AI Learning Transparency

Where appropriate:

> `Your corrections help Pyrintu understand future requests better.`

Do not make unsupported claims about training, retention, or private-data usage; detailed wording belongs in the later Privacy specification.

## Loading State

Primary:

`Understanding your intent…`

If processing takes longer:

`Still working on it. You can wait or edit manually.`

Actions:

- Wait
- Edit manually

## Error States

### AI service failure

`Pyrintu couldn't interpret this right now.`

Actions:

- Try again
- Edit manually

### Intent save failure

`We couldn't save your confirmation. Your draft is still safe.`

Actions:

- Retry
- Keep editing

### Network failure

`You're offline. Your intent hasn't been activated yet.`

Action:

`Try again`

The interface must never imply activation when the server has not confirmed it.

## Recovery State

If an edit fails after interpretation:

`Interpretation complete → User edits → Save fails → Edited draft preserved → Retry`

The user's corrections must never be silently discarded.

## First-Time User Guidance

### Guide 04B — AI Confirmation

Target:

`Intent interpretation`

Message:

`Pyrintu will show exactly what it understood before using your request. You can correct anything.`

Primary:

`Review`

This is contextual guidance at the point where AI first becomes materially important.

## Accessibility Requirements

- semantic grouping of signals
- screen-reader labels for source and confidence
- keyboard-accessible editing
- accessible ambiguity choices
- accessible conflict warnings
- confirmation state announced
- no color-only confidence indication
- sufficient contrast
- visible focus states
- reduced-motion support
- touch-friendly controls

Example assistive output should communicate:

`Small group. Source: your intent. Confidence: clearly understood. Edit button.`

## Responsive Behavior

### Mobile

Priority order:

`Original request → What we understood → Signal cards → Source / confidence → Conflicts / clarification → Privacy preview → Final confirmation`

### Desktop

Two-column layout may be used:

**Left:** Original request + editable interpretation

**Right:** Why we understood this + sources + privacy preview

## Analytics Events

- intent_confirmation_viewed
- intent_original_expanded
- intent_signal_viewed
- intent_signal_edited
- intent_signal_removed
- intent_signal_added
- intent_signal_source_viewed
- intent_signal_confidence_viewed
- intent_ambiguity_detected
- intent_ambiguity_resolved
- intent_assumption_accepted
- intent_assumption_rejected
- intent_preference_conflict_detected
- intent_preference_conflict_resolved
- intent_privacy_preview_viewed
- intent_confirmation_started
- intent_confirmed
- intent_confirmation_abandoned
- intent_ai_failed
- intent_manual_fallback_selected

Never send raw intent text or sensitive extracted values into generic analytics.

## Performance

- cached draft available immediately
- AI results may update progressively where appropriate
- edits remain responsive
- no full-page reload
- manual editing works independently of AI

## Matching Boundary

Screen 9 does not choose matches.

It produces a validated intent representation.

Conceptual flow:

`Profile + Social Preferences + Availability + User Intent + Confirmed AI interpretation → Screen 10 — Discovery / Opportunities`

## Acceptance Criteria

### Trust

- User sees exactly what Pyrintu understood.
- Original request remains accessible.
- Every important signal has a source.
- Uncertain values are clearly identified.
- AI assumptions are labeled.

### Accuracy

- AI cannot silently invent critical details.
- Ambiguous information is clarified.
- Conflicting preferences are surfaced.
- User can edit any extracted value.

### Privacy

- User sees what may be shared later.
- Full intent is not automatically public.

### AI Safety

- AI is advisory.
- Manual fallback always exists.
- AI failure does not block the workflow.

### Lifecycle

- Confirmation activates the intent.
- User can edit, pause, or cancel afterward.

### Reliability

- Draft is preserved when saving fails.
- Offline state does not falsely activate an intent.

### Accessibility

- Keyboard accessible.
- Screen-reader compatible.
- Confidence and source information available without color.

## Final Intended Experience

```text
I said it.
    ↓
AI understood it.
    ↓
I checked it.
    ↓
I corrected it.
    ↓
I approved it.
    ↓
Now Pyrintu can act.
```

The user should leave this screen feeling that Pyrintu did not merely generate something; it showed its understanding and let the user remain in control.

## Lock Note

Screen 9 was explicitly approved in product review. This specification is locked for implementation planning; implementation remains separate from the UX contract.
