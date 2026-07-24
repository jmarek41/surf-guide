# Sagres and southwest Algarve — public location pack

- Country: Portugal
- Region slug: `sagres`
- IANA timezone: `Europe/Lisbon`
- Approximate coverage: Arrifana south to Sagres and east to Zavial
- National forecast source: IPMA
- Last researched: 2026-07

This seed pack covers established, publicly documented breaks. It does not
include a rider base or drive times.

## Offshore model cells

| Cell ID | Latitude | Longitude | Spots represented | Notes |
|---|---:|---:|---|---|
| west-north | 37.294 | -8.872 | Arrifana | Bay/headland translation required |
| west-central | 37.166 | -8.904 | Amado | Shared offshore input; local wind shelter differs by section |
| west-south | 37.105 | -8.944 | Cordoama, Castelejo | Exposed west-coast beaches |
| sagres-tip | 37.007 | -8.953 | Tonel, Beliche | Same regional input; radically different cape exposure |
| south-east | 37.050 | -8.860 | Zavial | W/WNW wrap and south-swell behaviour |

## Spots

### Praia da Arrifana

- Slug: `arrifana`
- Approximate coordinates: `37.294, -8.872`
- Orientation: west/northwest-facing bay
- Wave type / bottom: beach break with advanced reef/point section
- Exposure class: B — north headland partially shadows NW energy
- Supported swell: W to NW
- Supported wind: E/NE offshore; public sources also describe shelter from N
- Tide: broad low-to-mid preference; works outside it depending on section
- Sections and skill: centre beach is the more accessible section; reef/point
  section is faster and rock-exposed
- Hazards: rocks near higher tide, currents, narrow beach at high water
- Access: public clifftop access with a substantial return climb
- Crowd/localism: popular and frequently crowded; schools use the bay
- Confidence: medium-high
- Evidence label: multi-source; headland-size translation also
  community-observed
- Sources: S1–S4

### Praia do Amado

- Slug: `amado`
- Approximate coordinates: `37.166, -8.904`
- Orientation: west
- Wave type / bottom: multi-peak beach break
- Exposure class: C — exposed swell, but section-level N-wind shelter is
  direction-sensitive
- Supported swell: W to NW
- Supported wind: E/NE offshore; a true N wind may be reduced near the south
  end, but this requires visual confirmation
- Tide: broad mid-tide starting point; banks change
- Sections and skill: multiple peaks allow separation by level; power increases
  quickly with size
- Hazards: rocks at the edges, rips, shifting banks
- Access: established public beach access and parking
- Crowd/localism: popular with schools and visitors
- Confidence: medium
- Evidence label: multi-source for spot facts; community-observed for the
  narrow wind-shelter gate
- Sources: S5–S8

### Praia da Cordoama

- Slug: `cordoama`
- Approximate coordinates: `37.110, -8.940`
- Orientation: west/northwest
- Wave type / bottom: exposed beach break
- Exposure class: A
- Supported swell: W to NW
- Supported wind: E/NE offshore
- Tide: mid through higher stages commonly recommended; banks vary
- Sections and skill: open peaks; suitable at smaller, cleaner sizes and more
  demanding as swell increases
- Hazards: rips, rocks at sections/edges, long exposed beach
- Access: public parking and formal descent
- Crowd/localism: generally less concentrated than the principal Sagres-town
  breaks
- Confidence: medium-high
- Evidence label: multi-source
- Sources: S9–S11

### Praia do Castelejo

- Slug: `castelejo`
- Approximate coordinates: `37.101, -8.947`
- Orientation: west/northwest
- Wave type / bottom: exposed beach break
- Exposure class: A
- Supported swell: W to NW
- Supported wind: E/NE offshore
- Tide: broad mid-tide starting point; shifting sandbanks limit precision
- Sections and skill: multiple peaks; approachable when small, powerful and
  rippy when larger
- Hazards: rips, shorebreak, rocks near edges
- Access: established public parking and stair/path access
- Crowd/localism: moderate and dispersed across peaks
- Confidence: medium-high
- Evidence label: multi-source
- Sources: S12–S14

### Praia do Tonel

- Slug: `tonel`
- Approximate coordinates: `37.007, -8.953`
- Orientation: west/northwest
- Wave type / bottom: exposed beach break with rock influence
- Exposure class: A
- Supported swell: W to NW
- Supported wind: E/NE offshore; cliff effects vary by direction and strength
- Tide: broad mid-tide preference; rock exposure changes with tide
- Sections and skill: beach peaks can suit developing surfers when small;
  becomes powerful and demanding with swell
- Hazards: rocks, rips, strong shorebreak, rapid step-up in power
- Access: established town beach access
- Crowd/localism: frequently busy because of location and consistency
- Confidence: high for offshore-grid size as a regional anchor; medium for
  section quality
- Evidence label: multi-source plus community-observed calibration
- Sources: S15–S18

### Praia do Beliche

- Slug: `beliche`
- Approximate coordinates: `37.025, -8.965`
- Orientation: southwest-facing bay near Cape St Vincent
- Wave type / bottom: beach break with rock/cliff influence
- Exposure class: C — strongly direction- and period-sensitive cape shadow
- Supported swell: deep-W energy reaches it more directly; NW requires enough
  size and period to wrap
- Supported wind: N/NE commonly described as favourable/sheltered
- Tide: broad low-to-mid preference; water reaches cliff base as tide rises
- Sections and skill: clean smaller days can be approachable; larger days
  become hollow, rippy, and more technical
- Hazards: cliff/rockfall exposure, rocks, strong currents, rising-water access
- Access: long formal staircase
- Crowd/localism: limited takeoff space can concentrate crowds; reports on
  localism vary
- Confidence: high that raw tip-cell size must not be quoted directly; medium
  on any exact size translation
- Evidence label: multi-source plus community-observed calibration
- Sources: S19–S23

### Praia do Zavial

- Slug: `zavial`
- Approximate coordinates: `37.050, -8.860`
- Orientation: south-facing bay with west-side right point
- Wave type / bottom: right point/reef plus beach peaks
- Exposure class: C — south swell and long-period W/WNW wrap behave differently
- Supported swell: S/SW; long-period W/WNW can wrap into the point
- Supported wind: N/NW offshore
- Tide: broad low-to-mid preference; low water can make it hollow and shallow
- Sections and skill: beach peaks can suit developing surfers when small; the
  point is faster, shallower, more localised, and more advanced
- Hazards: rocks/reef, closeouts, currents, shallow point section
- Access: established road, parking, and short public path
- Crowd/localism: protective local crew is repeatedly reported at the main
  point; use public beach peaks and normal etiquette
- Confidence: high for section/hazard distinction; medium for wrap size
- Evidence label: multi-source plus community-observed calibration
- Sources: S24–S27

## Important limitations

- Sandbanks, access, and crowd patterns change.
- The model-cell coordinates are forecast sampling points, not secret-spot pins.
- Exact face-height multipliers remain provisional because current public
  calibration comes from one independent contributor.
- Use `calibration.md` and a live nearshore/visual check before a class B/C call.
