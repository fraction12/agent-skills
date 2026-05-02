# UX and Design Pass

Use this for user-facing changes after the base product direction is clear.

## UX Questions

Consider:

- What is the user's first moment of understanding?
- What is the primary path?
- What secondary paths exist?
- What information must be visible before action?
- What can be progressively disclosed?
- What happens when there is no data?
- What happens while loading?
- What happens on error?
- What happens after success?
- What states are permission-gated or disabled?
- What should mobile/responsive behavior be?
- What accessibility constraints matter?
- What copy/labels reduce confusion?

## States Checklist

Include states as relevant:

- default
- empty
- loading
- success
- error
- partial failure
- disabled
- permission denied
- unsaved changes
- destructive confirmation
- offline/stale data

## UX Options Template

```markdown
## UX Options

### Option 1 — <name>
- Layout/flow:
- Strength:
- Weakness:
- Best for:

### Option 2 — <name>
- Layout/flow:
- Strength:
- Weakness:
- Best for:

### Option 3 — <name, optional>
- Layout/flow:
- Strength:
- Weakness:
- Best for:

### Recommended UX
<Recommendation and why.>
```

## Prototype / Wireframe Choices

If the workspace has a prototype system, use it. Otherwise, produce the lightest useful artifact:

- Storybook state list
- Spec UI prototype package
- Microcanvas-viewable HTML/markdown
- plain markdown wireframe
- screen-by-screen flow

## UX Spec Update

Add to the spec:

- screens/components touched
- user journey
- interaction model
- states
- copy/label guidance
- accessibility notes
- analytics events if relevant
