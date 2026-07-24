# Forecast workflow

This is the destination-agnostic process behind `/surf`.

## 1. Resolve time before data

Convert relative language to an explicit local date using the current system
date and the active location's IANA timezone. State the weekday and full date
before the forecast.

Interpret broad requests as follows unless the profile says otherwise:

- `today` or `tomorrow`: evaluate the full remaining daylight window;
- a named day: evaluate sunrise through sunset;
- `dawn`: sunrise through roughly two hours after sunrise;
- `evening`: the final three daylight hours;
- `weekend`: compare both days, not just daily maxima.

## 2. Load only relevant context

Read:

- private profile and active-location pointer;
- active public location pack or local draft;
- private calibration and recent comparable sessions;
- forecast source and interpretation methods.

The public spot pack supplies facts. The private profile supplies fit and hard
exclusions. Private session observations override generic assumptions for that
surfer but are not universal truth.

## 3. Fetch efficiently

1. Group spots by distinct offshore model cell.
2. Batch Open-Meteo marine cells into one request where practical.
3. Fetch hourly wind for the same cells.
4. Use model spread and independent public sources only where they change
   confidence or ranking.
5. For exposure class B/C spots, fetch a spot-specific nearshore source before
   making a confident size claim.

Use the smallest forecast horizon that answers the question. Treat forecasts
beyond roughly 48 hours as planning guidance, not a commitment.

## 4. Read the sea state

For each cell and daylight hour examine, in order:

1. primary swell direction, height, and period;
2. secondary and tertiary components;
3. combined wave height and wind-wave contamination;
4. wind direction, mean speed, and gusts;
5. tide timing and stage;
6. daily wind-cycle changes.

Do not convert combined offshore wave height directly into breaking face height.

## 5. Apply spot geometry

Every spot has an exposure class:

- **A — exposed:** offshore grid is broadly representative, still subject to
  bathymetry and banks.
- **B — shadowed:** headland, cape, island, harbour, or cliff reduces incoming
  energy. Do not quote the grid as spot size.
- **C — direction-sensitive:** wrap, reef focusing, point geometry, or
  section-specific behaviour requires a directional rule and nearshore check.

Research-based geometry is a prior. Empirical multipliers require logged
observations and must carry evidence counts.

## 6. Score spot × time windows

Score expected surf quality using:

- swell-direction fit;
- rideable swell energy and period;
- wind orientation and strength;
- tide fit;
- consistency and likely section quality;
- confidence in the size translation.

Rank surf quality first. Then annotate:

- estimated face-height band and confidence;
- fit against comfortable and maximum size;
- ability and section-level fit;
- named hazards;
- documented localism and likely crowd;
- travel and access implications;
- source disagreement and cam/visual-check need.

A hard exclusion in the rider profile does not erase a high-quality spot.
Surface it separately as excluded and explain why.

## 7. Use the whole daylight window

Do not reduce a day to morning versus afternoon. Look for:

- dawn glass;
- wind-direction changes;
- short tide windows;
- midday calm;
- genuine evening cleanup.

Reserve `glassy` for genuinely light wind. An easing but still side-onshore wind
is not a glass-off.

## 8. Rest-day gate

Before recommending rest on a marginal day, inspect the following day:

- meaningfully better next day: rest may be sensible;
- same or worse next day: recommend a lower-intensity session rather than
  saving energy for improvement that is not forecast.

State the following-day status whenever this gate is used.

## 9. Communicate uncertainty

Use confidence labels:

- **high:** models and nearshore sources agree; spot translation is calibrated;
- **medium:** incoming conditions agree but spot translation or wind timing is
  uncertain;
- **low:** models split, source is missing, or class B/C behaviour is
  uncalibrated.

Recommend a visual check when uncertainty is material. Never manufacture a
precise face height from weak evidence.
