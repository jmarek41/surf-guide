# Public short-trip destination catalog

This catalog is a reusable starting set for `/scan`. It contains public surf
and travel facts, not a user's origin airports, budget, bookings, or scan
history.

Coordinates are forecast sampling points or approximate established-break
locations, not secret spots. Provider identifiers and routes can change; verify
them live when a destination reaches Phase 2.

The `Reference tier` is a rough European travel-shape hint, not a promise from
every origin. `/scan` must recalculate it from each user's private origins,
available schedules, transfers, and connection policy.

## Destination index

| ID | Region | Reference tier | Gateway airports | Prime tendency | Catalog confidence |
|---|---|---|---|---|---|
| canaries | Lanzarote + Fuerteventura | short-haul | ACE, FUE | Atlantic winter/shoulder swell | medium-high |
| lisbon | Ericeira + Peniche | short-haul | LIS | autumn through spring | high |
| north-portugal | Porto + Figueira da Foz | short-haul | OPO | autumn through spring | medium-high |
| sagres | Southwest Algarve | short-haul | FAO | multi-aspect, autumn through spring | high |
| cadiz | Cádiz coast | short-haul | SVQ, XRY, AGP | winter W/SW swell | medium |
| southwest-france | Landes + Biarritz | short-haul | BIQ, BOD | autumn swell; winter can be heavy | high |
| basque | Zarautz + San Sebastián | short-haul | BIO | autumn through spring | high |
| morocco | Taghazout + Imsouane | long-haul | AGA | winter groundswell | high |
| rome | Lazio coast | short-haul wildcard | FCO, CIA | SW/Libeccio wind-swell | medium |
| sardinia | West coast + Capo Mannu | short-haul wildcard | CAG, AHO | NW/Mistral wind-swell | medium |

## Phase-1 triage cells

Rows marked `triage` form the default 13-cell portfolio. A private configuration
may include a subset.

| Order | Destination | Cluster | Latitude | Longitude | Tier |
|---:|---|---|---:|---:|---|
| 1 | canaries | Lanzarote / Famara | 29.120 | -13.560 | Atlantic |
| 2 | canaries | Fuerteventura / El Cotillo | 28.680 | -14.015 | Atlantic |
| 3 | lisbon | Ericeira / Ribeira d'Ilhas | 38.990 | -9.420 | Atlantic |
| 4 | lisbon | Peniche / Baleal | 39.370 | -9.340 | Atlantic |
| 5 | north-portugal | Porto / Matosinhos | 41.170 | -8.690 | Atlantic |
| 6 | north-portugal | Figueira / Cabedelo | 40.150 | -8.870 | Atlantic |
| 7 | sagres | Tonel | 37.007 | -8.953 | Atlantic |
| 8 | cadiz | El Palmar | 36.230 | -6.070 | Atlantic |
| 9 | southwest-france | Seignosse | 43.699 | -1.441 | Atlantic |
| 10 | basque | Zarautz | 43.290 | -2.171 | Atlantic |
| 11 | morocco | Devil's Rock | 30.506 | -9.687 | Atlantic |
| 12 | rome | Banzai | 42.030 | 11.920 | Mediterranean |
| 13 | sardinia | Capo Mannu | 40.030 | 8.383 | Mediterranean |

## Confirmation spot cache

`—` means no verified public page was found; do not invent an identifier.

