# Private forecast calibration

> Local-only. Store under `data/calibration/`. Do not commit.

## Source-bias matrix

| Source | Condition bucket | Bias | Adjustment | Sessions | Counterexamples |
|---|---|---|---|---:|---|

## Spot rules

| Spot | Swell/wind/tide bucket | Observed behaviour | Confidence | Sessions | Counterexamples |
|---|---|---|---|---:|---|

## Candidate public lessons

Generalized lessons may be drafted here. Evidence references in this table stay
private and must not be copied into `locations/`.

| Candidate ID | Public spot | Condition bucket | Proposed generalized behaviour | Observations | Independent contributors | Counterexamples / uncertainty | Evidence refs (private) | Target public file | Status |
|---|---|---|---|---:|---:|---|---|---|---|

Allowed status values:

- `needs-more-evidence`
- `candidate`
- `proposed`
- `approved`
- `declined`
- `promoted`

Only explicit user approval can move an entry to `approved`. Mark it `promoted`
only after the anonymized rule has actually been added to the public location
calibration. Follow `method/calibration-promotion.md`.
