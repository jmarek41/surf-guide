# Promoting private observations into shared calibration

This workflow lets session evidence improve forecasts for everyone without
publishing the surfer's raw log or identity.

## The three layers

1. **Raw evidence — private**
   - `data/sessions/<region>.csv`
   - `data/sessions/<region>.md`
   - rider, board, exact time, base, personal verdict, and narrative
2. **Candidate lesson — private**
   - `data/calibration/<region>.md`
   - stable candidate ID, evidence references, counts, counterexamples, and a
     proposed anonymous rule
3. **Shared calibration — public**
   - `locations/<country>/<region>/calibration.md`
   - only the approved generalized behaviour and aggregate evidence

Never skip directly from a raw session to a public file.

## 1. Decide whether the lesson is reusable

Good public candidates describe a repeatable model or spot mechanic, for
example:

- a cliff shelters a named public section from a narrow wind direction;
- a cape shadows NW swell but admits longer-period W swell;
- one forecast cell systematically overstates a sheltered bay;
- a wind source is biased in a defined time/season bucket.

Keep these private:

- personal dislike, fear, fatigue, performance, or board fit;
- exact session time, base, travel pattern, seller, booking, or conversation;
- one-off wildlife, debris, crowd, or water-quality incidents unless a public
  authority documents an ongoing hazard;
- secret or unpublished breaks.

Public safety facts from authorities belong in the spot pack with their direct
source, not as anonymous empirical calibration.

## 2. Maintain the private candidate

Use the `Candidate public lessons` table from
`templates/personal-calibration.md`.

- Give the rule a stable ID such as `sagres-beliche-cape-shadow`.
- Bucket swell direction, period, wind regime, tide stage, and time of day only
  as narrowly as the evidence supports.
- Count observations and counterexamples.
- Count people, not sessions, under independent contributors. Ten observations
  by one surfer remain one independent contributor.
- Link the candidate to private evidence references, but never copy those
  references into the public proposal.

Do not promote an exact multiplier or threshold from a single observation.
Useful low-confidence geometry can still be proposed when labelled honestly.

## 3. Draft the public rule

Draft one row or short section matching
`locations/_template/calibration.md`. Include:

- public spot or source;
- condition bucket;
- generalized behaviour;
- observation count;
- independent-contributor count;
- counterexamples;
- `community-observed`, `inference`, `single-source`, or `multi-source`;
- confidence.

Public research may corroborate geometry, but it does not turn repeated
sessions from one surfer into multiple independent contributors. State combined
evidence such as `multi-source geometry + community-observed` when appropriate.

## 4. Approval gate

Show the exact proposed public text and target file to the user. Do not edit
`locations/`, create a branch, open an issue, or prepare a pull request until
the user explicitly approves the public contribution.

Approval covers only the displayed anonymous rule. It does not authorize
publishing raw evidence or unrelated candidates.

## 5. Publish and preserve provenance

After approval:

1. Add or update the public calibration entry.
2. Update public source links when research supports the rule.
3. Run `./scripts/validate.sh`.
4. Mark the private candidate `promoted` and record the public target.
5. Keep private evidence and counterexamples; publication is not deletion.

Future reports should update counts and counterexamples through the same gate.
Conflicting observations lower confidence; they must not be silently discarded.
