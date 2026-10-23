---
name: label-fits-failures
description: Use when labeling, triaging or quality-checking a telescope observation image (a JPEG or PNG preview of a CCD frame) to say why it is poor - clouds, trailed, streaked or donut-shaped stars, an off-centre target, a stuck shutter, moonlight or stray light, satellite or airplane trails, a bug on the camera window, over-exposure - or when deciding whether an observation must be re-observed.
---

# Label FITS Failures

## Overview

Label what you **see**, by comparing the image with the reference images in
`examples/`. The labels, their causes and the reference images come from the
Skynet Astro 101 lab units, mainly Lab 1 section A.2, "How to Check Your
Images" (see Sources). The units' rule is the purpose of the label: "If any of
your images are of poor quality for any reason, re-observe them!"

**Decide by eye.** Tools may only crop, resize, zoom or contrast-stretch the
image so you can see it. Do not compute anything from the pixels: no
percentiles, histograms, pixel values, brightness ratios, correlations between
images, star counts, widths or ellipticities. Do not use metadata, file names
or anyone else's labels. If your evidence contains a measured number, you
measured instead of looked: delete it and describe what you saw. Paths below
are relative to this skill's directory.

## Labels

| Label | Cause, in the unit's words | What you see | Reference |
|---|---|---|---|
| `clouds_total` | clouds blocking all of the light | **No stars at all.** Only the camera's own pattern remains: a smooth glow (often brighter middle, darker corners), soft bands or stripes, faint rings ("donuts") and specks from out-of-focus dust on the camera window. Dust donuts and darker corners prove light reached the camera, so this is cloud, not a closed shutter. | `clouds_total_a.png`, `clouds_total_b.png` |
| `clouds_partial` | clouds blocking some of the light | Stars visible but **fainter or missing where the background is lifted**; background grainy and **uneven or blotchy**; dust donuts may show; low contrast. | `clouds_partial.png` next to `nominal_same_field_clear.png` (same field, clear) |
| `wind_or_mount_shake` | wind or mount misbehavior distorting or streaking the images | **Every** star has the same distorted shape: a **short** dash, oval, doubled dot, loop, bright head with a tail, or zig-zag, a few star-widths long. Uniform short dashes belong here too: compare the length with the two references. | `wind_or_mount_shake.png` |
| `not_tracking` | the mount not tracking Earth's rotation | **Every** star is a **long** thin trail, clearly a line rather than a dash (more than about ten star-widths, often a large part of the frame); trails parallel and equal; galaxies and nebulae smeared the same way. Near the celestial pole the trails curve into concentric arcs around one point. | `not_tracking.png` |
| `off_center` | mount misbehavior off-centering the images | The obvious target (planet, Moon, bright galaxy or nebula, very bright star) sits **at, or is cut off by, an edge or corner**, and the middle is empty. A target that is merely below or beside centre but well inside the frame is not off-centre. | `off_center.png` |
| `out_of_focus` | focus misbehavior | Stars are not points: **rings or donuts with a dark centre**, crescents, "C", horseshoe or heart shapes, all alike; bigger for brighter stars. Not stretched in one direction. | `out_of_focus.png` |
| `shutter_stuck` | the camera shutter sticking | Any of three looks: **(a)** a thin straight line through a bright star, exactly along the pixel columns (or rows), **running the full height (or width) of the frame**; **(b)** a thick bright bar from a frame edge ending at a bright object, often on a striped background; **(c)** shutter partly open: dark lobes or a dark crescent with **sharp curved edges** cutting in from the corners or edges, against ordinary sky (no bright glow behind them), so the lit area has a curved, non-circular outline. The edge is sharp enough to trace with a pen; a soft darkening along an edge is vignetting, not this. | `shutter_stuck_a_smear_line.png`, `..._b_smear_bar.png`, `..._c_partly_open.png` |
| `stray_light` | proximity to the moon or someone leaving a light on at the telescope | Large bright fans, wedges, arcs or glows, often **coming in from an edge or corner**, much brighter than the sky, sometimes with dark silhouettes of telescope parts against them. Light is **added**: put a tile from a bright part next to one from a dark part, and faint stars still show in both. If stars are too sparse to compare, decide by shape: a glow **entering from an edge or corner** is this; blotches spread across the frame are `clouds_partial`. The Moon's limb cutting into a corner of a frame that has stars counts. | `stray_light.png` |
| `satellite_trail` | a satellite moving through that part of the sky during the exposure | **One** thin straight line of even brightness, at any angle, usually edge to edge but it may start or stop inside the frame; the stars stay round. | `satellite_trail.png` |
| `airplane_trail` | an airplane moving through that part of the sky during the exposure | **Two or more parallel** straight lines (the gap between them stays the same along their whole length), often with bright flashes, blobs or dashes along them. Lines whose gap widens are separate satellites. | `airplane_trail.png` |
| `obstruction` | a bug sitting on the camera window | A large **dark** (below the sky) irregular silhouette with soft edges and protrusions, hiding the stars behind it; the rest of the frame is normal. | `obstruction.png` |
| `overexposed` | exposing too long: "you may over-expose the bright parts of your images" | A bright object (usually the planet or target) is a flat white blob with **a bright tongue or jagged streak running out of it along the columns**, as circled in the reference; its detail is gone. A plain round white disc without a tongue is not this (see Not failures). | `overexposed.png` |
| `nominal` | — | Round, sharp stars in the middle **and** the corners, a fairly even background, the target in frame, no lines or blobs. Use only when no other label applies. | `nominal_same_field_clear.png` |
| `other_defect` | "poor quality for any reason" | The frame is clearly poor, but none of the looks above matches. Describe what you see. | — |
| `uncertain` | — | Two or more readings fit and you cannot choose. Name them in the evidence. | — |

