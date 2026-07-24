# Short-trip scan workflow

This workflow finds unusually good, reachable surf windows across a configured
destination portfolio. It is deliberately two-phase: a cheap wide net followed
by expensive confirmation only for candidates.

## 1. Resolve the request

- Convert relative dates to explicit local dates.
- Default to 7–10 days.
- Load the private rider profile and `data/scan/config.md`.
- Select configured entries from `scan/destinations.md`.
- Do not hardcode one surfer's size, period, crowd, or travel thresholds.

## 2. Phase 1 — batched triage

Build one Open-Meteo Marine multi-location request from the selected catalog
rows marked `triage`.

Set `timezone=auto` so each location's daily aggregates and returned timestamps
use its local timezone. For multiple coordinates, verify that the response
contains one timezone-resolved object per requested coordinate before comparing
calendar dates.

Use daily:

```text
swell_wave_height_max,swell_wave_period_max,
swell_wave_direction_dominant,wave_height_max,wave_period_max
```

Also request three-hourly:

```text
secondary_swell_wave_height,secondary_swell_wave_period
```

Request the configured 7–10-day window, then verify the returned date arrays
instead of assuming the provider supplied the full horizon. If the provider or
selected model returns fewer days, scan only the received dates and report the
shortened horizon. Days 8–10 remain direction-of-travel evidence even when
available.

The default broad Atlantic triage floor is:

- primary swell at least 0.8 m and 10 s; or
- secondary swell at least 0.5 m and 10 s.

For Mediterranean wind-swell catalogs, the default floor is 0.7 m at any
period. These are discovery defaults, not the final GO bar. A private config may
raise or lower them.

Do not apply a size ceiling during triage. Large offshore energy may translate
into the target range at a documented refuge or shadowed spot.

When many cells pass, deep-confirm the closest roughly four candidates and list
the remaining triage hits as not yet deep-checked.

## 3. Phase 2 — confirmation

For every candidate:

1. Fetch hourly primary, secondary, combined, and wind-wave components plus MSL
   tide timing. Use tertiary swell only when the selected model provides it;
   Open-Meteo currently documents tertiary components for GFS Wave models.
2. Fetch hourly atmospheric wind and gusts across the full daylight window.
3. Compare Open-Meteo best-match with `ncep_gfswave016` when available.
4. Check the country's official forecast or a public nearshore surf source.
5. Apply the destination's exposure/refuge notes.
6. For class B/C spots, require a nearshore or visual confirmation before a
   confident breaking-wave size claim.

Models exposed by one API are a model spread, not two independent publishers.
Say so.

## 4. Opportunity verdicts

- **GO:** clears every configured surf and travel requirement with adequate
  source agreement.
- **Near-GO:** one explicit, bounded shortfall, such as period just below the
  target or one fewer surf day than preferred.
- **Watch:** sources disagree or a sub-grid translation remains unconfirmed.
- **No-go:** materially misses the configured bar.

Do not convert a watch into a GO because flights are cheap.

For days 4–7, label the opportunity developing. For days 8–10, label it
direction-of-travel only and do not encourage booking without a closer recheck.

## 5. Travel/surf ratio

Use the private limits rather than a universal policy.

The default template distinguishes:

- short-haul: roughly half a day each way;
- long-haul: roughly one day each way;
- routes with a connection: recalculate rather than trusting the catalog tier.

Catalog tiers are reference hints only. Compute the effective tier from the
private origins, schedules, transfers, and trip limits on every scan.

Count usable surf days after realistic arrival, transfer, board pickup, return,
and flight times.

## 6. Flight gate

Fetch prices only for GO and near-GO candidates.

Follow `method/flight-sources.md`:

- SerpAPI Google Flights when a private key is available;
- optional best-effort airline sources where documented;
- pre-filled Google Flights links for every origin as fallback.

Prices are live observations, not guarantees. Report bags, seats, rental car,
board rental, and transfers as excluded unless explicitly included.

## 7. Output

Return:

1. scan window and confidence;
2. ranked GO opportunities;
3. near-GO and watch candidates;
4. closest no-go cases when no destination clears the bar;
5. surf window, source agreement, approximate face height, crowd/localism,
   travel shape, board-rental note, and live flight observation;
6. next recheck date.

## 8. Private logging

Append one entry to `data/scan/scan-log.md`.

For every priced route append one row to
`data/scan/flight-price-log.csv`. Never write origins, prices, bookings, or
credentials into the public catalog.
