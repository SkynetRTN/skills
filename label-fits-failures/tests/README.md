# Re-validating the skill

Run these tests after any edit to `SKILL.md` or the reference images: give
fresh agents the skill and a blind set of frames, then score their labels.

## Frames

The keys name real Skynet frames by `file_id`. They come from the Opticon
pilot set (`SkynetRTN/opticon`, `tools/build-data/out.zip`, Git LFS; extract
with `unzip -q -o out.zip 'out/jpg/*'`). They are other users'
observations, so they are not copied here.

Build a blind set by copying each `out/jpg/<file_id>.jpg` to
`<test_id>.jpg` in an empty folder. The agent must never see the key, the
file IDs or the Opticon labels sheet.

## Agent prompt

> Label telescope observation images for observation failure modes using the
> skill at `<skill dir>/SKILL.md`. Read that SKILL.md first and follow it
> exactly; you may open any file inside the skill directory except `tests/`.
> Images: `<folder>/<first>.jpg` through `<last>.jpg`. Do not open any other
> files. Write your records, in the skill's Output format, to `<out>.csv`.
> When finished, reply with the CSV and one sentence on anything in the skill
> that was unclear.

For a baseline, give the same frames with only the label list and no skill.

## Scoring

```bash
python3 score.py key_set2.csv path/to/results.csv
```

A frame counts as correct when every required label slot is present
(`a/b` means either) and no label outside required + optional appears. Also
read the evidence column: it must describe what was seen and contain no
measured numbers (percentiles, pixel values, ratios, correlations).

## Keys

| Key | Frames | Role |
|---|---|---|
| `key_set1.csv` | 20 | Development set: its baseline errors shaped the Common mistakes table |
| `key_set2.csv` | 10 | Held-out set: never used to write guidance |
| `key_regress.csv` | 13 | Hardest frames from both sets, after the refactor |
| `key_micro.csv` | 7 | Frames touched by the last edits (glow shape, Moon intruder) |

Every key label was checked by eye at native resolution against the unit
references. Some frames are genuinely ambiguous; their keys accept several
readings rather than force one.

## Results (2026-10-23)

| Run | Without skill | With skill |
|---|---|---|
| Set 1, Opus | 16/20 | 20/20 |
| Set 2, Opus | 8/10 | 10/10 |
| Set 2, Sonnet | — | 10/10 |
| Regression, Sonnet (before the last two edits) | — | 12/13 |
| Micro, Sonnet (after the last edits) | — | 7/7 |

Without the skill, every run's evidence contained measured numbers (2 to 5
per ten frames); with it, none did.

Corrections made while testing, all after rechecking at full resolution:

- set 1: t09 is two satellites (the lines are not parallel), not an airplane;
  t01 and t07 also show mount shake; the t15/t19 background repeats across
  two fields from one telescope, so its reading is left open;
- set 2: s07's left edge is soft vignetting, not a shutter lobe (the key
  first said `shutter_stuck`, from a shrunken view); s06, s08 and s09 now
  accept several readings. Against the original set 2 key, the scores were
  baseline 6/10, Opus with skill 7/10 and Sonnet with skill 8/10.
