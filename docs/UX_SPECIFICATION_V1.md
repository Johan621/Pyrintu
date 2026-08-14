# PYRINTU — UX SPECIFICATION V1.0

**Status:** Screen 1 and Screen 2 approved; Screen 3 approved / next active workstream

## Purpose

Define the complete V1 product experience screen-by-screen before technical architecture or application code is generated.

## UX principles

1. Warm, premium, human, and trustworthy.
2. Small-group, relationship-first experience rather than feed-first engagement.
3. Natural language is welcome, but structured controls remain available.
4. Users should always understand what Pyrintu is doing and why.
5. Safety controls are visible and never hidden behind the onboarding guide.
6. AI recommendations are explainable and grounded in actual user-provided signals.
7. First-time users receive progressive guidance rather than a long tutorial.
8. Every important workflow has clear loading, empty, success, error, and recovery states.
9. Accessibility is designed in from the beginning.
10. Avoid dark patterns and pressure-based engagement.

## First-time user guided experience

### Goal

Help a brand-new user complete the first meaningful Pyrintu journey without requiring prior knowledge of the product.

### Guided-tour requirements

- Highlight the specific control being introduced.
- Explain the purpose in one clear sentence.
- Provide an immediate action.
- Show progress without creating a feeling of a tutorial maze.
- Permit skipping non-essential guidance.
- Persist completion state.
- Allow later contextual help.
- Support keyboard navigation and screen readers.
- Respect reduced-motion settings.
- Never obscure Report, Block, Leave Group, or other safety-critical controls.

### Initial guided sequence

#### Guide 01 — Welcome

**Trigger:** First authenticated session.

**Purpose:** Establish the mental model.

**Target:** No button highlight initially; use a lightweight welcome panel.

**Message:** `Pyrintu helps you move from a promising connection to a real relationship. We'll guide you through your first step.`

**Primary action:** `Let's begin`

**Secondary action:** `Skip introduction`

**Acceptance criteria:**

- User understands the core purpose before being asked for detailed preferences.
- Skip is available.
- Progress is persisted.

#### Guide 02 — Profile

**Target:** `Create Profile`

**Message:** `Tell Pyrintu a little about yourself so we can make better recommendations.`

**Primary action:** `Create Profile`

#### Guide 03 — Social preferences

**Target:** `Your Preferences`

**Message:** `Tell us what kind of people, activities, group sizes, and environments feel right for you.`

#### Guide 04 — Intent

**Target:** `Create Intent`

**Message:** `Describe what you want right now. You can type it naturally — Pyrintu will structure it for you.`

Example intent:

`I'm new to Hyderabad, like badminton and startups, and want to meet a small group this weekend.`

#### Guide 05 — Match reasoning

**Target:** `Why this match?`

**Message:** `Pyrintu will show the real signals behind a recommendation rather than giving you a mysterious score.`

#### Guide 06 — Mutuality

**Target:** `Continue`

**Message:** `A match is only useful when both people want to invest effort. This is what makes Pyrintu different.`

#### Guide 07 — Group

**Target:** `Group Details`

**Message:** `See who is in the group, why the group was formed, and what the group is planning.`

#### Guide 08 — Activity

**Target:** `Choose Activity`

**Message:** `The activity is the bridge from online matching to a real-world interaction.`

#### Guide 09 — Meetup confirmation

**Target:** `Confirm Meetup`

**Message:** `Review the time, place, group, and privacy details before confirming.`

#### Guide 10 — Feedback

**Target:** `Post-Meet Feedback`

**Message:** `Your private feedback helps Pyrintu improve future matches and group formation.`

## Screen 1 — Landing / Marketing Page

**Status:** Approved / ready to lock

### Purpose

Help the right visitor understand Pyrintu quickly and begin the first meaningful connection journey.

### Primary product message

**Headline:** `Meet people. Build something real.`

**Supporting text:** `Pyrintu helps you find compatible people, create real-world experiences together, and turn promising connections into meaningful relationships.`

**Primary CTA:** `Get Started`

**Secondary CTA:** `See How It Works`

`Get Started` begins the signup/onboarding flow. `See How It Works` scrolls to the explanation on the same page.

### Navigation

Desktop navigation should expose:

- Pyrintu
- How It Works
- Safety
- About
- Sign In
- Get Started

Mobile navigation should collapse to the essential links behind a menu.

### Hero

**Eyebrow:** `REAL CONNECTIONS, NOT ENDLESS MATCHING`

**Headline:** `Meet people. Build something real.`

**Supporting text:** `Find people who fit the kind of connection you're looking for, meet through shared experiences, and give promising relationships a chance to grow.`

**Primary CTA:** `Get Started →`

**Secondary CTA:** `See How It Works`

The hero visual should communicate the progression `You → compatible people → small group → shared activity → relationship`.

The visual style should be warm, premium, human, and modern. Avoid generic AI robots, corporate SaaS dashboards, or dating-app visual language.

Animation is optional and must never be required to understand the product.

### Core differentiation

**Heading:** `Not more matches. Better connections.`

Three supporting concepts:

#### 01 — Understand You

`Pyrintu learns the kinds of people, activities, environments, and experiences that actually fit you.`

#### 02 — Find Mutuality

`Compatibility isn't enough. Pyrintu looks for genuine willingness from both sides to invest effort.`

#### 03 — Build Momentum

`A promising connection shouldn't disappear after one interaction. Pyrintu helps relationships move forward naturally.`

### How Pyrintu works

**Heading:** `From “Nice to meet you” to “See you again.”`

1. **Tell us about you** — interests, preferences, and social style.
2. **Tell us what you want** — describe the desired connection or experience naturally.
3. **Meet a compatible opportunity** — Pyrintu explains why the recommendation fits.
4. **Do something together** — a small group and shared activity create the real-world interaction.
5. **Keep the connection going** — when the connection is mutual, Pyrintu helps it continue.

### Product demonstration

**Heading:** `Tell Pyrintu what you want.`

Example input:

`I'm new to Hyderabad, I like badminton and startups, and I want to meet a small group this weekend. Somewhere relaxed, under ₹500.`

The interface can translate this into a structured intent preview:

- Hyderabad
- Small group
- Badminton
- Startups
- Relaxed environment
- Budget ≤ ₹500
- This weekend

Example opportunity:

- 4 people
- Sunday · 6:30 PM
- Badminton + café
- Small group
- ₹350 estimated

Illustrative mutuality message:

`Everyone independently wants to meet.`

This is an example of the product behavior, not a claim about current availability.

### Educational section

**Heading:** `A match isn't the goal.`

Supporting message:

`Two people can look perfect on paper and never meet. Pyrintu looks beyond similarity and asks whether both people are actually willing to make something happen.`

Conceptual relationship:

`Compatibility + Mutual willingness = Real opportunity`

### Trust section

**Heading:** `Built for real-world connection.`

Trust principles:

- **Privacy first** — personal information is not automatically public.
- **Small groups** — optimize for meaningful interaction rather than crowds.
- **Safety controls** — users can report, block, and leave when needed.
- **You're in control** — Pyrintu recommends; the user decides.

Do not show fabricated testimonials, user counts, ratings, awards, partner logos, or unsupported trust claims.

### First-time entry

The marketing page should not expose the full product tutorial. Clicking `Get Started` enters product onboarding, where the progressive first-time guide begins with the Welcome panel and then moves through the contextual controls defined above.

### Final conversion section

**Heading:** `Your people aren't always obvious.`

**Supporting text:** `Start with what you're looking for. Pyrintu will help with the rest.`

**Primary CTA:** `Get Started →`

### Footer

The initial footer should provide routes/placeholders for:

- Product
- How It Works
- Safety
- About
- Contact
- Privacy
- Terms
- Community Guidelines
- Instagram
- LinkedIn
- YouTube

Unpublished destinations must not be represented as completed content.

### Required states

The landing page should remain usable if non-critical visual assets fail or load slowly. Text, navigation, and primary CTA must not depend on animation or remote visual assets.

### Accessibility

