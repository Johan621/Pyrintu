# PYRINTU — UX SPECIFICATION V1.0

**Status:** Screen 1 approved; remaining screens in draft / next active workstream

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