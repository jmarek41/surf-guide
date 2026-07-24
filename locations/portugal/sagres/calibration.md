# Sagres — anonymized public calibration

These summaries were generalized from a private 2026 trip log. Raw session rows,
the rider profile, board history, base, and personal narrative are not included.
All current observations come from one independent contributor, even where the
same pattern repeated many times.

## Evidence baseline

The private source log contains 67 spot checks across 40 dates. Aggregate
forecast-versus-reality verdicts are 35 hits, 14 partials, and 18 misses.
Publishing those aggregates does not publish session times, the board used,
travel base, or personal performance.

| Spot | Hits / checks | Operational use | Confidence |
|---|---:|---|---|
| Tonel | 8 / 8 | exposed regional anchor | medium-high |
| Cordoama | 3 / 4 | broadly trust exposed input | medium |
| Mareta | 6 / 9 | use south-coast cell, then section geometry | medium |
| Beliche | 11 / 17 | derate/cross-check by direction and period | medium |
| Arrifana | 2 / 5 | headland translation required | low-medium |
| Castelejo | 1 / 3 | exposed size, banks/wind still uncertain | low |
| Amado | 4 / 16 | coarse grid is weak on section-level wind shelter | low |
| Zavial | 0 / 3 | never commit from the offshore grid alone | low |

The table includes spots with at least three checks. Two one-off checks are
retained in the private aggregate totals but are not enough to publish a
spot-level success rate.

These are repeated observations from one contributor, not independent forecast
verification studies.

## Source/geometry rules

| Source or geometry | Condition bucket | Generalized behaviour | Observations | Independent contributors | Counterexamples | Evidence label | Confidence |
|---|---|---|---:|---:|---|---|---|
| Offshore grid at Tonel | W/NW swell | Exposed Tonel broadly reflects regional swell size and is a useful anchor | 8 | 1 | Section quality still varies | community-observed | medium |
| Cape shadow at Beliche | NW 315°+ with modest/short-period energy | Tip-cell offshore size can substantially overstate surf reaching the bay | 17 checks total across mixed conditions | 1 | High-energy or more westerly swell can still produce good surf | multi-source geometry + community-observed | medium |
| Arrifana headland | N-heavy NW swell | Bay can break smaller than fully exposed beaches; this can make it a size refuge | 2 | 1 | Insufficient independent contributors | community-observed | low |
| Amado north headland | Wind approximately true N | Southern bay may be cleaner than the open cell; shelter weakens when wind backs NNW | 16 checks total across mixed conditions | 1 | Several misses; gusts can penetrate | public-source geometry + community-observed | low-medium |
| Zavial W/WNW wrap | Longer-period W/WNW | Point/bay can receive more energy than a coarse south-coast reading suggests | 3 | 1 | Size does not guarantee peeling waves; short-period cases failed | community-observed | low |
| Crossing SE secondary at the Sagres tip | W/NW primary with a significant short-period SE secondary | Exposed Tonel can turn pushy and disorganized beyond what primary alone suggests, while the same SE energy can feed Mareta's sheltered east-corner rights | 2 | 1 | Exact size/period thresholds are single-observation; west-side mirror untested | community-observed | low |

## Conservative operational rules

### Tonel versus Beliche

Tonel and Beliche are close enough to share regional offshore input but must not
share breaking-wave size:

- Tonel is exposed to W/NW and is the safer grid anchor.
- Beliche sits behind Cape St Vincent. Deep-W direction and longer period
  increase its chance of receiving energy.
- On NW, quote Beliche only as uncertain/derated unless a nearshore source or
  visual check confirms it.

Do not publish an exact multiplier until independent observations support it.

### Beliche direction/period buckets

The following is a one-contributor working calibration. Use it as a prior, then
confirm nearshore:

| Offshore primary direction | Working behavior | Counterexample requirement |
|---|---|---|
| deep W, approximately 295° or less | energy commonly reaches the bay when primary period is at least roughly 7 s | a sub-6 s case was flat despite westerly direction |
| 296–305° | plausible with sufficient size/period | small or short-period edge cases can be weak |
| 306–310° | energy-gated; longer period materially improves consistency | short-period or dominant N/NW wind-wave can overstate the face |
| 311°+ | normally deep shadow unless offshore energy is substantial | high-energy NW produced surf despite the shadow |

Across roughly 14 relevant checks, provisional offshore-primary-to-face
translations clustered around 0.7–0.9× for deep W and 0.5–0.6× near the shadow
edge. These are not universal multipliers and require independent validation.

Always start from primary swell. A large N/NW wind-wave can inflate combined
height without wrapping into clean Beliche surf.

### Amado wind shelter

Treat the N-headland shelter as a narrow possibility, not a guarantee:

- most plausible with wind near true N;
- much less reliable as wind backs NNW or gusts increase;
- section-specific and invisible to a coarse atmospheric grid;
- requires a cam, visual check, or conservative uncertainty label.

### Zavial wrap