- semantic heading hierarchy
- keyboard navigation
- visible focus states
- accessible controls
- meaningful alt text for meaningful imagery
- decorative imagery marked appropriately
- sufficient contrast
- reduced-motion support
- no essential information conveyed by color alone
- comfortable mobile touch targets
- screen-reader-friendly navigation

### Responsive behavior

Mobile priority order:

`Headline → Supporting message → Get Started → See How It Works → Hero visual → Core difference → How it works → Product example → Trust → Final CTA`

Tablet and desktop may use two-column layouts where useful, but the information hierarchy remains the same.

### SEO foundation

Initial technical requirements:

**Title:** `Pyrintu — Meet People. Build Something Real.`

**Meta description:** `Pyrintu helps you build meaningful real-world relationships through compatible people, shared experiences, and mutual connection.`

Also require one canonical URL, semantic HTML, crawlable text, Open Graph metadata, appropriate icons, and later sitemap/robots configuration.

### Analytics events

- `landing_view`
- `nav_sign_in_clicked`
- `hero_get_started_clicked`
- `how_it_works_clicked`
- `core_difference_viewed`
- `intent_demo_interacted`
- `trust_section_viewed`
- `final_get_started_clicked`
- `signup_started`

Do not place raw private user content into generic analytics payloads.

### Performance

- mobile-first
- minimal JavaScript on first paint
- lazy-load non-critical visual assets
- optimized images
- avoid blocking third-party scripts
- fast CTA interaction

Premium design must not require a heavy page.

### Security and privacy boundary

The marketing page must not request unnecessary personal permissions. It must not request exact location, contacts access, or social graph scraping before authenticated product flows require them.

### Acceptance criteria

#### Messaging

- Visitor can understand Pyrintu's purpose without external explanation.
- The product is clearly differentiated from a generic matching app.
- Mutuality is understandable without technical jargon.

#### UX

- Primary CTA is obvious.
- Secondary information is easy to discover.
- Marketing page flows naturally into onboarding.

#### Trust

- No unsupported claims.
- No fake social proof.
- Safety principles are visible.

#### Accessibility

- Keyboard accessible.
- Screen-reader compatible.
- Reduced-motion supported.

#### Performance

- No unnecessary heavy assets.
- Mobile experience remains usable on slower connections.

#### Analytics

- Required conversion events are defined and testable.

### Lock note

Screen 1 was approved in product review and is now the first locked UX contract. Implementation is intentionally separate from this UX specification and must not begin until the UX branch is merged and the technical implementation task is created.

## Screen catalogue — to be specified next

1. Landing / marketing page
2. Sign up / sign in
3. Account verification
4. Welcome / guided introduction
5. Profile creation
6. Social preferences
7. Availability
8. Intent creation
9. AI intent confirmation
10. Discovery / opportunities
11. Match details
12. Match reasoning
13. Mutuality flow
14. Group creation
15. Group details
16. Activity selection
17. Activity plan
18. Group chat
19. Meetup confirmation
20. Meetup state / reminders
21. Post-meet feedback
22. Relationship Momentum
23. Circles
24. Notifications
25. Safety center
26. Report flow
27. Block flow
28. Privacy settings
29. Account settings
30. Help / support

## Required state model for every screen

Each screen must define:

- purpose
- user goal
- primary action
- secondary actions
- required data
- AI behavior
- deterministic behavior
- loading state
- empty state
- error state
- recovery state
- privacy implications
- safety implications
- analytics events
- accessibility requirements
- acceptance criteria

## Status

This document is intentionally incomplete. We will fill it one screen at a time, review it, then freeze UX V1 before technical architecture begins.

# Screen 2 — Sign Up / Sign In

## Purpose

Allow new and returning users to securely access Pyrintu while minimizing friction and establishing trust.

## Authentication Methods

### Supported Providers

- Continue with Google
- Continue with LinkedIn
- Continue with Phone Number (OTP)

Authentication provider is separate from the Pyrintu user account.

Multiple authentication methods may be linked to a single Pyrintu account.

## User Goal

Access Pyrintu as quickly as possible without completing unnecessary profile information.

## Entry Experience

### Heading

Welcome to Pyrintu

### Supporting Copy

Meet people. Build something real.

### Primary Actions

- Continue with Google
- Continue with LinkedIn
- Continue with Phone Number

### Divider

or

### Phone Flow

Enter Phone Number

Send OTP

## Authentication Flow

### Existing User

Authentication
→ Identity Found
→ Sign In
→ Open Pyrintu

### New User

Authentication
→ Identity Verified
→ Create Pyrintu Account
→ Continue to Onboarding

### Partial Onboarding

If onboarding was not completed previously:

Welcome back. Let's continue where you left off.

## Google Authentication

Purpose:

- Fast onboarding
- Trusted identity verification

Only minimum required identity information is requested.

## LinkedIn Authentication

Purpose:

- Professional identity verification
- Reduced onboarding friction

LinkedIn information must never be used as a measure of social value.

## Phone OTP Authentication

### Step 1

Phone Number Input

Default country:

India (+91)

### Step 2

OTP Verification

Actions:

- Verify
- Resend Code
- Change Number

## Age Gate

Question:

Are you 18 or older?

Options:

- Yes, I'm 18+
- No

Users below the minimum age requirement cannot proceed.

## Terms & Privacy

Before account creation:

By continuing, you agree to Pyrintu's Terms and Privacy Policy.

Marketing consent must remain optional and separate.

## AI Behavior

AI is not involved in authentication decisions.

AI may assist later onboarding flows but does not determine authentication success.

## Deterministic Behavior

Authentication outcome is based only on:

- Provider verification
- OTP verification
- Account existence checks

## Loading State

Examples:

Connecting to Google...

Connecting to LinkedIn...

Verifying code...

Buttons become temporarily disabled during processing.

## Empty State

No authentication method selected.

User is shown available authentication options.

## Error State

### Google Failure

Google sign-in isn't available right now.

### LinkedIn Failure

LinkedIn sign-in isn't available right now.

### Invalid OTP

That code doesn't look right.

### Expired OTP

That code has expired.

### Network Failure

We couldn't complete that request.

## Recovery State

Every failure path provides recovery options.

Examples:

- Retry
- Use another method
- Resend OTP
- Change phone number
- Account recovery

## Privacy Implications

Authentication data must be protected.

Personal information is not automatically public.

Sensitive authentication secrets are never exposed.

## Safety Implications

Authentication contributes to trust but does not automatically create a trusted reputation.

Identity state and safety state remain separate.

## Analytics Events

- auth_screen_viewed
- google_auth_started
- google_auth_succeeded
- google_auth_failed
- linkedin_auth_started
- linkedin_auth_succeeded
- linkedin_auth_failed
- phone_auth_started
- otp_sent
- otp_verified
- otp_failed
- auth_completed
- auth_abandoned
- age_gate_completed
- terms_accepted

No phone numbers, emails, tokens, or OTP values may be stored in analytics events.

## Accessibility Requirements

- Keyboard accessible
- Screen-reader compatible
- Logical focus order
- Visible focus indicators
- Sufficient contrast
- Touch-friendly controls
- Reduced-motion support

## Acceptance Criteria

### Authentication

- Google authentication works
- LinkedIn authentication works
- Phone OTP authentication works

### Account Integrity

- Duplicate account creation is prevented
- Multiple providers can link to one account
- Partial onboarding resumes correctly

### Trust

- Age gate exists
- Terms and Privacy are accessible

### User Experience

- Unified sign-in experience
- Clear loading states
- Clear error states
- Recovery available for all failures

### Accessibility

- Keyboard accessible
- Screen-reader compatible
- Mobile-friendly

### Privacy

- No sensitive authentication information is stored in analytics

# Screen 3 — Account Verification

**Status:** Approved / ready to lock

## Purpose

Help Pyrintu establish enough trust in an account before the user enters higher-risk social interactions.

Verification should be proportionate, understandable, privacy-conscious, and recoverable.

The user should always know what Pyrintu is checking, why it is checking it, and what happens next.

## Core Verification Model

Pyrintu separates three concepts:

`Authentication → Verification → Safety state`