| Destination | Spot | Latitude | Longitude | Surf-Forecast slug | Exposure/refuge note |
|---|---|---:|---:|---|---|
| canaries | Famara | 29.120 | -13.560 | `Playade-Famara_1` | exposed beach |
| canaries | Caleta de Caballo | 29.117 | -13.640 | `Caletade-Cabello` | reef; advanced sections |
| canaries | El Cotillo | 28.680 | -14.015 | `Cotillo` | exposed beach |
| canaries | Grandes Playas | 28.710 | -13.830 | — | east-facing alternative |
| lisbon | Ribeira d'Ilhas | 38.990 | -9.420 | `Ribeira-Dilhas` | point/reef; crowd concentration |
| lisbon | Foz do Lizandro | 38.940 | -9.420 | `Fozdo-Lizandro` | beach alternative |
| lisbon | Cantinho da Baía | 39.370 | -9.340 | `Cantinho` | sheltered size refuge |
| lisbon | Lagide | 39.380 | -9.330 | `Lagide` | reef-influenced |
| lisbon | Molhe Leste | 39.350 | -9.370 | `Molhe-Leste` | breakwater shelter |
| north-portugal | Matosinhos | 41.170 | -8.690 | `Matosinhos` | harbour-sheltered beach |
| north-portugal | Espinho | 41.000 | -8.650 | `Espinho` | exposed beach/jetty |
| north-portugal | Furadouro | 40.873 | -8.679 | `Furadouro` | exposed beach |
| north-portugal | Cabedelo | 40.150 | -8.870 | `Cabedelo` | breakwater influence |
| north-portugal | Buarcos | 40.170 | -8.890 | `Buarcos` | long right when swell aligns |
| sagres | Tonel | 37.007 | -8.953 | `Tonel` | exposed anchor |
| sagres | Beliche | 37.025 | -8.965 | `Beliche` | Cape St Vincent shadow |
| sagres | Mareta | 37.050 | -8.860 | `Mareta` | use south-coast forecast cell |
| sagres | Cordoama | 37.110 | -8.940 | `Cordama` | exposed west coast |
| sagres | Castelejo | 37.101 | -8.947 | `Castelejo` | exposed west coast |
| sagres | Amado | 37.166 | -8.904 | `Praiado-Amado` | true-N section shelter only |
| sagres | Arrifana | 37.294 | -8.872 | `Arrifana` | headland size/wind refuge |
| cadiz | El Palmar | 36.230 | -6.070 | `Playa-El-Palmar` | exposed beach |
| cadiz | Fuente del Gallo | 36.290 | -6.110 | — | partial shelter |
| cadiz | Caños de Meca | 36.180 | -6.030 | `Canosde-Meca` | Cabo Trafalgar refuge |
| southwest-france | Les Bourdaines | 43.699 | -1.441 | `Les-Bourdaines` | exposed beach |
| southwest-france | Les Estagnots | 43.686 | -1.444 | `Les-Estagnots` | exposed beach |
| southwest-france | Hossegor La Sud | 43.662 | -1.447 | `La-Sud` | harbour/headland shelter |
| southwest-france | Le Prévent | 43.651 | -1.447 | `Capbreton-Le-Prevent` | Gouf/refuge behavior |
| southwest-france | Côte des Basques | 43.479 | -1.569 | `Cotedes-Basques` | sheltered high-energy option |
| basque | Zarautz | 43.290 | -2.171 | `Zarautz` | exposed multi-peak beach |
| basque | Zurriola | 43.327 | -1.973 | `Zurriola-hondartza` | city beach |
| basque | Sopelana | 43.391 | -3.002 | `Sopelana` | exposed beach |
| basque | Bakio | 43.434 | -2.802 | `Bakio` | exposed beach |
| basque | Mundaka | 43.409 | -2.695 | `Mundaka` | advanced, tidal river-mouth left |
| morocco | Devil's Rock | 30.506 | -9.687 | `Devils-Rock` | accessible point/beach |
| morocco | Banana Point | 30.501 | -9.683 | `Banana-Point` | right point |
| morocco | Panorama Point | 30.540 | -9.710 | `Panoramas` | right point |
| morocco | Imsouane Bay | 30.837 | -9.811 | — | long sheltered right |
| morocco | Cathedral Point | 30.844 | -9.823 | `Pointed-Imessouane` | more exposed point |
| morocco | Tamri | 30.730 | -9.850 | `Tamri-Plage` | exposed fallback beach |
| rome | Banzai | 42.030 | 11.920 | `Banzai_2` | reef/groynes hold wind-swell |
| rome | Santa Severa | 42.016 | 11.958 | — | structure-dependent |
| rome | Lido di Ostia | 41.726 | 12.276 | — | open beach wind-swell |
| rome | Fregene | 41.849 | 12.193 | — | open beach wind-swell |
| sardinia | Capo Mannu | 40.030 | 8.383 | `Capo-Mannu` | lee-side point in Mistral |
| sardinia | Putzu Idu | 40.030 | 8.390 | — | clean after Mistral eases |
| sardinia | Sa Mesa Longa | 40.046 | 8.398 | `Sa-Mesa-Longa` | reef-sheltered softer option |
| sardinia | Porto Ferro | 40.660 | 8.190 | `Porto-Ferro` | exposed NW beach |

## Destination notes

- **Canaries:** reef quality can be high, but shallow/heavy/localized sections
  require explicit flags. Famara and El Cotillo provide broader beach options.
- **Lisbon:** Ericeira points concentrate crowds; Peniche offers multiple
  aspects and Cantinho as a documented refuge.
- **North Portugal:** Matosinhos and Cabedelo can retain manageable surf when
  exposed beaches are oversized; verify pollution and access alerts live.
- **Sagres:** use the full public location pack and calibration rather than this
  cache for spot translation.
- **Cádiz:** winter W/SW pulses matter; Caños can be a refuge behind Cabo
  Trafalgar.
