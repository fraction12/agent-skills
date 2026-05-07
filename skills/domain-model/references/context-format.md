# CONTEXT.md Format

Use this format when creating or updating domain language docs.

## Structure

```md
# {Context Name}

{One or two sentence description of what this context is and why it exists.}

## Language

**Order**:
{A concise description of the term}
_Avoid_: Purchase, transaction

**Invoice**:
A request for payment sent to a customer after delivery.
_Avoid_: Bill, payment request

**Customer**:
A person or organization that places orders.
_Avoid_: Client, buyer, account

## Relationships

- An **Order** produces one or more **Invoices**
- An **Invoice** belongs to exactly one **Customer**

## Example dialogue

> **Dev:** “When a **Customer** places an **Order**, do we create the **Invoice** immediately?”
> **Domain expert:** “No — an **Invoice** is only generated once **Fulfillment** is confirmed.”

## Flagged ambiguities

- “Account” is currently ambiguous: could mean Customer, Workspace, or User.
```

## Rules

- Only include terms specific to this project's domain.
- Do not add general programming concepts, utility patterns, or implementation details.
- Prefer terms domain experts would recognize.
- Include avoided synonyms when they prevent future drift.
- Group terms under subheadings when natural clusters emerge.
- Add example dialogue when it clarifies boundaries between related concepts.

## Single vs multi-context repos

Single-context repo: one root `CONTEXT.md`.

Multi-context repo: a root `CONTEXT-MAP.md` lists contexts, where they live, and how they relate.

```md
# Context Map

## Contexts

- Ordering — receives and tracks customer orders
- Billing — generates invoices and processes payments
- Fulfillment — manages warehouse picking and shipping

## Relationships

- **Ordering → Fulfillment**: Ordering emits `OrderPlaced` events; Fulfillment consumes them to start picking
- **Fulfillment → Billing**: Fulfillment emits `ShipmentDispatched` events; Billing consumes them to generate invoices
- **Ordering ↔ Billing**: Shared types for `CustomerId` and `Money`
```

If multiple contexts exist, infer which one the current topic relates to. If unclear, ask one question.