### Authentication

Question: `Do you control this identity?`

### Verification

Question: `Can Pyrintu establish additional trust?`

### Safety State

Question: `Is this account currently allowed to participate?`

These are separate concepts and must not be treated as interchangeable.

A user signing in with Google or LinkedIn does not automatically receive a high-trust reputation.

## Verification Levels

### Level 0 — Account created

The user has authenticated successfully.

Status:

`Account created`

### Level 1 — Contact verified

Depending on the authentication method:

- Phone verified
- Provider identity verified

Status:

`Basic verification complete`

### Level 2 — Profile readiness

The user completes the minimum information required for meaningful participation.

Examples:

- profile basics
- required social information
- profile completeness

Status:

`Profile ready`

### Level 3 — Safety eligibility

Pyrintu completes applicable automated safety checks.

The system may consider:

- suspicious authentication patterns
- repeated failed verification
- account abuse signals
- duplicate-account indicators
- unusual automated behavior

The user should not be shown an unexplained secret score.

Possible states:

`Ready`

`Additional verification required`

`Under review`

### Level 4 — Higher-trust verification

Certain future actions may require stronger verification.

Examples:

- higher-risk meetups
- unusual account behavior
- repeated safety incidents
- features requiring stronger identity assurance

This is not automatically required for every user.

Exact requirements belong in the Trust, Safety & Privacy specification.

## Initial Verification Screen

### Heading

`Let's make Pyrintu safer for everyone.`

### Supporting text

`A few verification steps help us protect the community. We'll only ask for information when it's necessary.`

### Primary CTA

`Continue`

### Secondary CTA

`Why do you need this?`

The secondary action opens a concise explanation.

## Verification Checklist

Show a clear progress component:

```text
Your account

✓ Identity
○ Contact
○ Profile
○ Safety check
```

The exact steps shown should depend on the user's current state. Do not show unnecessary verification requirements.

## Phone Verification

If the user chose phone authentication:

`Phone number → OTP → Phone verified ✓`

Message:

`Phone number verified`

No second OTP should be requested unnecessarily.

If the user authenticated using Google or LinkedIn, phone verification can be introduced when the product requires it.

## Provider Verification

Message:

`Identity provider connected`

Purpose:

- confirm control of the authentication account
- reduce onboarding friction

The interface must not imply that provider authentication means the user is trustworthy.

## Profile Verification

When minimum profile information is required:

### Heading

`Complete your basic profile`

### Supporting message

`A little context helps people know who they're connecting with and helps Pyrintu make better recommendations.`

### CTA

`Complete Profile`

This should transition into the Profile screen rather than turning verification into a large form.

## Safety Check

Loading message:

`Running a safety check…`

Success:

`Safety check complete`

Additional step:

`We need one more step.`

Do not expose internal fraud-detection logic or opaque numerical trust scores.

## Additional Verification Required

### Heading

`One more step`

### Supporting text

`We need a little more information before you can continue with this activity. This helps protect Pyrintu members and reduce abuse.`

### Primary CTA

`Continue verification`

### Secondary CTA

`Why?`

The explanation should be specific enough to be understandable without revealing anti-abuse mechanisms.

## Identity-Document Verification

Identity-document verification is **not part of default onboarding for every user**.

If stronger verification is required for a specific risk scenario, the flow must explain:

- why the information is requested
- what is collected
- how it is used
- how long it is retained
- who can access it
- what happens after verification

Exact document types and retention policy belong in the later Trust, Safety & Privacy specification.

## Verification Result States

### Verified

`✓ You're verified`

`You're ready to continue.`

CTA: `Continue`

### Pending

`◷ Verification in progress`

`Your verification is still being reviewed. We'll let you know when there's an update.`

CTA: `Continue where available`

### More Information Required

`! One more step`

`We couldn't complete verification with the information available.`

Actions:

- Try again
- Get help

### Failed

Use neutral language:

`We couldn't verify your account yet.`

Actions:

- Try again
- Use another verification method
- Contact support

## Rate Limiting and Abuse Protection

Verification attempts must not be unlimited.

Possible system behavior:

`normal → retry → temporary cooldown → additional review`

User-facing message:

`Please wait before trying again.`

Exact limits belong in the security specification.

## Suspicious Activity State

### User-facing message

`We need to review your account before you continue.`

Supporting text:

`This additional review helps us protect the Pyrintu community.`

Actions:

- View status
- Get help

Do not expose internal detection rules.

## Manual Review

Flow:

`Submitted → Under review → Decision`

User message:

`Verification under review`

`Your account is being reviewed. You don't need to keep this screen open.`

## Appeal / Dispute

### Heading

`Think we got this wrong?`

### Supporting text

`You can request a review of the decision.`

### CTA

`Request review`

The appeal flow must not reveal internal detection rules.

## Privacy Explanation

### Why verification?

`Verification helps reduce fake accounts, abuse, and unsafe interactions.`

### Your privacy

`Pyrintu should collect only the information needed for the verification purpose.`

### Your control

`You should be able to understand what information is being requested before providing it.`

This becomes part of the trust contract.

## Safety Controls

Verification must never block access to essential safety controls.

Where applicable, users can access:

- Report
- Block
- Leave
- Help

Verification UI must not obscure these controls.

## AI Behavior

AI does **not** decide verification eligibility.

Authentication and verification decisions should rely on deterministic and security-controlled systems.

AI may eventually assist humans with:

- review prioritization
- explanation generation
- support responses

AI must not be the blind final authority for identity or safety decisions.

## Deterministic Behavior

The system owns:

- authentication state
- verification state
- attempt limits
- cooldowns
- required verification level
- review state
- eligibility state

The UI reflects these states. The UI does not invent them.

## Analytics Events

- verification_screen_viewed
- verification_started
- phone_verification_started
- phone_verification_completed
- provider_verification_completed
- profile_verification_started
- safety_check_started
- safety_check_completed
- additional_verification_requested
- verification_retry
- verification_pending
- verification_completed
- verification_failed
- manual_review_started
- appeal_started
- support_opened
- verification_abandoned

Never send these through generic analytics:

- OTP values
- identity-document contents
- raw personal identifiers
- sensitive verification evidence

## Accessibility Requirements

- Keyboard navigable
- Screen-reader compatible
- Progress states announced clearly
- Status changes accessible
- Errors associated with relevant controls
- Visible focus states
- Sufficient contrast
- No color-only status indication
- Reduced-motion support
- Touch-friendly controls

For asynchronous verification, screen readers should receive an accessible status update when verification changes state.

## First-Time User Guide

### Guide 03 — Verification

**Target:** Verification status / progress component

**Message:** `Verification helps keep Pyrintu trustworthy. We'll only ask for additional information when it's necessary.`

**Primary action:** `Continue`

**Secondary action:** `Why?`

The guide must not automatically highlight sensitive information fields before the user understands why they are being requested.

## Responsive Behavior

### Mobile

Priority order:

`Heading → Explanation → Verification progress → Current verification action → Privacy explanation → Safety / Help`

### Desktop

A two-column layout may be used:

- Left: explanation + progress
- Right: current verification action

The information hierarchy remains identical.

## Loading States

Examples:

`Checking your account…`

`Sending verification code…`

`Checking verification…`

`Reviewing your account…`

No infinite spinner. Every operation must have a recoverable failure state.

## Offline / Network Failure

Message:

`We couldn't complete the verification right now.`

Actions:

- Try again
- Continue later

Interrupted verification must not corrupt the account state.

## Security Principles

At implementation time, verification must include protections such as:

- rate limiting
- replay protection
- secure token handling
- server-side validation
- audit logging
- abuse detection
- secure provider callbacks
- protection against account enumeration

Exact implementation belongs in the later security architecture.

## Acceptance Criteria

### Understandability

- User knows why verification exists.
- User knows what is currently being verified.
- User knows what happens next.

### Trust

- Verification does not automatically imply a social reputation score.
- Stronger verification is progressive rather than unnecessarily mandatory.

### Privacy

- No unnecessary sensitive information requested.
- Privacy explanation exists before sensitive collection.
- Analytics contains no verification secrets.

