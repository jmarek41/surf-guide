# Data attribution and service notes

## Open-Meteo

Forecast data obtained from Open-Meteo are licensed under CC BY 4.0. Forecast
answers must include a nearby link such as:

> Weather data by [Open-Meteo.com](https://open-meteo.com/)

Marine answers must also follow the acknowledgement shown by the current
[Marine Weather API documentation](https://open-meteo.com/en/docs/marine-weather-api)
for the model actually used. For example, the documented ICON Wave output
requires attribution to the
[German Weather Service (DWD)](https://www.dwd.de/) as well as Open-Meteo.
Named GFS, ECMWF, or Météo-France requests should credit the upstream provider
identified in the current Open-Meteo data-source table.

The free API is for non-commercial use and has usage limits. Review the current
[terms](https://open-meteo.com/en/terms) and
[license](https://open-meteo.com/en/license).

## MET Norway

MET Norway data require attribution under CC BY 4.0. API clients must identify
the application with a meaningful User-Agent and must avoid unnecessary
traffic. Generic AI web-fetch tools do not always provide reliable control over
that header, so MET Norway is not a default automated source in this repository.

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

## SerpAPI Google Flights

Optional flight pricing uses the user's own SerpAPI account and its documented
Google Flights engine:

https://serpapi.com/google-flights-api

Do not publish API keys or cached private itineraries. SerpAPI and Google retain
their respective terms and marks.
