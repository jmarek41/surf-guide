---
name: scan
description: Scan configured short-trip destinations for exceptional reachable surf windows, then price flights only for confirmed candidates.
license: MIT
---

# Short-trip surf scan

Answer: “Is any configured destination about to be worth a short surf trip?”

Follow:

- `method/scan-workflow.md`
- `method/flight-sources.md`
- `scan/destinations.md`
- `method/forecasting-principles.md`
- `method/forecast-sources.md`

## Private configuration

Read:

- `data/profile.md`
- `data/scan/config.md`
- `data/scan/catalog-overlay.md` if it exists
- `data/scan/scan-log.md`
- `data/scan/flight-price-log.csv`

If `data/scan/config.md` is absent, create it from
`templates/scan-config.md` after asking one compact batch for:

- origin airports and acceptable ground-transfer time;
- included destinations or `all`;
- target face-height band and minimum period;
- cleanliness and crowd requirements;
- maximum nights and travel/surf ratio;
- board-rental requirement;
- currency and any price preference.

Never store an exact home address. Airport codes and an approximate home city
are sufficient.

## Run

1. Resolve and state the exact scan window. Default to the next 7–10 days.
2. Run the cheap, batched swell triage for configured catalog cells.
3. Deep-confirm only candidates, following the source and geometry gates.
4. Classify each result as GO, near-GO, watch, or no-go.
5. Price flights only for GO and near-GO candidates.
6. Rank by surf opportunity first. Price, crowd, and travel are clearly shown,
   not hidden.
7. Append the private scan and flight-price logs.

If SerpAPI is not configured, continue the surf scan and provide pre-filled
Google Flights links. Never ask the user to paste a private key into chat.

## Safety and authority

Forecasts and prices are volatile. State retrieval times and sources. Do not
book travel, reserve equipment, contact an operator, or spend money without
explicit user instruction.