### Safety

- Report/block/leave/help remain accessible.
- Suspicious activity has a review pathway.

### Recovery

- Retry exists.
- Cooldown exists where required.
- Manual review exists where applicable.
- Appeal/support path exists where applicable.

### Accessibility

- Keyboard accessible.
- Screen-reader compatible.
- Status transitions accessible.

### Engineering Boundary

- AI is not the final authority for identity/safety verification.

## Final User Experience

Ideal journey:

```text
Welcome
   ↓
"We'll keep this simple."
   ↓
Identity ✓
   ↓
Phone ✓
   ↓
Profile →
   ↓
Safety check ✓
   ↓
"You're ready."
   ↓
Continue to Pyrintu
```

## Lock Note

Screen 3 was reviewed and explicitly approved in product discussion. It is now locked as a UX contract on `feature/ux-screen-3`; implementation remains separate from the UX specification.

# Screen 4 — Welcome / Guided Introduction

**Status:** Approved / ready to lock

## Purpose

Give a newly authenticated user a clear mental model of Pyrintu before asking them to create a profile or preferences.

The user should leave this screen understanding:

`What Pyrintu does → how the journey works → what happens next`

This is a guided welcome, not a long tutorial.

## Core Message

### Heading

`Welcome to Pyrintu`

### Supporting Message

`Pyrintu helps you move from a promising connection to a real relationship. We'll guide you through your first step.`

### Primary Action

`Let's begin`

### Secondary Action

`Skip introduction`

## Experience Structure

The screen has three conceptual layers:

`Welcome → What Pyrintu does → What happens next`

The user is not asked for profile information on this screen.

## Visual Composition

### Desktop

Use a centered, spacious composition containing:

- Pyrintu identity
- welcome heading
- supporting message
- simple visual journey
- primary CTA
- secondary skip action

### Mobile

Prioritize:

- Pyrintu identity
- welcome heading
- supporting message
- visual journey
- Let's begin
- Skip introduction

The screen should feel spacious rather than dense.

## Visual Story

The visual should communicate:

`You → Understand what you want → Compatible people → Shared experience → Real relationship`

Use the same conceptual language established by the Landing Page.

Do not introduce a conflicting visual metaphor.

## Three-Step Explanation

### 01 — Tell Pyrintu about you

`Share the things that help Pyrintu understand your social preferences.`

### 02 — Tell Pyrintu what you want

`Describe the kind of connection or experience you're looking for.`

### 03 — Let Pyrintu help with the rest

`Discover compatible opportunities, shared activities, and connections that have the potential to grow.`

These explanations remain high-level. The purpose is to explain the journey, not every feature.

## Progress Indicator

Show that onboarding is a sequence without making it feel like a form.

Recommended presentation:

```text
● ○ ○ ○
Your first step
```

Avoid large numerical counters such as `1/17`.

The onboarding should feel guided rather than pressured.

## Primary CTA Behavior

When the user selects:

`Let's begin`

The system:

`Persist guide_started → Open Profile Creation`

The next destination is:

`Screen 5 — Profile Creation`

The transition should feel immediate and intentional.

## Skip Behavior

The `Skip introduction` action is always visible.

When selected, present:

### Message

`You can explore Pyrintu without the introduction. You can revisit guidance later from Help.`

### Actions

- Skip
- Continue introduction

Do not use guilt-based or pressure-based copy.

## Skip State

When the user skips:

`guided_intro_status = skipped`

The user continues to:

`Profile Creation`

Contextual guidance remains available later.

The introduction should not repeatedly reopen unless the user explicitly requests it.

## Resume Behavior

If onboarding is interrupted:

### Message

`Welcome back. Let's continue where you left off.`

The user resumes from the last completed onboarding state rather than restarting.

## First-Time Behavior

The full Welcome experience appears once per user by default.

It may be shown again only when:

- the user explicitly requests onboarding help
- Pyrintu substantially changes onboarding and intentionally reintroduces guidance

Normal product use must never be interrupted by a forced tutorial.

## Contextual Guidance After Skip

Skipping the introduction does not disable later help.

Example contextual guidance:

### Title

`Create your profile`

### Message

`This helps Pyrintu understand what kinds of connections may fit you.`

The hint may be dismissed and must not block progress.

## AI Behavior

AI does not dynamically generate the Welcome experience.

The welcome copy and structure are deterministic product behavior.

AI becomes useful later when users begin expressing their own intent.

## Personalization Boundary

Do not use inferred sensitive traits on the Welcome screen.

Acceptable:

`Welcome`

Potentially unnecessary:

Showing inferred personality characteristics before the user provides them.

Not acceptable:

`We know you're an introvert.`

The user controls how Pyrintu understands them.

## Privacy

No additional permissions are requested on this screen.

Do not request:

- contacts
- exact location
- camera
- microphone
- calendar
- social graph access

The purpose of this screen is to explain Pyrintu before collecting additional information.

## Safety

Provide lightweight access to:

- Safety
- Help

Safety content should remain secondary to the welcome experience.

Critical safety controls must never be obscured by onboarding.

## Loading State

Normally this screen requires minimal loading.

If onboarding state must be retrieved:

`Preparing your Pyrintu experience…`

The screen should remain usable whenever possible while state loads.

## Error State

### Message

`We couldn't load your onboarding progress.`

### Actions

- Try again
- Continue

Failure to retrieve onboarding state must not permanently block product access.

## Recovery State

### State unavailable

Continue with the current onboarding step where safe.

### Previous session interrupted

Resume from the last known state.

### Invalid onboarding state

Reset only the affected onboarding state while preserving the account.

### User message

`Let's restart this step. Your account is safe.`

## Accessibility Requirements

- semantic heading hierarchy
- keyboard navigation
- visible focus states
- screen-reader-compatible controls
- accessible progress indicator
- sufficient contrast
- no meaning conveyed only through animation
- reduced-motion support
- mobile-friendly touch targets
- skip action reachable without excessive navigation

The journey explanation must remain understandable without the visual illustration.

## Responsive Behavior

### Mobile

Priority order:

`Heading → Supporting message → Visual story → Three-step explanation → Let's begin → Skip introduction`

### Desktop

The visual story may sit beside the explanation while preserving the same CTA hierarchy.

## Analytics Events

Track:

- welcome_viewed
- welcome_started
- welcome_skip_clicked
- welcome_skip_confirmed
- welcome_continue_clicked
- welcome_completed
- onboarding_resumed
- contextual_help_opened

Do not collect private profile information in these analytics events.

## Performance

This should be one of the lightest authenticated screens.

Requirements:

- minimal JavaScript
- optimized illustration
- no video required
- no blocking third-party content
- fast transition to Profile Creation
- animation optional

## Acceptance Criteria

### Mental Model

- User understands what Pyrintu does.
- User understands the high-level journey.
- User knows what happens after `Let's begin`.

### Onboarding

- `Let's begin` leads to Profile Creation.
- `Skip introduction` is always available.
- Skip does not create guilt or friction.
- Progress is persisted.
- Interrupted onboarding can resume.

### Guidance

- Welcome appears once by default.
- Contextual guidance remains available later.
- The tutorial never becomes a mandatory maze.

### Privacy

- No unnecessary permissions requested.
- No inferred sensitive traits displayed.

### Accessibility

- Keyboard accessible.
- Screen-reader compatible.
- Reduced-motion compatible.

### Reliability

- Failure to load onboarding state does not permanently block access.
- Recovery is available.

## Final Intended Experience

```text
"I'm new here."
        ↓
"Oh, I understand what Pyrintu is."
        ↓
"That actually sounds different."
        ↓
"I know what happens next."
        ↓
"Okay, let's begin."
```

The experience must not feel like a long mandatory onboarding process.

## Lock Note

Screen 4 was reviewed and explicitly approved in product discussion. It is now locked as a UX contract on `feature/ux-screen-4`; implementation remains separate from the UX specification.

# Screen 5 — Profile Creation

**Status:** Approved / ready to lock

## Purpose

