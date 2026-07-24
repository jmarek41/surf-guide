---
name: surf
description: Recommend where and when to surf from the active location using live swell, wind, tide, shared spot facts, and private calibration.
license: MIT
---

# Surf forecast

Answer the user's “where and when should I surf?” request.

## Preconditions

1. Resolve the requested date against the current system date. Default to
   tomorrow when no argument is supplied.
2. State the weekday and full date at the top.
3. Read `data/profile.md` and `data/active-location.md`.
4. If either is missing, stop and tell the user to run `/setup-surf`.
5. Read the active public location pack or local draft, then:
   - `method/forecast-workflow.md`
   - `method/forecasting-principles.md`
   - `method/forecast-sources.md`
   - the matching `data/calibration/<region>.md`
   - recent rows from `data/sessions/<region>.csv`

Never read unrelated private regions or board shortlists.

## Forecast

Fetch the smallest useful payload for all distinct offshore grid cells:

- Open-Meteo Marine hourly swell components, combined waves, wind-wave, and
  `sea_level_height_msl`;
- Open-Meteo Forecast hourly wind speed, direction, and gusts;
- the Open-Meteo blend versus GFS Wave model spread when swell confidence
  matters;
- a national meteorological or surf-specific public source for confirmation;
- nearshore spot pages for class B/C shadowed, wrapping, reef, or point breaks.

Batch Open-Meteo locations where possible. Do not fetch MET Norway through
generic WebFetch because its API requires an identifiable User-Agent.
Do not use undocumented or access-controlled endpoints.

## Rank

Follow `method/forecast-workflow.md`. In particular:

- evaluate every daylight window;
- apply exposure class before translating offshore swell into face height;
- rank expected surf quality;
- annotate hard exclusions and every material skill, hazard, crowd, localism,
  distance, access, and section-level consideration;
- include all spots that score well rather than arbitrarily limiting the list;
- state source disagreement and visual-check needs;
- check the next day before recommending a rest day.

## Answer format

Keep the answer operational:

1. Explicit date and forecast confidence.
2. Best window and top choice.
3. Ranked table of worthwhile spot × time windows.
4. “Why this could be wrong” with model splits, class B/C uncertainty, and
   missing nearshore checks.
5. Day-after status if the day is marginal.
6. Attribution links for forecast providers actually used, including
   “Weather data by Open-Meteo.com” when applicable.

Do not claim chart-datum tide heights from MSL-referenced model data. Do not
present inferred face height as a measured value.
