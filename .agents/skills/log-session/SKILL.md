---
name: log-session
description: Log a surf session or visual spot check locally and update private forecast calibration. Use when the user reports what conditions were actually like.
license: MIT
---

# Log a session

Record the user's session report as private ground truth.

## Load

Read:

- `data/active-location.md`
- `templates/sessions.csv`
- the active `data/sessions/<region>.csv`
- the active `data/sessions/<region>.md`
- the active `data/calibration/<region>.md`

If setup is missing, tell the user to run `/setup-surf`.

## Clarify

Ask only for fields necessary to avoid a misleading record:

- date, public spot name, and approximate time window;
- surfed or visual check;
- observed face height, cleanliness, consistency, wind feel, and verdict;
- forecast numbers only if they were saved in the prior conversation or the
  user provides them;
- what matched and what missed.

Never invent missing forecast values. Leave CSV fields empty.

## Write locally

Append:

1. One concise prose entry to `data/sessions/<region>.md`.
2. One CSV row per checked spot to `data/sessions/<region>.csv`, following the
   exact template schema.

Update `data/calibration/<region>.md` only when the observation changes a useful
private rule. Preserve counterexamples and evidence counts.

## Privacy

Do not write raw sessions under `locations/`. If a lesson appears broadly
useful, separately offer an anonymized summary:

- condition bucket;
- generalized observation;
- number of sessions;
- number of independent contributors;
- uncertainty and counterexamples.

Preparing a public contribution requires explicit approval. Repeated sessions
from this user still count as one independent contributor.

Finish by summarizing what was logged and which private calibration rule, if
any, changed.
