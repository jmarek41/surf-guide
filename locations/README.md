# Shared location packs

Location packs contain public surf knowledge that can be reused by every rider.
Personal fit is applied later from `data/profile.md`.

## Layout

```text
locations/<country>/<region>/
├── README.md       # coverage, timezone, grid cells, and spot facts
├── calibration.md  # generalized model/spot behaviour with evidence labels
└── sources.md      # direct source URLs and notes
```

Copy `locations/_template/` when adding a region.

## Shared versus private

Shared:

- public spot name and approximate coordinates;
- orientation, wave type, bottom, and sections;
- swell, wind, and tide guidance;
- hazards, access, crowd, and documented localism;
- model grid cells and exposure class;
- anonymized calibration with observation and contributor counts;
- public source links.

Private:

- rider ability, weight, boards, preferences, and hard exclusions;
- exact accommodation or home;
- raw sessions and personal narrative;
- seller details, purchases, and board shortlists;
- private or unpublished breaks.

Drive time is calculated from the private base at runtime. It should not be
hard-coded into a shared pack.
