---
name: log-session
description: Log a surf session or visual spot check locally and update private forecast calibration. Use when the user reports what conditions were actually like.
license: MIT
---

# Log a session

Record the user's session report as private ground truth.

## Load

Read `data/active-location.md` first.

If it is missing, tell the user to run `/setup-surf`.

If its status is `none`, stop before resolving any region paths. Explain that
there is no active destination and offer either:

- `/setup-surf` to activate the next trip; or
- logging against a named archived region, but only after the user explicitly
  identifies that region.

For an active destination, verify that the region slug and every configured
session/calibration path are non-empty. Then read:

- `templates/sessions.csv`
- the active `data/sessions/<region>.csv`
- the active `data/sessions/<region>.md`
- the active `data/calibration/<region>.md`

## Clarify

Ask only for fields necessary to avoid a misleading record:

- date, public spot name, and approximate time window;
- surfed or visual check;
- observed face height, cleanliness, consistency, wind feel, and verdict;
- forecast numbers only if they were saved in the prior conversation or the
  user provides them;
- a primary and alternate wind-source value when both were captured;
- what matched and what missed.

Never invent missing forecast values. Leave CSV fields empty.

## Write locally

Append:

1. One concise prose entry to `data/sessions/<region>.md`.
2. One CSV row per checked spot to `data/sessions/<region>.csv`, following the
   exact template schema.

Update `data/calibration/<region>.md` only when the observation changes a useful
private rule. Preserve counterexamples and evidence counts.

## Evaluate a reusable lesson

Follow `method/calibration-promotion.md` after updating the private record.
Classify the result as:

- personal-only;
- needs more evidence;
- candidate public lesson; or
- update to an existing candidate.

For a candidate, add or update a stable entry in the private calibration's
`Candidate public lessons` table. Keep its evidence references private. Draft a
separate anonymized public rule with:

- public spot name and condition bucket;
- generalized model or geometry behaviour;
- observation count and independent-contributor count;
- counterexamples, uncertainty, evidence label, and confidence;
- the target `locations/<country>/<region>/calibration.md`.

Do not edit `locations/` during session logging. Show the proposed public rule
to the user and ask for explicit approval in a later contribution step.

## Privacy

Do not write raw sessions under `locations/`. If a lesson appears broadly
useful, separately offer the anonymized proposal described above.

Preparing a public contribution requires explicit approval. Repeated sessions
from this user still count as one independent contributor.

Finish by summarizing what was logged and which private calibration rule, if
any, changed. Also report the candidate lesson status without implying that it
has already been published.
