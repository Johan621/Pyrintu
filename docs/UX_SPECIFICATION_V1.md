# PYRINTU — UX SPECIFICATION V1.0

**Status:** Draft / Next active workstream

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
