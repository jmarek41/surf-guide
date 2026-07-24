# Surf Guide — agent context

This repository provides a community surf knowledge base plus local-only rider
data.

## Privacy boundary

- `data/` is private and gitignored. Rider profiles, exact bases, board history,
  recommendations, raw session logs, and personal calibration belong there.
- `locations/` is public. Only sourced spot facts and anonymized, generalized
  calibration belong there.
- Never move information from `data/` into `locations/` automatically. Propose
  the generalized lesson and ask the user before preparing a public change.
- Never reveal secrets, unpublished breaks, private shop/seller messages,
  rental bookings, exact accommodation addresses, or personally identifying
  session details.

## Quality rules

- For factual spot, board, availability, or forecast claims, prefer two
  independent sources. If that is not available, label the claim
  `single-source` or `unverified`; never fill a field by guessing.
- Distinguish public research, model output, inference, and first-hand
  observation.
- A forecast is advisory. Surface uncertainty, hazards, and source disagreement.
- Do not silently filter good surf because of crowd, localism, danger, distance,
  or skill. Rank surf quality, then clearly annotate those considerations unless
  the rider profile defines a hard exclusion.
- Treat raw session observations as ground truth for that surfer's local
  calibration, not as universal truth.

## Repository map

- `.agents/skills/` — portable Agent Skills workflows.
- `method/` — shared forecasting and board-selection methods.
- `scan/` — public short-trip destination catalog.
- `locations/` — contributed public location packs.
- `templates/` — schemas for local and public data.
- `data/` — ignored local state created by the skills.

Do not commit or push unless the user explicitly requests it.