- **Southwest France:** open beaches become heavy quickly. La Sud, Le Prévent,
  and Côte des Basques are possible size refuges, not guaranteed easy surf.
- **Basque:** Zarautz is the broad beach baseline. Mundaka is advanced,
  tide-sensitive, crowded, and a river mouth; profiles may exclude it.
- **Morocco:** long-haul transfers and rental availability must be counted.
  Point crowds and local etiquette need explicit treatment.
- **Rome and Sardinia:** wind-swell wildcards. The wind that creates the swell
  may initially spoil open beaches; seek the lee structure or post-wind cleanup.

## Sources

These direct pages are reproducible entry points for the catalog. They do not
support every field or replace live Phase-2 verification. Spot mechanics that
have only one relevant source remain single-source even when a second page
supports regional access or tourism context.

| Destination | Direct source | Retrieved | Supports |
|---|---|---|---|
| canaries | [Surf-Forecast — Famara](https://www.surf-forecast.com/breaks/Playade-Famara_1) | 2026-07-24 | representative break orientation and nearshore forecast |
| canaries | [Turismo Lanzarote — Famara](https://turismolanzarote.com/playa/playa-de-famara/) | 2026-07-24 | official beach and access context |
| lisbon | [Surf-Forecast — Ribeira d'Ilhas](https://www.surf-forecast.com/breaks/Ribeira-Dilhas) | 2026-07-24 | representative break and nearshore forecast |
| lisbon | [Visit Portugal — Ericeira Surfing Reserve](https://www.visitportugal.com/en/content/ericeira-surfing-reserve) | 2026-07-24 | official regional surf context and named breaks |
| north-portugal | [Surf-Forecast — Matosinhos](https://www.surf-forecast.com/breaks/Matosinhos) | 2026-07-24 | representative break and nearshore forecast |
| north-portugal | [Matosinhos municipality beach guide](https://www.cm-matosinhos.pt/cmmatosinhos2020/uploads/writer_file/document/24234/beach_guide.pdf) | 2026-07-24 | official beach and surf context |
| sagres | [Sagres location-pack sources](../locations/portugal/sagres/sources.md) | 2026-07-24 | 66 numbered public references, including spot pages and regional indexes |
| sagres | [Surf-Forecast — Tonel](https://www.surf-forecast.com/breaks/Tonel) | 2026-07-24 | exposed anchor and nearshore forecast |
| cadiz | [Surf-Forecast — El Palmar](https://www.surf-forecast.com/breaks/Playa-El-Palmar) | 2026-07-24 | representative break and nearshore forecast |
| cadiz | [Cádiz tourism — El Palmar](https://www.cadizturismo.com/es/playas/el-palmar) | 2026-07-24 | official beach and surf context |
| southwest-france | [Surf-Forecast — Les Bourdaines](https://www.surf-forecast.com/breaks/Les-Bourdaines) | 2026-07-24 | representative exposed break |
| southwest-france | [Hossegor tourism — beaches](https://www.hossegor.fr/en/the-beaches/) | 2026-07-24 | official beach, access, and regional surf context |
| basque | [Surf-Forecast — Zarautz](https://www.surf-forecast.com/breaks/Zarautz) | 2026-07-24 | representative break and nearshore forecast |
| basque | [Basque tourism — Surfing Euskadi](https://turismo.euskadi.eus/en/surfing-euskadi/) | 2026-07-24 | official regional surf and skill-range context |
| morocco | [Surf-Forecast — Devil's Rock](https://www.surf-forecast.com/breaks/Devils-Rock) | 2026-07-24 | representative break and nearshore forecast |
| morocco | [Moroccan tourism — Agadir–Taghazout](https://www.visitmorocco.com/en/travel/agadir-taghazout/beach) | 2026-07-24 | official regional surf context |
| rome | [Surf-Forecast — Banzai](https://www.surf-forecast.com/breaks/Banzai_2) | 2026-07-24 | representative reef and nearshore forecast |
| rome | [Visit Lazio](https://www.visitlazio.com/en/) | 2026-07-24 | official regional context only; detailed surf mechanics remain single-source |
| sardinia | [Surf-Forecast — Capo Mannu](https://www.surf-forecast.com/breaks/Capo-Mannu) | 2026-07-24 | representative point and nearshore forecast |
| sardinia | [Sardegna Turismo — wind and waves](https://www.sardegnaturismo.it/en/search-wind-and-waves?language=en-gb) | 2026-07-24 | official Mistral, west-coast, and Capo Mannu context |

## Known limitations

- This is a discovery catalog, not Sagres-depth calibration.
- Provider IDs, airline routes, rental stock, access, and sandbanks change.
- A catalog entry never overrides live warnings, local law, or a private hard
  exclusion.