Create a user-controlled profile that gives Pyrintu meaningful context for recommendations while allowing the user to decide what is visible to other people.

The profile serves three purposes:

`Understand me → Represent me → Help Pyrintu find better opportunities`

The experience must not feel like a CV, dating profile, personality test, or generic registration form.

## Core Philosophy

Pyrintu should understand behavior and preferences rather than reduce users to labels.

The profile should capture:

- who the user is
- what they genuinely enjoy
- how they naturally connect with people
- what kinds of interactions feel comfortable
- what kinds of connections they are open to
- what they want others to know

## Screen Opening

### Heading

`Let's make your Pyrintu profile feel like you.`

### Supporting text

`A good profile isn't a perfect profile. Give people enough of the real you to start something meaningful.`

### Primary CTA

`Create my profile`

### Secondary action

`I'll do this later`

The user should immediately see the profile taking shape rather than facing a dense form.

## Live Profile Preview

The strongest visual element should be a live profile card.

Example structure:

```text
┌─────────────────────┐
│       PHOTO         │
│                     │
│   Display name      │
│   General location  │
│                     │
│   Short description │
│                     │
│   Interest chips    │
│                     │
│  What I'm looking   │
│  for...             │
└─────────────────────┘
```

The preview updates as the user adds information.

## Step 01 — Identity Basics

### Required / defaulted where available

**Display name**

The value may default from authentication where available, but remains editable.

### Product-required profile context

**Age / age-range representation**

**City / general location**

Exact residential location must not be exposed.

Example:

`Hyderabad`

not an exact home, hostel, or residential address.

## Profile Photo

Primary action:

`Add photo`

Secondary:

`Choose later`

Supporting message:

`A real photo helps people feel comfortable knowing who they're connecting with.`

The product must not imply a required appearance standard.

### Upload options

- Take a photo
- Choose from device

### Photo guidance

Preferred user-facing guidance:

`Choose a clear photo where people can easily recognize you.`

For a poor image:

`This photo may make it harder for people to recognize you. Try another one?`

Technical validation details remain implementation concerns and should not dominate the UX.

## Step 02 — A Little About You

### Prompt

`What are you like when you're around people you enjoy?`

Examples:

- `Quiet at first, then I won't stop talking about startups.`
- `Always up for badminton or discovering a new café.`
- `I like small groups more than huge crowds.`

Input placeholder:

`Write something in your own words...`

The input should support a meaningful answer without encouraging an essay.

## AI Assistance

After the user provides natural-language text, Pyrintu may offer structured suggestions.

Example input:

`I like badminton, startups, coffee, sometimes I'm shy but after knowing people I talk a lot.`

Possible structured preview:

- 🏸 Badminton
- 🚀 Startups
- ☕ Coffee
- 🌱 Takes time to open up
- 💬 Enjoys deeper conversations

Actions:

- `Use suggestions`
- `Edit`
- `Keep my wording`

The interface must clearly indicate:

`AI suggestion — you decide what stays.`

AI must never silently rewrite or publish profile content.

## Step 03 — Interests

### Heading

`What do you genuinely enjoy?`

Use a concise set of suggested interests rather than requiring the user to browse a very large taxonomy.

Example suggestions:

- 🏸 Badminton
- 💻 Building things
- 🚀 Startups
- 🎵 Music
- 🎬 Movies
- ☕ Cafés
- 📚 Reading
- ✈️ Travel
- 🎮 Gaming
- 🏃 Fitness

Action:

`Add your own`

Users can select multiple interests.

## Interest Intent

When useful, distinguish passive interest from willingness to use it as a social activity.

Example:

`Badminton`

Options:

- `I'd happily join`
- `Maybe`
- `Just something I enjoy personally`

This signal can later support opportunity formation without assuming every interest is a meetup preference.

## Step 04 — Social Style

### Heading

`How do you naturally connect with people?`

Use behavior-based language rather than personality labels.

Examples:

- Small groups
- One-on-one conversations
- Activity first, conversation later
- Deep conversations
- Casual conversations
- I like meeting new people
- I need some time to warm up

Multiple selections are allowed.

Avoid making `Introvert / Extrovert` the primary interaction model.

## Step 05 — Comfortable Group Size

### Question

`What's your ideal group?`

Options:

- Just me + one person
- 3–4 people
- 5–6 people
- Small group, flexible

This preference can feed later opportunity formation.

## Step 06 — What Are You Open To?

### Heading

`What kind of connection are you open to?`

Examples:

- New friends
- Activity partners
- Professional connections
- People with shared interests
- Small communities
- Exploring a new city

Multiple selections are allowed.

Pyrintu must not assume that every user wants the same type of relationship.

## Visibility and Privacy Controls

Every meaningful profile field must have a clear visibility policy.

Possible states:

- Visible to people you connect with
- Visible only to Pyrintu
- Hidden

Users should understand visibility before sharing information.

Exact location is never shown through the profile.

## Why Are You Asking This?

For unfamiliar fields, provide a concise explanation.

Example:

### Why are you asking about group size?

`It helps Pyrintu create opportunities that feel comfortable instead of putting you into groups that don't fit your social style.`

Users should understand what Pyrintu is doing and why.

## AI-Generated Profile Understanding

At the end of profile creation:

### Heading

`Here's how Pyrintu currently understands you.`

Example:

> Hyderabad-based builder who enjoys badminton, startups and relaxed cafés. You prefer smaller groups, take a little time to warm up, and enjoy activity-based connections.

Then ask:

`Is this a good representation of you?`

Actions:

- `Looks right`
- `Change something`

The AI is reflecting user-provided signals rather than deciding who the user is.

## Explainability

Provide:

`Why did Pyrintu say that?`

Example explanation:

`Small groups came from your preference for 3–4 people.`

`Activity-based connections came from your selected interests and social-style preferences.`

The product should make AI-derived summaries understandable and correctable.

## Profile Readiness

Avoid meaningless percentage completion such as `87% Complete`.

Instead show meaningful readiness:

### `Your profile is ready for better recommendations.`

Possible checklist:

```text
✓ Identity
✓ Photo
✓ About you
✓ Interests
✓ Social style
○ Availability
```

Availability belongs to Screen 7 and must not be required to complete Screen 5.

## Save Behavior

Profile information should autosave where safe.

Message when appropriate:

`Your progress is saved.`

If the user returns later:

`Continue building your profile`

## Exit Behavior

If the user exits while editing:

`Your changes are saved automatically.`

Actions:

- Keep editing
- Leave

Do not use fear-based loss warnings.

## Empty State

For a new profile:

`Add your first details`

`Your profile preview will appear here.`

No awkward blank-state layout.

## Validation

Validation should be human and actionable.

Prefer:

`Add a little more so people can get a sense of you.`

over technical validation language.

For interests:

`Choose at least one thing you'd genuinely enjoy doing with others.`

## Error States

### Photo upload failure

`We couldn't upload that photo.`

Actions:

- Try again
- Choose another photo

### Save failure

`We couldn't save that change. Your earlier information is safe.`

Actions:

- Retry
- Continue

### AI unavailable

`Pyrintu couldn't generate the profile summary right now.`

Actions:

- Try again
- Continue without summary

The user must never be blocked because an AI service failed.

## AI Failure Boundary

The product must work without AI.

Architecture principle:

`Deterministic profile collection → Optional AI enhancement → Profile ready`

AI failure must never prevent basic profile completion.

## Privacy and Safety

Do not request contacts here.

Do not silently import the user's entire social graph.

Do not publish the profile outside the intended Pyrintu experience without the required user action and visibility rules.

Users must be able to access applicable privacy, visibility, and safety controls from the profile experience.

## Safety-Sensitive Content

The profile system must enforce the eventual content-safety policy for clearly prohibited content.

User-facing recovery language should remain neutral:

`This section contains content that can't be used on Pyrintu. Try describing yourself another way.`

Provide a recovery path rather than a dead end.

## First-Time User Guide

### Guide 02 — Profile

**Target:** `Create Profile`

**Message:** `Tell Pyrintu a little about yourself so we can make better recommendations.`