## Not failures

These come from the same units. They look unusual but are normal: label them
`nominal` unless a bullet below says otherwise.

- **Planet frames.** Short planet exposures show the planet and perhaps its
  moons on black; no stars is expected, not cloud. A zoomed planet looks blocky and soft
  (the atmosphere blurs by about 1 arcsecond); its phase (crescent, gibbous) is
  real. See `nominal_planet_zoomed.png`.
- **A planet washed out on purpose** to bring out its moons: a plain round
  white disc with moon dots around it and no tongue along the columns
  (`nominal_planet_washed_out_for_moons.png`). Label it `nominal`.
- **Moon frames.** First ask: does the rest of the frame show stars or a
  deep-sky object (stretch view)? If yes, the Moon is an intruder:
  `stray_light`. If no, the Moon was the target: lunar surface, with or
  without the limb against black sky, is `nominal`, even when it fills only a
  third of the frame (framing the limb is normal); only a thin sliver at an
  edge is `off_center`, and say in the evidence that the black part may be the
  Moon in darkness (the unit's own caveat).
- **Occulting ("special") filter.** A large round black disc centred on a
  bright object, the object visible inside, spikes outside
  (`nominal_occulting_filter.png`). A bug is irregular and off-centre; this is
  round and centred.
- **Diffraction spikes:** a cross of four straight spikes on bright stars.
- **A short bleed spike** on a bright star (a stub along the columns that stops
  near the star) is ordinary saturation, not a failure. Only a line that runs
  the full frame is the shutter look.
- **Display stretch.** The same frame can look dark ("Default") or grainy with
  a bright background ("Faint Target"), and the brighter preset saturates the
  inner nebula; see `nominal_stretch_presets.png`. A uniformly grainy background
  is not cloud; cloud is uneven or blotchy. A white core in a galaxy, cluster or
  nebula is the display stretch, not `overexposed`.
- **Galaxies are elongated.** Judge shapes from point-like stars only.
- **Smooth, circular darkening toward the corners** (as in
  `airplane_trail.png`) is the optics, not a stuck shutter: the shutter look has
  sharp curved edges and lobes.

## Procedure

Do this for every image. Write down what you see before you choose a label.

1. **Look at the references once per session.** Open
   `examples/atlas_failures.jpg` and `examples/atlas_not_failures.jpg` and look
   at every panel.
2. **Make the views.**
   `python3 scripts/make_views.py IMAGE OUT_DIR` writes three files (needs
   Pillow; without it, see Fallback):
   - `*_overview.jpg`: the whole frame, downscaled;
   - `*_stretch.jpg`: the same view with a hard contrast stretch, which shows
     gradients, dust donuts, faint lines and dark edges;
   - `*_tiles.jpg`: native-resolution crops of the corners, edges and centre.
     **Star shapes can only be judged here.** The overview hides elongation and
     donuts.

   Add `--zoom X,Y` (fractions from top left) for a native crop of any
   suspicious spot, such as the end of a line or a dark patch.
3. **Name the frame type:** star or deep-sky field; planet or Moon;
   background only.
4. **Whole frame** (overview and stretch). Are there stars at all? Glows
   entering from an edge? Dark lobes with curved edges? A dark irregular
   silhouette? Is the target at an edge? Is the background blotchy?
5. **Lines.** First ask: **are there round stars besides the lines?** If
   almost every star is itself a line or dash, the lines are the stars: this
   is the mount, so go to step 6, even when the lines cross or curve. Only when
   round stars remain:
   - one thin line, or several lines at **different** angles or with a gap
     that widens → `satellite_trail` (one satellite per line);
   - two or more **parallel** lines (constant gap), often with flashes or
     blobs → `airplane_trail`;
   - a line through a bright star, exactly vertical or horizontal, running the
     full frame, or a thick bar from an edge to a bright object →
     `shutter_stuck`. A short spike that stops near a bright star is ordinary
     saturation, not a failure.
6. **Star shapes** (tiles). Look at several stars in the centre and in each
   corner, then hold them next to `wind_or_mount_shake.png` and
   `not_tracking.png`:
   - round points → no shape failure;
   - short dashes, ovals, doubles or a bright head with a tail, a few
     star-widths long → `wind_or_mount_shake`;
   - long parallel lines (more than about ten star-widths) or concentric arcs
     → `not_tracking`;
   - every star a line, but lines crossing or of different shapes → the mount
     moved erratically: `wind_or_mount_shake` at `medium` confidence (never
     satellites);
   - between the two references (longer than the wind dashes, shorter than
     the tracking lines) → `wind_or_mount_shake` at `medium`;
   - rings, donuts, crescents → `out_of_focus`.
7. **Bright objects.** A flat white blob with a tongue along the columns →
   `overexposed`. A plain white disc or galaxy core → no label.
8. **Compare.** For each candidate label, open its reference image and the
   not-failure atlas. Keep the label only if your image shows the same look.
9. **Record** every label that applies (a frame can be cloudy *and* trailed).
   Use `nominal` only when nothing else applies.

## Output

One record per image:

```csv
image,labels,confidence,reobserve,evidence
frame_0412.jpg,clouds_partial|satellite_trail,high,yes,"blotchy background, dark patches upper right and lower left with stars dimmed; one thin line top-left to bottom-right; stars round in all tiles"
```

- `labels`: one or more labels from the table, separated by `|`.
- `confidence`: `high` (the look is unmistakable and matches the reference),
  `medium` (it matches but is faint, partial or between two references) or
  `low` (one reading of several: consider `uncertain`). With several labels,
  give the confidence of the least certain one.
- `reobserve`: `no` for `nominal`; `yes` for everything else, including
  `uncertain` (the units' rule: re-observe if poor "for any reason").
- `evidence`: what you saw and where. It must describe the image, not repeat
  the label definition.

## Common mistakes

Agents labelling real frames without this skill made these errors.

| Mistake | Correction |
|---|---|
| A thin column line through a bright star, running the whole frame, labelled `overexposed` ("charge bleed") | Full-frame line = `shutter_stuck` look (a). Bleed is a short stub. |
| Dozens of crossing lines, almost no round stars, labelled `satellite_trail` | When the stars themselves are lines, the mount moved. Satellites leave the stars round. |
| Short, even dashes on every star labelled `not_tracking` | Compare lengths with the references: short dashes = `wind_or_mount_shake`; `not_tracking` is long lines. |
| A planet a little below centre labelled `off_center` | Only a target at or cut off by an edge is off-centre. |
| A galaxy's white core labelled `overexposed` | Display stretch. `overexposed` needs the tongue along the columns. |
| A soft dark strip along one edge, seen in a shrunken view, labelled `shutter_stuck` | Check at full size. Vignetting is soft; the shutter edge is sharp and curved. |
| Evidence such as "99th percentile 162", "correlation 0.80", "values 1-2" | Measuring is not looking. Describe the shapes, positions and textures you saw. |
| A star-less frame called a possible closed shutter | Dust donuts or darker corners mean light arrived: `clouds_total`. |
| A blotchy background called `clouds_partial` although stars are just as dense in the bright patches | Added light with stars intact is `stray_light`; cloud dims or hides stars. If unsure, `uncertain` naming both. |

## Fallback without Python

With ImageMagick (`magick`, or `convert` on older versions):

```bash
magick IMG -resize 1200x1200 overview.jpg
magick IMG -resize 1200x1200 -colorspace gray -equalize stretch.jpg
magick IMG -gravity center    -crop 480x480+0+0 +repage tile_centre.jpg
magick IMG -gravity northwest -crop 480x480+0+0 +repage tile_top_left.jpg
# repeat with northeast, southwest, southeast for the other corners
```

With neither tool, open the image in any viewer and zoom to 100% on the
centre and each corner before judging star shapes.

## Sources

Skynet Robotic Telescope Network, UNC Astro 101 lab units (WebAssign, 2020;
author Dan Reichart). The PDFs are kept outside this skill.

- Lab 1, "Introduction to Skynet", A.2 "How to Check Your Images" (pp. 7–11):
  every failure label and its reference image. A.8 (p. 16): over-exposure and
  `overexposed.png`. A.4 and B.4 (pp. 13, 20–21): planets washed out to show
  moons, and thin cloud hiding moons. B.1 (p. 17): zoomed planet and
  atmospheric blurring. B.6 (p. 23): display stretch presets.
- Lab 4, "Distance Ladder I: Parallax", C–D (pp. 14–15): the special filter
  that darkens the centre around Venus and Alpha Centauri.
- Labs 2, 3 and 5–8 hold no further failure modes.

`tests/` holds answer keys and a scorer for people re-validating this skill
after an edit. Labelling does not need it.
