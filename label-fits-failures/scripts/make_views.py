#!/usr/bin/env python3
"""Make inspection views of one telescope image for visual labelling.

Writes, into OUT_DIR:
  <stem>_overview.jpg  the whole frame, downscaled to fit 1200 px
  <stem>_stretch.jpg   the same view, histogram-equalised, so faint
                       gradients, dust rings, smear lines and dark edges show
  <stem>_tiles.jpg     a 3x3 grid of native-resolution crops (corners, edge
                       middles, centre) so star shapes can be judged
  <stem>_zoom.jpg      only with --zoom: one native-resolution crop

It only rearranges pixels for viewing. It prints file paths, never
measurements: the label comes from looking at the views.

Usage:
  python3 make_views.py IMAGE OUT_DIR
  python3 make_views.py IMAGE OUT_DIR --zoom 0.8,0.1        # x,y as fractions
  python3 make_views.py IMAGE OUT_DIR --zoom 0.8,0.1,900    # crop size in px

Needs Python 3 and Pillow (pip install pillow).
"""

import argparse
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageOps

OVERVIEW_PX = 1200  # long side of the whole-frame views
TILE_PX = 480       # native-resolution crop size; 3 tiles + gaps fit ~1450 px
GAP_PX = 6
TILE_NAMES = [["top-left", "top", "top-right"],
              ["left", "centre", "right"],
              ["bottom-left", "bottom", "bottom-right"]]


def overview(img):
    view = img.copy()
    view.thumbnail((OVERVIEW_PX, OVERVIEW_PX), Image.LANCZOS)
    return view


def stretch(view):
    return ImageOps.equalize(view.convert("L"))


def tiles(img):
    w, h = img.size
    t = min(TILE_PX, w // 3, h // 3)
    xs = [0, (w - t) // 2, w - t]
    ys = [0, (h - t) // 2, h - t]
    sheet = Image.new("RGB", (3 * t + 2 * GAP_PX, 3 * t + 2 * GAP_PX), "red")
    draw = ImageDraw.Draw(sheet)
    for r, y in enumerate(ys):
        for c, x in enumerate(xs):
            px, py = c * (t + GAP_PX), r * (t + GAP_PX)
            sheet.paste(img.crop((x, y, x + t, y + t)).convert("RGB"), (px, py))
            # Label on a black box so it never hides as a fake star or trail.
            label = TILE_NAMES[r][c]
            draw.rectangle((px, py, px + 7 * len(label) + 6, py + 14), fill="black")
            draw.text((px + 3, py + 2), label, fill="yellow")
    return sheet


def zoom(img, spec):
    parts = [float(p) for p in spec.split(",")]
    if len(parts) not in (2, 3) or not all(0 <= p <= 1 for p in parts[:2]):
        sys.exit("--zoom takes X,Y or X,Y,SIZE with X and Y between 0 and 1")
    w, h = img.size
    size = int(parts[2]) if len(parts) == 3 else 600
    size = min(size, w, h)
    cx, cy = int(parts[0] * w), int(parts[1] * h)
    x = min(max(cx - size // 2, 0), w - size)
    y = min(max(cy - size // 2, 0), h - size)
    return img.crop((x, y, x + size, y + size))


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("image")
    ap.add_argument("out_dir")
    ap.add_argument("--zoom", help="X,Y[,SIZE]: native crop centred at fractional X,Y")
    args = ap.parse_args()

    img = Image.open(args.image)
    img.load()
    if img.mode not in ("L", "RGB"):
        img = img.convert("RGB")
    out = Path(args.out_dir)
    out.mkdir(parents=True, exist_ok=True)
    stem = Path(args.image).stem

    view = overview(img)
    written = {
        "overview": view,
        "stretch": stretch(view),
        "tiles": tiles(img),
    }
    if args.zoom:
        written["zoom"] = zoom(img, args.zoom)
    for name, pic in written.items():
        path = out / f"{stem}_{name}.jpg"
        pic.save(path, quality=92)
        print(path)
    print(f"frame size: {img.size[0]} x {img.size[1]} px")


if __name__ == "__main__":
    main()