**Primary action:** `Create Profile`

Contextual guidance may appear beside unfamiliar controls but must never cover the primary form or important safety controls.

## Accessibility Requirements

- keyboard navigation
- screen-reader labels
- logical focus sequence
- accessible chips and toggles
- accessible photo upload
- visible focus indicators
- sufficient contrast
- error announcements
- reduced-motion support
- touch-friendly controls
- no information conveyed only through color

AI-generated changes must be announced clearly, for example:

`Pyrintu suggested changes to your profile.`

## Responsive Behavior

### Mobile

Priority order:

`Profile preview → Identity → Photo → About → Interests → Social style → Group size → Connection preferences → AI understanding → Save & continue`

### Desktop

Use a two-column composition where practical:

- Left: profile editing
- Right: live profile preview + Pyrintu understanding

The information hierarchy remains equivalent on smaller screens.

## Analytics Events

- profile_viewed
- profile_started
- profile_photo_added
- profile_about_started
- interest_added
- interest_removed
- social_style_selected
- group_size_selected
- connection_preference_selected
- ai_profile_summary_requested
- ai_profile_summary_accepted
- ai_profile_summary_edited
- ai_profile_summary_rejected
- profile_saved
- profile_completed
- profile_abandoned
- profile_validation_error
- profile_save_failed

Never send raw profile text or private personal information into generic analytics.

## Performance

- optimized image uploads
- image compression before upload where appropriate
- autosave without blocking interaction
- asynchronous AI generation
- no full-page reloads
- graceful degradation when AI is unavailable

## Acceptance Criteria

### User understanding

- User knows why each meaningful field exists.
- User understands what is visible to other people.
- User can see how Pyrintu understands their profile.

### Profile

- Live preview updates.
- Profile can be saved incrementally.
- User can edit AI suggestions.
- AI never silently changes profile content.

### Privacy

- Visibility is understandable.
- Exact location is not required.
- Contacts and social graph access are not requested.

### Reliability

- AI failure does not block profile completion.
- Upload failure is recoverable.
- Save failure preserves previous information.

### Accessibility

- Keyboard accessible.
- Screen-reader compatible.
- Mobile-friendly.

### Product quality

- Profile feels human rather than form-like.
- Profile captures behavioral and social-preference signals useful for later matching.

## Pyrintu Understanding Moment

The intended emotional moment is:

### `Here's what we understand about you.`

The user sees a concise summary based on their own inputs and can confirm or change it.

The experience should make the user feel understood without implying that Pyrintu knows more about them than they have provided.

## Final Intended Experience

```text
"I'm new here."
        ↓
"I understand what Pyrintu is."
        ↓
"I can make this profile feel like me."
        ↓
"Pyrintu shows me what it understood."
        ↓
"Yes — that's me."
```

## Lock Note

Screen 5 was reviewed and explicitly approved in product discussion. It is now locked as a UX contract on `feature/ux-screen-5`; implementation remains separate from the UX specification.

# Screen 6 — Social Preferences

**Status:** Approved / ready to lock

## Core Objective

Answer:

`What kind of social experience feels right for you?`

Capture:

- how the user likes to meet
- who and what environments feel comfortable
- communication style
- group preferences
- activity vs conversation preference
- planning style
- social boundaries
- preference importance
- preference confidence

The screen should understand social behavior without forcing psychological or personality labels.

## Opening Experience

### Heading

`Let's understand how you like to connect.`

### Supporting text

`There is no "right" way to socialize. Tell Pyrintu what feels natural to you.`

### Reassurance

`You can change these preferences anytime.`

## Preference Importance Model

Every major preference can have an importance level:

### Flexible

`Nice to have`

### Important

`I'd prefer this`

### Boundary

`This really matters to me`

This distinction separates soft preferences from meaningful constraints.

## Section — How Do You Like to Meet?

### Heading

`What kind of first interaction feels natural?`

Options:

- Activity first
- Conversation first
- Small group first
- One-on-one first
- Casual drop-in
- Structured activity
- Exploring somewhere together

Multiple selections are allowed.

Each selection can be marked:

- Nice to have
- Important
- Boundary

## Section — Group Comfort

### Heading

`What's your comfortable group size?`

Options:

- 1 person
- 2–3 people
- 4–5 people
- 6–8 people
- Flexible

Then ask:

`How important is group size to you?`

Example:

`4–5 people — Boundary`

## Section — Conversation Style

### Heading

`What kind of conversations do you enjoy?`

Options:

- Deep conversations
- Casual conversations
- Humor and banter
- Sharing ideas
- Learning from each other
- Talking about hobbies
- Professional conversations
- Quiet / low-pressure interaction

Avoid psychological labels.

## Section — Social Environment

### Heading

`What kind of environment helps you enjoy the experience?`

Options:

- Calm
- Lively
- Quiet
- Energetic
- Outdoor
- Indoor
- Structured
- Spontaneous

Then ask:

`Which environments do you generally avoid?`

Users can distinguish soft preferences from stronger boundaries.

## Section — Activity vs Conversation

### Heading

`When meeting someone new, what helps most?`

Use a simple spectrum:

`More activity — Balanced — More conversation`

The user can place a marker anywhere on the spectrum.

Provide an accessible categorical alternative:

- Activity-first
- Balanced
- Conversation-first

This becomes a continuous preference signal where supported without excluding keyboard or screen-reader users.

## Section — Getting Comfortable

### Heading

`How do you usually warm up to new people?`

Options:

- I open up quickly
- I prefer a little time
- Activity helps me relax
- I like someone else starting the conversation
- I prefer observing first
- It depends on the situation

This is a matching signal and must not be presented as a public personality judgment.

## Section — Communication Style

### Heading

`What communication style feels best to you?`

Options:

- Direct
- Friendly and casual
- Thoughtful
- Playful
- Practical
- Low-pressure

Then ask:

`Anything you'd rather avoid?`

Examples:

- Constant messaging
- Very personal questions early
- Aggressive networking
- Large group chatter
- High-pressure invitations

## Section — Planning Style

### Heading

`How do you like plans to happen?`

Options:

- Plan ahead
- A little notice is enough
- Spontaneous is fine
- Depends on the activity

Then:

`How much flexibility do you usually have?`

Detailed schedule data belongs to Screen 7 — Availability and should not be duplicated here.

## Section — What Are You Open To?

### Heading

`What kinds of connections feel meaningful to you?`

Options:

- New friends
- Activity partners
- Professional connections
- Learning connections
- Local communities
- People with shared interests
- Exploring a new city
- Collaborative projects

The user may select multiple options.

Pyrintu must not assume all users want the same relationship type.

## Section — Social Boundaries

### Heading

`What should Pyrintu avoid?`

Examples:

- Large groups
- Last-minute plans
- Very crowded places
- Loud environments
- Alcohol-centered settings
- Competitive activities
- Professional networking
- One-on-one first meetings
- Long-distance travel for meetups

The user controls which boundaries matter.

## Boundary Language

Pyrintu should say:

`We'll try to avoid opportunities that conflict with your preferences.`

And:

`Preferences aren't guarantees. Some situations may not fit perfectly.`

The product must not overpromise perfect matching.

## Preference Confidence

Allow users to express certainty:

- I'm sure
- Somewhat
- Still figuring it out

This lets Pyrintu distinguish stronger signals from tentative ones.

## Natural-Language Mode

Offer an alternative entry path:

### Prompt

`Rather type it?`

Example input:

`I usually like small groups, prefer doing something rather than sitting and talking, and I'm okay with spontaneous plans.`

Action:

`Structure this for me`

Pyrintu may convert this into a structured preview:

- Group size → Small
- Interaction → Activity-first
- Planning → Flexible

The user must review before accepting.

## AI Behavior

AI may:

- extract preference signals
- identify contradictions
- ask for clarification
- summarize the user's preferences

AI must not silently create hard boundaries.

Example:

User: `I generally prefer quieter places.`

Pyrintu should ask:

`I understood "quieter places" as a preference. Is that right?`

Actions:

- Yes
- Make this important
- Make this a boundary

