# Forecast sources

Provider mechanics change. Verify URLs and parameter names against official
documentation when a request fails. The endpoints, fields, batching, and model
comparison below were live-checked on 2026-07-24.

## Default source stack

### Open-Meteo Marine

Endpoint:

```text
https://marine-api.open-meteo.com/v1/marine
```

Useful hourly fields:

```text
wave_height,wave_direction,wave_period,
swell_wave_height,swell_wave_direction,swell_wave_period,
secondary_swell_wave_height,secondary_swell_wave_direction,secondary_swell_wave_period,
tertiary_swell_wave_height,tertiary_swell_wave_direction,tertiary_swell_wave_period,
wind_wave_height,wind_wave_direction,wind_wave_period,
sea_level_height_msl
```

Use the active IANA timezone and the shortest practical forecast horizon.
Comma-separated latitude and longitude lists can batch multiple cells; response
order follows input order.

### Open-Meteo atmospheric wind

Endpoint:

```text
https://api.open-meteo.com/v1/forecast
```

Fields:

```text
wind_speed_10m,wind_direction_10m,wind_gusts_10m
```

When wind confidence matters, compare explicitly selected atmospheric models
where they are available rather than treating one blend as certainty.

### Wave model spread

Open-Meteo can expose multiple marine models. A practical European comparison
has been the default/best-match result versus NOAA GFS Wave:

```text
models=best_match,ncep_gfswave016
```

Treat model names as version-sensitive. If a model returns null or the API
rejects it, consult current Open-Meteo documentation and report that the second
arm was unavailable.

Different models served by the same API are a model comparison, not two
independent publishers. Label them honestly.

## Independent confirmation

Use at least one of:

- the country's official marine/weather service;
- a public surf-specific nearshore forecast page;
- a trustworthy cam or same-day visual report.

Nearshore confirmation is particularly important for exposure class B/C.
Respect site terms and access controls. Do not scrape around blocks or reproduce
proprietary tables.

## MET Norway

MET Norway can be useful, but its API requires an identifying User-Agent and
responsible caching. Generic Claude WebFetch does not provide reliable header
control, so it is excluded from the default workflow. A future helper may add it
only if it follows the official terms.

## Tide

Use `sea_level_height_msl` for timing and stage. Prefer an official local tide
source for chart-datum heights. Label the datum and do not mix them.

## Attribution

Every answer must link providers actually used. Open-Meteo output must include:

> Weather data by [Open-Meteo.com](https://open-meteo.com/)

See `ATTRIBUTION.md`.

## Fetch discipline

- Batch same-provider/same-field locations.
- Fetch nearshore pages only for relevant class B/C candidates.
- Avoid repeated requests for unchanged data.
- Preserve the forecast values used for a session in the private session log;
  do not reconstruct them later from a newer model run.
