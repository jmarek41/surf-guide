# Surf Guide for AI Agents

`surf-guide` gives an AI coding agent a personal surf forecaster and board
recommendation workflow.

The repository deliberately separates two kinds of knowledge:

- **Shared knowledge:** forecast methodology, sourced spot facts, hazards, access,
  exposure, and anonymized calibration that can help every surfer.
- **Private knowledge:** rider profile, exact base, board history,
  recommendations, raw session logs, and personal calibration. These live under
  `data/`, which is ignored by Git.

## What you get

- `/setup-surf` — creates a local rider profile and activates or researches a
  surf region.
- `/surf [when]` — ranks suitable spots and daylight windows using live swell,
  wind, and tide data.
- `/log-session` — records forecast versus reality locally so recommendations
  improve over time.
- `/board-recommend [request or option]` — recommends a board, then evaluates
  matching new, used, or rental options.
- `/scan [window or destination]` — scans configured destinations for
  exceptional short-trip windows and prices flights only for confirmed
  candidates.

The workflows follow the open [Agent Skills](https://agentskills.io/) `SKILL.md`
format. There is no application server, account, database, required API key, or
build step.

## Quick start

1. Use an AI coding agent that can read `AGENTS.md` and Markdown files. Native
   Agent Skills support is helpful but not required.
2. Clone this repository and open it as the agent's workspace:

   ```bash
   git clone https://github.com/jmarek41/surf-guide.git
   cd surf-guide
   ```

3. Ask the agent to run the `setup-surf` skill. Tools with slash-command
   support can use:

   ```text
   /setup-surf
   ```

4. Once setup finishes, ask where to surf or use:

   ```text
   /surf tomorrow
   ```

Your AI tool may ask permission before fetching forecast or research websites.
Review the domain and approve only sources you trust.

`AGENTS.md` is the canonical project instruction file. Portable skills live in
`.agents/skills/`. Tools that do not discover that path automatically can be
directed to the relevant `SKILL.md` file.

## Private data stays private

Setup writes files only under `data/`:

```text
data/
├── profile.md
├── active-location.md
├── sessions/
├── calibration/
├── boards/
├── scan/
└── secrets/
```

The whole directory is ignored except for `data/.gitkeep`. Do not force-add it.
Run `git status` before every contribution.

If you intentionally want to sync private data, use a separate private
repository or encrypted backup. Do not open a PR containing it.

## Shared spot database

Community location packs live under:

```text
locations/<country>/<region>/
```

A location pack contains public, sourced spot facts and generalized forecast
calibration. It must never contain:

- a contributor's home or accommodation address;
- raw session rows, names, phone numbers, or vehicle details;
- private shop/seller messages, rental bookings, or transaction history;
- secret or unpublished breaks;
- claims presented with more confidence than their evidence supports.

See [CONTRIBUTING.md](CONTRIBUTING.md) and the
[location template](locations/_template/README.md).

## Forecast philosophy

- Resolve relative dates explicitly.
- Rank by expected surf quality; annotate skill, hazards, crowd, localism, and
  access instead of silently hiding spots.
- Treat offshore grid swell as input, not guaranteed breaking-wave height.
- Cross-check shadowed, wrapping, reef, and point breaks with a nearshore source.
- Prefer an honest uncertainty label over a false recommendation.
- Ground truth from sessions improves private calibration; only anonymized,
  generalizable lessons belong in public location packs.

The promotion path is deliberately review-gated:

```text
private raw session → private candidate lesson → approved public calibration
```

See [calibration promotion](method/calibration-promotion.md) for evidence,
privacy, contributor-count, and approval rules.

Forecasts can be wrong. Check current conditions, local warnings, lifeguards,
and your own ability before entering the water.

## Board recommendations

The board workflow is profile-driven. It uses weight, ability, successful and
unsuccessful past boards, duck-dive needs, target waves, budget, duration, and
local availability. It does not apply one universal litres-per-kilogram formula
to everyone.

It recommends the board specification first, independently of how the surfer
will obtain it. It can then compare:

- new boards and current shop inventory;
- used boards and their condition;
- rental boards, including duration, swap policy, and damage terms.

It must not contact a shop, seller, owner, or rental operator; reserve; buy; or
rent anything without explicit approval.

## Short-trip scans

`/scan` uses a cheap batched swell pass, then deep-confirms only promising
destinations. Personal origin airports, trip limits, scan history, prices, and
bookings remain under `data/`.

Surf scanning uses keyless public forecast sources. Automated all-carrier
flight pricing is optional and uses each user's own
[SerpAPI](https://serpapi.com/users/sign_up) key:

1. Retrieve the key from the
   [SerpAPI dashboard](https://serpapi.com/manage-api-key).
2. Store `SERPAPI_API_KEY=<value>` in ignored
   `data/secrets/serpapi.env`.
3. Restrict the file to its owner: `chmod 600 data/secrets/serpapi.env`.

Never paste the key into a prompt or commit it. Without a key, `/scan` still
returns surf opportunities and browser-ready Google Flights links.

## Data providers

The default workflow uses Open-Meteo and may use national meteorological
services and public surf-specific sources. Forecast responses must attribute the
providers actually used. See [ATTRIBUTION.md](ATTRIBUTION.md).

## Contributing

Issues and pull requests are welcome. Useful contributions include:

- a new sourced spot or regional location pack;
- a correction to exposure, hazards, access, or forecast behaviour;
- an anonymized calibration lesson supported by observations;
- improvements to the forecast or board-selection methodology;
- sourced scan destinations or improvements to the short-trip workflow;
- fixes to source URLs or provider mechanics.

Please do not contribute raw personal data or expose sensitive breaks.

## License

MIT. Third-party forecast data and linked sources retain their own licenses and
terms.