## Contradiction Handling

If the user selects contradictory preferences, do not silently choose one.

Example:

`Large groups — Important`

and

`Small groups — Important`

Prompt:

`You selected both small and large groups as important.`

Then:

`Would you like to prioritize one, or keep both flexible?`

Actions:

- Prefer small groups
- Prefer large groups
- Keep both

## Preference Summary

At completion, show:

### `Here's what feels right for you`

Example:

> **Small groups** — You prefer 3–5 people.
>
> **Activity-first** — You enjoy having something to do while meeting.
>
> **Calmer environments** — You generally prefer quieter spaces.
>
> **Flexible planning** — You're comfortable with both planned and spontaneous opportunities.

Each summary item should show its importance where useful.

## Explainability

Allow:

`Why does this matter?`

Example:

`We use this preference when comparing possible people, groups, activities, and environments.`

Every preference should be easy to change.

## Preference Influence

Do not expose matching coefficients or numerical weights.

Instead show human language such as:

- Very important to you
- Important to you
- Flexible

The underlying matching algorithm belongs to technical architecture.

## Privacy

Social preferences may be:

- Pyrintu-only
- Shared selectively when relevant
- Private

The default should favor minimum exposure.

Sensitive social preferences are not automatically visible to other users.

## Safety Boundaries

Preferences that affect safety should influence opportunity formation without exposing the private reason to other users.

For example:

`I don't want one-on-one first meetings.`

This can affect recommendations without becoming public profile information.

## Autosave

Preferences should save progressively.

States:

`Saving…`

`Saved`

If synchronization fails:

`Couldn't save this change. We'll retry.`

Previously saved preferences remain safe.

## Error States

### AI unavailable

`Pyrintu can't structure this right now.`

Actions:

- Try again
- Keep writing manually

### Save failure

`We couldn't save that preference.`

Action:

`Retry`

### Network failure

`You're offline. Your changes will sync when you're back online.`

The exact offline persistence architecture belongs to technical design.

## Completion State

### Heading

`Your social preferences are ready.`

### Supporting message

`Pyrintu has a clearer picture of what kind of experiences fit you.`

### Primary CTA

`Continue`

Destination:

`Screen 7 — Availability`

### Secondary action

`Review preferences`

## Editing After Onboarding

Users can later access:

`Profile → Social Preferences`

and change any preference.

Changes take effect prospectively.

## First-Time User Guide

### Guide 03 — Social Preferences

**Target:** `Your Preferences`

**Message:** `Tell us what kind of people, activities, group sizes, and environments feel right for you.`

Contextual guidance should appear only when needed and must never block primary controls.

## Accessibility Requirements

- All chips usable by keyboard
- Checkbox and radio semantics where applicable
- Slider exposes accessible value
- Screen-reader labels describe selection and importance
- Progress state announced
- Errors announced
- No color-only importance indicators
- Sufficient contrast
- Reduced-motion support
- Touch-friendly controls

For the activity/conversation spectrum, provide the accessible alternatives:

- Activity-first
- Balanced
- Conversation-first

## Responsive Behavior

### Mobile

Structure:

`Question → Options → Importance → Explanation → Next`

Only one major decision should dominate the viewport.

### Desktop

A two-column layout may be used:

- Left: questions and controls
- Right: live preference summary

The information hierarchy remains equivalent.

## Analytics Events

- social_preferences_viewed
- social_preferences_started
- social_preference_selected
- social_preference_importance_changed
- social_preference_removed
- natural_language_preference_started
- ai_preference_structuring_requested
- ai_preference_structuring_accepted
- ai_preference_structuring_edited
- ai_preference_structuring_rejected
- preference_conflict_detected
- preference_conflict_resolved
- social_preferences_saved
- social_preferences_completed
- social_preferences_abandoned

Never send raw personal preference text to generic analytics.

## Matching Boundary

This screen collects signals. It does not expose the matching algorithm.

Later Match Reasoning may explain relevant signals in human terms.

## Acceptance Criteria

### User Understanding

- User understands why preferences are collected.
- User understands importance levels.
- User can change preferences later.

### Matching Quality

- Strong preferences can be distinguished from soft preferences.
- Boundaries are distinguishable from simple likes.
- Uncertainty can be represented.
- Contradictions are resolved explicitly.

### AI

- AI assists with structuring.
- AI explanations are visible.
- AI cannot silently create hard constraints.
- AI failure does not block completion.

### Privacy

- Sensitive social preferences are not automatically public.
- User controls visibility.

### UX

- Progress feels lightweight.
- No personality-label dependency.
- User receives a useful preference summary.

### Accessibility

- Keyboard accessible.
- Screen-reader compatible.
- Mobile accessible.

## Final Intended Experience

```text
"Finally, Pyrintu asked how I actually like meeting people."
        ↓
"I can be specific without being labeled."
        ↓
"Pyrintu understands what matters to me."
        ↓
"I can change it whenever I want."
```

## Lock Note

Screen 6 was reviewed and explicitly approved in product discussion. It is now locked as a UX contract on `feature/ux-screen-6`; implementation remains separate from the UX specification.

# Screen 7 — Availability

**Status:** Approved / ready to lock

## Core Objective

Convert a user's real-world availability into useful, flexible signals for opportunity formation.

The product should answer:

`When are you realistically open to a good Pyrintu opportunity?`

Availability is about opportunity readiness, not surveillance.

## Opening Experience

### Heading

`When are you open to something good?`

### Supporting text

`Tell Pyrintu roughly when you're available. You don't need to plan every minute.`

### Reassurance

`You can change this anytime.`

## Availability Entry Modes

Do not begin with a large Monday–Sunday calendar.

Ask:

### `How would you like to tell us your availability?`

Options:

- `Set my usual times`
- `Tell us in my own words`
- `I'll decide later`

This keeps setup lightweight.

## Mode A — Usual Times

Users define recurring availability in simple blocks.

Example:

```text
Weekdays
After 6 PM

Weekends
Mostly open
```

Exact time windows remain optional unless the user wants more precision.

## Quick Availability Presets

Offer useful presets:

### Weekdays

- Morning
- Afternoon
- Evening
- Flexible

### Weekends

- Morning
- Afternoon
- Evening
- Flexible

### Custom

`Choose specific times`

Presets should support fast setup without forcing calendar-level detail.

## Exact Time Windows

When the user wants precision:

```text
Monday
6:00 PM — 9:00 PM

Wednesday
6:30 PM — 10:00 PM

Saturday
10:00 AM — 4:00 PM
```

Use friendly time-range controls rather than a dense calendar grid.

## Recurring Availability

Support readable recurring rules such as:

`Every weekday after 6 PM`

`Saturday afternoons`

The user should be able to understand the rule in natural language.

## Natural-Language Mode

Provide:

### `Rather tell Pyrintu?`

Example:

`I'm usually free after 6 on weekdays and most of Saturday, but this weekend I'm busy.`

Action:

`Structure my availability`

Possible structured preview:

```text
Weekdays
After 6 PM

Saturday
Flexible

Exception
This weekend unavailable
```

Then:

`Here's what I understood.`

Actions:

- `Looks right`
- `Edit`
- `Keep writing`

AI must never silently create or remove availability.

## Availability Certainty

Allow the user to distinguish:

### Reliable

`Usually available`

### Flexible

`Often available`

### Uncertain

`Maybe available`

This helps Pyrintu understand that an opening can have different levels of confidence.

## Flexibility

### Heading

`How flexible are you?`

Use a spectrum:

`Need advance notice — Very flexible`

Accessible alternatives:

- Need advance notice
- Some flexibility
- Flexible
- Very flexible

## Notice Preference

### Question

`How much notice do you usually prefer?`

Options:

- Same day is okay
- A day or two
- A few days
- A week or more
- Depends on the activity

This can affect opportunity timing later.

## Duration Preference

### Heading

`How much time do you usually enjoy spending?`

Options:

- Under 1 hour
- 1–2 hours
- 2–3 hours
- Half day
- Depends on the activity

This represents preference, not a commitment.

## Repeating vs Occasional Availability