Long-period W/WNW can wrap into Zavial despite a south-facing bay. Confirm with a
nearshore source. A size signal does not prove that beach peaks will peel; add a
closeout/section-quality warning.

Use a period gate on the nearshore signal: when the offshore primary is only
about 5 s, an apparent long-period nearshore value has produced a false
positive. With offshore primary at least roughly 7–8 s, long-period W/WNW
nearshore guidance has been more useful.

## Additional geometry rules

### Mareta and south-facing cliff bays

South-facing bays with cliffs at both ends can have a narrow sheltered/peeling
corner while the open middle is disorganized:

- the upwind cliff shelters its lee;
- the cliff first contacted by the swell can create the wrap;
- the useful corner changes with wind and swell direction.

Repeated Mareta observations support an east-side right-hand wrap during E/SE
energy and wind. The mirrored west-side/left-hand behavior on SW energy remains
an unvalidated prediction.

### Crossing SE secondary at the Sagres tip

When a short-period SE secondary stacks onto the W/NW primary in the Sagres-tip
cell, evaluate combined height as well as primary swell:

- exposed Tonel can become pushy and harder to paddle, with a polluted face —
  treat a large stacked combined value as possible step-up territory;
- the same SE energy can feed Mareta's east-corner wrap, so compare the two
  before defaulting to the exposed beach.

Both observations come from one contributor within one season. No exact
secondary size, period, or combined-height threshold is validated for
publication.

### Amado and Arrifana N-wind gate

The north-headland refuge worked most plausibly with wind close to true N,
roughly 340–360°. It failed repeatedly as wind backed NNW, approximately
320–340°, or as gusts penetrated the bay.

At Arrifana the useful shelter can be dawn-only on a day when wind direction
backs after sunrise. Treat this as a timing-sensitive visual-check rule, not a
daily wind multiplier.

### Bordeira versus Amado

Bordeira and Amado can share very similar offshore input but diverge in wind:

- Bordeira's open beach takes the prevailing N wind directly;
- Amado's southern section may receive narrow true-N shelter;
- the shelter must not be applied to NNW.

### Small-swell tide observations

Several small/short-period sessions became harder to catch as water filled in.
This supports prioritizing a lower-to-mid stage for weak swell, but exact MSL
thresholds are not published as universal rules because datum, bank, and spot
matter.

## Source-bias observations

`≥1` is a conservative lower bound for legacy rows whose private evidence was
not separately counted before this schema was adopted. Treat those rows as
evidence debt: do not increase their confidence until exact counts and private
references are backfilled.

| Source | Condition bucket | Observed bias | Adjustment | Observations | Independent contributors | Counterexamples | Confidence |
|---|---|---|---|---|---:|---|---|
| Open-Meteo blended wind | Levante before roughly 09:00 | sometimes too strong | confirm the dawn window with another source | ≥1 (legacy; not separately counted) | 1 | no independent counterexample yet | low |
| Open-Meteo wind | exposed west coast morning/midday in established nortada | sometimes too light | use an official/alternate ceiling and visual check | ≥1 (legacy; not separately counted) | 1 | evening-lull behavior differs | low |
| Open-Meteo wind | exposed west-coast evening lull | lighter value sometimes more accurate than a hotter alternate | do not extend a morning bias into evening | ≥1 (legacy; not separately counted) | 1 | morning/midday undercalls do not transfer | low |
| Surfline size | Beliche on high-energy NW | one substantial undercall | do not let one source veto corroborated high-energy input | 1 | 1 | no general bias established | low |
| Surf-Forecast size/period | Beliche/Zavial wrap cases | useful nearshore signal | retain the offshore-period artefact gate | ≥1 (legacy; not separately counted) | 1 | a short-offshore-period case was a false positive | low |
| combined wave height | crossing N/NW wind-wave | can overstate clean face | start from primary and secondary components | ≥1 (legacy; not separately counted) | 1 | no independent counterexample yet | low |
| Open-Meteo blended wind | forecast near-calm | a "dead calm" reading was sometimes light but not glassy in reality | do not promise a glass-off from this source alone; confirm visually or with a second source | ≥2 (not separately counted) | 1 | no independent counterexample yet | low |
| Windfinder wind | afternoon Levante peaks | sometimes too light | do not use as the sole tiebreaker on strong-Levante afternoons | 1 | 1 | no independent counterexample yet | low |
| Open-Meteo swell period | long-period W/WNW wrap events | can under-call period versus nearshore surf sources | when the offshore primary period is at least roughly 7–8 s, prefer the nearshore period reading for wrap spots; below that, apply the artefact gate | 1 | 1 | short-period offshore cases can make nearshore guidance misleading | low |

## Contribution priority

The highest-value future reports are independent observations that:

- test Beliche on clear direction/period buckets;
- test the Amado shelter transition from N to NNW;
- compare Arrifana directly with an exposed beach at the same time;
- separate Zavial point size from beach-peak quality.
