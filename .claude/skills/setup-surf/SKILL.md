---
description: Set up a private rider profile and activate or research a surf region. Use when the user is new, changes destination, or asks to configure surf-guide.
argument-hint: "[region or base, optional]"
disable-model-invocation: true
---

# Set up surf-guide

Configure this clone without publishing personal data.

## 1. Inspect before asking

Read:

- `CLAUDE.md`
- `templates/profile.md`
- `templates/active-location.md`
- `locations/README.md`
- `$ARGUMENTS`

Check whether `data/profile.md` and `data/active-location.md` already exist.
Preserve existing answers unless the user asks to replace them.

## 2. Ask one compact batch

Ask only for missing information, in no more than six numbered questions:

1. Surf region and approximate base town or neighbourhood; never require an
   exact address.
2. Maximum drive time and transport/access constraints.
3. Ability, years/frequency, and comfortable versus absolute-maximum face
   height.
4. Hard exclusions: bottom types, hazards, localism, isolation, access, or
   daylight/time constraints.
5. Optional preferences: left/right, beach/point/reef, crowd tolerance, and
   current technique goal.
6. Current board plus height, weight, and successful/unsuccessful past boards
   if board-buying help is wanted.

Explain that weight and board history are optional for forecasts but useful for
board selection.

## 3. Write private configuration

Create or update only:

- `data/profile.md`
- `data/active-location.md`
- `data/sessions/<region-slug>.csv`
- `data/sessions/<region-slug>.md`
- `data/calibration/<region-slug>.md`

Use the templates exactly. Store the base only at town/neighbourhood precision.
Never write private answers under `locations/`.

## 4. Resolve the public location pack

Look for `locations/<country-slug>/<region-slug>/README.md`.

If it exists:

- verify that its coverage matches the user's drive radius;
- reference it from `data/active-location.md`;
- do not duplicate it under `data/`.

If it does not exist:

1. Explain that a one-time location research pass is required.
2. Research a bounded zone of roughly 5–12 established public breaks.
3. Apply the two-source rule from `CLAUDE.md`.
4. Create a local draft under
   `data/location-drafts/<country-slug>/<region-slug>/` using
   `locations/_template/`.
5. Include source URLs, confidence labels, approximate coordinates, timezone,
   orientation, swell/wind/tide guidance, hazards, access, sections, and
   exposure class.
6. Label map/geometry deductions as inference. Do not invent empirical
   multipliers or calibration.
7. Point `data/active-location.md` at the local draft.

Do not add a new public location pack automatically. At the end, offer to
prepare the factual draft as a reviewable contribution after the user has
checked it. Promotion requires explicit user approval and must exclude the
profile, base, sessions, and private calibration.

## 5. Initialize session files

Copy the exact CSV header from `templates/sessions.csv`. In the Markdown log,
state that first-hand observations are personal ground truth and must not be
published automatically.

## 6. Finish

Report:

- active region;
- shared pack or local draft path;
- number of included spots;
- any fields left unknown;
- that `data/` is ignored by Git;
- the next command: `/surf tomorrow`.