### Question

`Are these times usually available or just occasional?`

Options:

- Usually available
- Sometimes available
- Only for specific plans

The system must not treat a temporary opening as a permanent schedule.

## Exceptions

Provide a lightweight way to override recurring availability.

Example:

```text
Usual:
Saturday afternoon

Exception:
This Saturday
Unavailable
```

Another example:

```text
Usual:
Weekdays after 6 PM

Exception:
Tomorrow
Available only after 8 PM
```

Specific exceptions take precedence over recurring rules.

## This Week Quick Adjustment

Provide:

### `Anything different this week?`

Options:

- Nothing different
- Add a busy time
- Add extra availability

This avoids making users edit their entire recurring schedule for a temporary change.

## Calendar Integration Boundary

Google Calendar, Outlook, or other calendar integrations are **not required during V1 onboarding**.

The initial product must work without calendar access.

A later integration may offer an explicit:

`Connect your calendar`

with a clear permission and privacy explanation.

Calendar integration belongs to a later product/integration specification.

## Location Relationship

Availability does not require exact location tracking.

The product may later combine availability with the user's selected general location or meetup preferences, but Screen 7 must not require continuous location access.

## Privacy

Availability is potentially sensitive.

The default model is:

`Pyrintu uses availability to form opportunities.`

Other users should not automatically see a recurring private schedule such as:

`Free every Tuesday from 6–9 PM.`

When an opportunity is actually relevant, the system may expose only the information required for that opportunity, such as:

`Available Saturday at 6:30 PM.`

Broader visibility requires appropriate user control.

## Privacy Explanation

### `Why do you need this?`

`Availability helps Pyrintu suggest opportunities that can realistically happen—not just matches that look good on paper.`

## AI Behavior

AI may:

- parse natural-language availability
- identify recurring patterns
- detect ambiguity
- summarize availability
- suggest clarification

AI must not invent precise times.

Example:

User:

`I'm generally free after work.`

Pyrintu should ask:

`When you say “after work,” should I treat that as around 6 PM on weekdays?`

Actions:

- `Yes`
- `Change`
- `I'll set it myself`

## Ambiguity Handling

Example:

`Usually free Saturday.`

Ask:

`Roughly when on Saturday?`

Options:

- Morning
- Afternoon
- Evening
- Most of the day
- Custom

The system should resolve important ambiguity before using the signal for opportunity formation.

## Conflict Detection

If the user creates:

```text
Saturday
2 PM–6 PM available
```

and later:

```text
Saturday
4 PM–5 PM unavailable
```

Pyrintu should show:

`We found an overlap.`

Then explain:

`Your availability will be treated as 2–4 PM and 5–6 PM.`

Actions:

- `Accept`
- `Edit`

No silent conflict resolution.

## Overlapping Rules

Example:

```text
Weekdays:
After 6 PM

Tuesday:
Unavailable
```

Result:

`Tuesday: Unavailable`

Specific exceptions override recurring rules, and the UI should explain this precedence.

## Availability Summary

At completion:

### `Here's when you're usually open`

Example:

```text
Weekdays
Usually after 6 PM

Saturday
Mostly flexible

Sunday
Afternoons

Notice preference
A day or two

Flexibility
Moderate
```

Then:

`Does this look right?`

Actions:

- `Looks right`
- `Change something`

## Opportunity Readiness

After confirmation:

### Heading

`You're ready for better-timed opportunities.`

### Supporting text

`Pyrintu can now look for possibilities that fit both your preferences and your real availability.`

### Primary CTA

`Continue`

Destination:

`Screen 8 — Intent Creation`

## Save Behavior

Availability edits should autosave.

Possible states:

`Saving…`

`Saved ✓`

`Syncing…`

`Couldn't save`

A failed update must not overwrite the last valid saved schedule.

## Empty State

When no availability is provided:

### Heading

`Tell us when you're generally free.`

Options:

- `Set usual times`
- `Tell us in my own words`
- `Skip for now`

Skipping remains possible when product rules permit.

## Skip Behavior

If the user skips:

`availability_status = incomplete`

Pyrintu can later ask for availability when the user wants to participate in an opportunity.

User-facing message:

`No problem. We can ask when it becomes useful.`

This preserves lightweight onboarding.

## Loading State

Examples:

`Saving your availability…`

`Understanding your schedule…`

`Checking your availability rules…`

No infinite loading state.

## Error State

### Save failure

`We couldn't save that change. Your earlier availability is still safe.`

Actions:

- Retry
- Continue

### AI parsing failure

`Pyrintu couldn't structure that schedule right now.`

Actions:

- Try again
- Set it manually

### Network failure

`You're offline. Your changes can sync when you're connected again.`

## Recovery Behavior

If a partial update occurs:

- preserve the last valid schedule
- show the current unsaved change
- allow retry
- never silently reset the entire availability model

If a schedule becomes invalid:

`Let's fix one part of your availability before continuing.`

Highlight only the problematic rule.

## First-Time User Guide

### Guide 04A — Availability

**Target:** Availability summary / setup control

**Message:** `Tell Pyrintu roughly when you're open so we can suggest opportunities that can actually happen.`

**Primary action:** `Set availability`

**Secondary action:** `Skip for now`

This is a contextual extension of the progressive onboarding flow.

## Accessibility Requirements

- keyboard-accessible time controls
- accessible weekday selectors
- screen-reader-readable availability summaries
- accessible slider alternative
- clear focus states
- errors announced
- no color-only availability indicators
- reduced-motion support
- large touch targets
- readable time formatting

The user must be able to complete availability without dragging a visual calendar.

## Responsive Behavior

### Mobile

Priority order:

`Heading → Simple availability choice → Current availability → Edit → Flexibility → Notice preference → Summary → Continue`

### Desktop

Possible layout:

- Left: availability controls
- Right: live availability summary

A dense calendar is optional, not the default.

## Analytics Events

- availability_viewed
- availability_started
- availability_preset_selected
- availability_time_window_added
- availability_time_window_removed
- availability_recurring_rule_created
- availability_exception_created
- availability_flexibility_changed
- availability_notice_preference_changed
- availability_duration_preference_changed
- natural_language_availability_started
- ai_availability_structuring_requested
- ai_availability_structuring_accepted
- ai_availability_structuring_edited
- availability_conflict_detected
- availability_conflict_resolved
- availability_saved
- availability_completed
- availability_skipped
- availability_abandoned
- availability_save_failed

Do not place the user's detailed private schedule into generic analytics payloads.

## Matching Boundary

Screen 7 collects availability signals.

It does not decide:

- who the user should meet
- whether a meetup is safe
- whether an opportunity is available
- whether another user is compatible

Those belong to later systems.

Availability is an input.

## Acceptance Criteria

### Simplicity

- User can provide useful availability without filling a detailed calendar.
- Presets make setup fast.
- Natural language is supported.

### Accuracy

- Ambiguity is clarified.
- Exceptions override recurring rules.
- Conflicts are surfaced.
- Uncertainty is represented.

### Flexibility

- User can choose a rough schedule.
- User can specify exact windows when desired.
- Notice preference is captured.
- Flexibility is captured.

### Privacy

- Exact weekly availability is not automatically exposed to other users.
- Calendar access is not required during onboarding.
- No continuous location permission is requested.

### AI

- AI parses but does not invent precise availability.
- AI-generated interpretation is reviewable.
- AI failure never blocks manual setup.

### Reliability

- Autosave exists.
- Failed saves preserve the previous valid state.

### Accessibility

- Keyboard accessible.
- Screen-reader compatible.
- No calendar dragging requirement.

## Final Intended Experience

```text
"I don't need to schedule my whole life."
        ↓
"I can tell Pyrintu roughly when I'm open."
        ↓
"It understands my flexibility and notice preference."
        ↓
"It can now look for opportunities that can actually happen."
```

The experience should feel like opportunity readiness, not calendar administration.

## Lock Note

Screen 7 was reviewed and explicitly approved in product discussion. It is now locked as a UX contract on `feature/ux-screen-7`; implementation remains separate from the UX specification.
