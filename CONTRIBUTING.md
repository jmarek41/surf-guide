# Contributing

Thank you for helping improve surf-guide.

## Before opening a pull request

1. Run `git status`.
2. Confirm that no file under `data/` is staged or tracked.
3. Run `./scripts/validate.sh`.
4. Remove names, exact accommodation details, raw session rows, shop/seller
   conversations, rental bookings, and other personal data.
5. Explain which statements are sourced, inferred, or observed.

## Adding a location or spot

Copy `locations/_template/` to:

```text
locations/<country-slug>/<region-slug>/
```

Use lowercase ASCII slugs with hyphens. Public location packs should contain:

- established public spot names and approximate coordinates;
- orientation and exposure;
- supported swell, wind, and tide guidance;
- hazards, access, crowd, and localism notes;
- section-level skill differences;
- source URLs and a confidence label;
- only anonymized calibration summaries.

### Evidence labels

- `multi-source` — at least two independent public sources agree.
- `single-source` — one public source; useful but not corroborated.
- `community-observed` — anonymized first-hand report, with the number of
  independent contributors stated.
- `inference` — geometry or model interpretation, explicitly labelled.
- `unknown` — leave the field blank rather than guess.

Multiple sessions from the same surfer are valuable calibration but remain one
independent contributor. Do not relabel them as multi-source.

### Sensitive breaks

Do not add secret, unpublished, culturally sensitive, or access-sensitive
breaks. A spot should already be publicly documented by established surf or
government sources. Maintainers may remove coordinates or reject a contribution
where publication could cause harm.

## Promoting a session lesson

Raw sessions remain under `data/`. Follow
`method/calibration-promotion.md` when a repeatable pattern may help everyone:

1. Keep raw evidence and its references in private data.
2. Maintain a private candidate with a stable ID and status.
3. Draft the exact anonymous public rule and target file.
4. Obtain explicit user approval for that text.
5. Add the approved rule to the relevant public `calibration.md`.

Never automate this promotion or include the raw CSV in a PR.

## Method changes

Forecast and board-selection changes should explain:

- the problem or failure mode;
- evidence or authoritative documentation;
- behaviour before and after;
- destinations or rider types for which the rule may not apply.

## Short-trip catalog changes

The public scan catalog may contain established destinations, approximate
forecast cells, gateway airports, and public provider identifiers. Verify
changes against two independent sources where possible. Never contribute
personal origins, budgets, bookings, fare history, or API keys.

## Pull-request scope

Prefer one location pack or one methodological change per pull request. Small,
reviewable contributions are easier to verify and merge.
