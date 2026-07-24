# Data attribution and service notes

## Open-Meteo

Forecast data obtained from Open-Meteo are licensed under CC BY 4.0. Forecast
answers must include a nearby link such as:

> Weather data by [Open-Meteo.com](https://open-meteo.com/)

The free API is for non-commercial use and has usage limits. Review the current
[terms](https://open-meteo.com/en/terms) and
[license](https://open-meteo.com/en/license).

## MET Norway

MET Norway data require attribution under CC BY 4.0. API clients must identify
the application with a meaningful User-Agent and must avoid unnecessary
traffic. Claude WebFetch does not provide reliable control over that header, so
MET Norway is not a default automated source in this repository.

If a future helper client is added, it must follow the
[MET Weather API terms](https://api.met.no/doc/TermsOfService), including
identification and caching.

## Surf-specific and national sources

Surf-forecasting websites, national meteorological services, maps, and local
guides have their own terms. Link to their public pages, summarize sparingly,
and do not copy proprietary forecast tables or bypass access controls.

Surfline's undocumented endpoints are intentionally not part of this project.
Use its normal browser interface only when permitted.

## Location-pack sources

Every location pack maintains its own source list. A source link documents the
origin of a factual claim; it does not imply that the source endorses this
project.
