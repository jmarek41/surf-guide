# Flight sources for short-trip scans

Flight sources and route schedules change. Verify current behavior and label
unofficial sources.

## Source order

1. **SerpAPI Google Flights:** structured all-carrier search when the user
   supplies a private key.
2. **Airline fare source:** optional best-effort confirmation for an airline
   with a usable public endpoint. Undocumented endpoints may disappear and must
   not be presented as official APIs.
3. **Google Flights link:** always provide a browser handoff.

## Best-effort Ryanair source

Ryanair's public website currently uses JSON endpoints under
`services-api.ryanair.com`. They are undocumented and may change without
notice. Treat them as best-effort, send modest traffic, and always retain the
browser fallback.

Route list:

```text
https://services-api.ryanair.com/views/locate/searchWidget/routes/en/airport/{ORIGIN}
```

Window round-trip fares:

```text
https://services-api.ryanair.com/farfnd/v4/roundTripFares?departureAirportIataCode={ORIGIN}&outboundDepartureDateFrom={DATE}&outboundDepartureDateTo={DATE}&inboundDepartureDateFrom={DATE}&inboundDepartureDateTo={DATE}&market=en-gb&adultPaxCount=1&arrivalAirportIataCodes={DEST}&limit=5
```

Monthly cheapest-per-day curve:

```text
https://services-api.ryanair.com/farfnd/v4/oneWayFares/{ORIGIN}/{DEST}/cheapestPerDay?outboundMonthOfDate={YYYY-MM-01}&currency={CURRENCY}
```

Schedule check:

```text
https://services-api.ryanair.com/timtbl/3/schedules/{ORIGIN}/{DEST}/years/{YEAR}/months/{MONTH}
```

An all-null cheapest-per-day response is not proof by itself that a route never
operates. Cross-check the route list and schedule.

For a usable route curve, compute P25 and median from available, non-null days
over roughly the next 60 days. Evaluate outbound and inbound separately:

- at or below P25 → great;
- above P25 but at or below median → fair;
- above median → pricey.

The worse leg determines the round-trip verdict. If there are too few available
days for a stable curve, show the raw fare without a percentile label.

## SerpAPI setup

Users create their own account at:

```text
https://serpapi.com/users/sign_up
```

The private key is available after sign-in at:

```text
https://serpapi.com/manage-api-key
```

Store it as either:

```text
SERPAPI_API_KEY=<private value>
```

in the process environment or in ignored `data/secrets/serpapi.env`. Set the
file mode to `0600`. Never commit, print, quote, or paste the value into an AI
conversation.

Use `scripts/serpapi_flights.py`; it reads and redacts the key.

The pricing page currently lists a free tier, but quota and terms can change:

```text
https://serpapi.com/pricing
```

## Google Flights query

The official SerpAPI engine documentation is:

```text
https://serpapi.com/google-flights-api
```

Use:

- `engine=google_flights`;
- one or more comma-separated `departure_id` airport codes;
- destination airport code(s) in `arrival_id`;
- explicit `outbound_date` and `return_date`;
- `type=1` for round trip;
- private currency;
- `stops=1` for nonstop, or `stops=2` for one stop or fewer;
- `deep_search=true` only when the more precise result justifies its latency.

An initial round-trip search identifies departing itineraries and prices.
Follow the selected itinerary's `departure_token` when return-flight details
must be confirmed. Do not call a route bookable until both directions and the
total price are clear.

Allow cache use by default. SerpAPI documents identical cached requests within
its cache window as not consuming monthly searches.

## Price verdict

When `price_insights` exists:

- `low` → great;
- `typical` → fair;
- `high` → pricey.

If price insights are absent, report the amount without inventing a market
verdict.

For an airline-specific forward-price curve, compare each leg only with the same
route and season. Log the method and use the more conservative verdict when
sources conflict.

## Google Flights fallback

Always emit browser links for the configured origins. A missing API key or
failed pricing source must not suppress a confirmed surf opportunity.

## Failure handling

- Missing key: skip SerpAPI and explain the fallback.
- HTTP 401/403: key invalid or unauthorized; do not retry with the key exposed.
- HTTP 429 or quota error: stop SerpAPI calls for this run.
- Empty route: retry the allowed stop count only if the private travel policy
  permits it.
- Changed response schema: preserve the raw error privately, link current
  documentation, and avoid a price verdict.
- Volatile fare: include retrieval time and advise browser verification before
  booking.
