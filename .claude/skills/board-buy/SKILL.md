---
description: Build a used-surfboard buying brief, research a destination market, or evaluate a listing against the rider profile and target waves.
argument-hint: "[destination, goal, or listing URL/text]"
disable-model-invocation: true
---

# Board buying assistant

Help with `$ARGUMENTS` using `method/board-buying.md`.

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
- destination, timing, budget, and whether resale is required.

Do not require unrelated personal data.

## Choose the mode

### Buying brief

Produce:

- target shape family and why;
- a range, not a single magic volume;
- useful length/width/thickness/foil/rail/tail/fin characteristics;
- hard walk-aways and flexible trade-offs;
- target waves and conditions;
- a used-board inspection checklist;
- resale considerations.

Base the range primarily on successful board history. Litres per kilogram is a
comparison tool, not a universal ability formula.

### Market research

Research current local channels and public listings. Because listings and prices
change, verify them live. For each candidate capture:

- URL and retrieval date;
- asking price and currency;
- stated dimensions, volume, construction, fins, condition, and repairs;
- fit against the brief;
- unknowns to ask the seller;
- resale liquidity;
- confidence and sources for model specifications.

Never invent dimensions from a model name. Use two independent sources for
model specifications where possible; otherwise label them unverified.

Write the shortlist only to `data/boards/shortlist.md`.

### Listing evaluation

Separate seller claims from independently verified specifications. Return:

- fit verdict: strong / plausible / poor / insufficient information;
- reasons and trade-offs;
- structural questions and photo requests;
- in-person checks;
- a price comparison only when current local evidence exists.

## Transaction boundary

Do not contact a seller, reveal private contact details, make an offer, reserve
a board, or purchase anything without the user's explicit instruction.

Finish with the smallest next action: request missing photos/specs, inspect in
person, compare candidates, or walk away.
