# Forecasting principles

## Sub-grid geography matters

Regional wave models cannot fully resolve small headlands, capes, cliffs,
harbours, reefs, or bay corners. The same model cell can represent two breaks
that behave very differently.

Common consequences:

- a cape-shadowed beach receives less swell than the grid reports;
- a cliff shelters one end of a bay while the open centre remains windy;
- long-period energy wraps into a point that short-period energy misses;
- reef or bathymetric focusing creates more breaking energy than a nearby beach.

Classify every spot A/B/C and calibrate it with observations.

## Primary, combined, and wind-wave energy

Combined wave height includes all components. A large short-period wind-wave
from another direction may increase the combined number without producing a
clean, rideable face.

Start with primary and secondary swell components. Then apply:

- direction and exposure;
- period and wrap potential;
- consistency penalty for crossing swell;
- wind-wave penalty or step-up warning;
- local empirical calibration.

## Wind direction before wind speed

The same wind speed can be damaging onshore, texturing cross-shore, or grooming
offshore. Strong offshore wind can still make paddling and takeoff difficult.
Interpret wind relative to each spot and rider, not as a universal speed cutoff.

Thermal coasts often have a calm dawn, daytime onshore build, and possible
evening easing. This is a pattern to verify, not assume.

## Tide data limitations

Model `sea_level_height_msl` is useful for high/low timing and stage. It is not
the same as local chart datum. Do not compare an MSL number directly with
published chart-datum thresholds.

Tide guidance is also spot- and sandbank-specific. Prefer broad stages until
observations justify a narrower rule.

## Ground truth and evidence

Raw observations are ground truth for what that surfer saw. They can reveal
model bias, but:

- one surfer remains one independent contributor across repeated sessions;
- a failed prediction is often more informative than a hit;
- counterexamples must remain visible;
- rules should be bucketed by direction, period, wind regime, tide, and time.

Maintain private calibration continuously. Promote only anonymized,
generalizable summaries to public location packs.

## Familiarity

For developing surfers, lineup familiarity and recent successful experience can
outweigh a small theoretical advantage at another spot. Use familiarity only as
a tie-breaker after surf quality, not as a reason to conceal better conditions.

## Face-height language

Body-height labels are approximate and vary by observer and region. State that
they are estimated face heights, use a range, and include uncertainty. Avoid
false precision.
