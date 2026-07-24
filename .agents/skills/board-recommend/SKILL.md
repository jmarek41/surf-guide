---
name: board-recommend
description: Recommend a suitable surfboard from rider ability, body parameters, board history, target waves, and available new, used, or rental options.
license: MIT
---

# Board recommendation

Recommend a board for the user's request using
`method/board-recommendation.md`.

## Profile first

Read:

- `data/profile.md`
- `data/boards/history.md` if it exists
- the active location pack when destination waves matter

If board fields are incomplete, ask one compact batch for:

- weight and height;
- ability and surf frequency;
- current board dimensions, volume, construction, and verdict;
- two successful and unsuccessful past boards, if available;
- duck-dive, paddle, stability, durability, and turning priorities;
- target waves and progression goal;
- destination, trip/session duration, budget, and available acquisition modes:
  new, used, rental, or any.

Do not require unrelated personal data.

## Recommend the board before the acquisition mode

Build a rider-and-wave brief:

- target shape family and why;
- a range, not a single magic volume;
- useful length/width/thickness/foil/rail/tail/fin characteristics;
- hard walk-aways and flexible trade-offs;
- target waves and conditions.

Base the range primarily on successful board history. Litres per kilogram is a
comparison tool, not a universal ability formula.

The core recommendation must remain valid whether the board is new, used, or
rented. Acquisition mode changes availability, price, condition, and commitment;
it does not change the rider's fundamental fit.

## Research available options

Because inventory and prices change, verify options live. For each candidate
capture:

- URL and retrieval date;
- acquisition mode: new | used | rental;
- price and currency, including rental duration where relevant;
- stated dimensions, volume, construction, fins, condition, and repairs;
- fit against the brief;
- unknowns to ask the shop, owner, or rental operator;
- availability and size certainty;
- confidence and sources for model specifications.

Never invent dimensions from a model name. Use two independent sources for
model specifications where possible; otherwise label them unverified.

Write recommendations only to `data/boards/recommendations.md`.

## Acquisition-specific checks

### New board

- Verify manufacturer specifications, construction, included fins, warranty,
  lead time, and local availability.
- Separate catalogue claims from independent information.
- Do not recommend ordering custom dimensions without explaining the uncertainty.

### Used board

- Separate seller statements from verified model specifications.
- Apply the inspection checklist in `method/board-recommendation.md`.
- Ask for repair history, clear photos, dimensions, and volume.
- Compare price only when current local evidence exists.

### Rental board

- Verify the exact model or at least dimensions, volume, construction, and fin
  setup; do not accept “mid-length” or “hybrid” as sufficient detail.
- Check rental duration, swap policy, damage terms, deposit, pickup hours, and
  whether the recommended size can be reserved.
- Prefer operators that allow board swaps when conditions change or the first
  choice proves unsuitable.

## Rank and answer

Return:

1. Recommended target specification.
2. Ranked available options with fit verdict:
   strong | plausible | poor | insufficient information.
3. Trade-offs caused by new, used, or rental availability.
4. Missing information and the smallest next action.

## Transaction boundary

Do not contact a shop, seller, owner, or rental operator; reveal private contact
details; make an offer; reserve a board; buy; or rent anything without the
user's explicit instruction.

Finish with the smallest next action: verify inventory, request specs/photos,
inspect a used board, compare candidates, reserve a rental with approval, or
walk away.
