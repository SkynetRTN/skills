#!/usr/bin/env python3
"""Score an agent's labels against an answer key.

Usage:
  python3 score.py KEY.csv RESULTS.csv [RESULTS.csv ...]

KEY columns: test_id, file_id, required, optional, why.
  required: '|' separates slots that must all be present; '/' separates
            acceptable alternatives within one slot.
  optional: labels that may also appear without penalty.
RESULTS: the skill's Output format; the `image` column holds <test_id>.jpg.

A frame is correct when every required slot is met and no label outside
required + optional was given.
"""

import csv
import sys

key = list(csv.DictReader(open(sys.argv[1])))
got = {}
for path in sys.argv[2:]:
    for r in csv.DictReader(open(path)):
        tid = (r.get("image") or r.get("test_id", "")).strip().removesuffix(".jpg")
        got[tid] = {l.strip() for l in r["labels"].split("|") if l.strip()}

correct = 0
for k in key:
    slots = [set(s.split("/")) for s in k["required"].split("|")]
    allowed = set().union(*slots) | {l for l in k["optional"].split("|") if l}
    labels = got.get(k["test_id"], set())
    missing = ["/".join(sorted(s)) for s in slots if not s & labels]
    extra = sorted(labels - allowed)
    ok = not missing and not extra
    correct += ok
    detail = "" if ok else f"  missing={missing} extra={extra}"
    print(f"{k['test_id']} {'ok  ' if ok else 'FAIL'} {'|'.join(sorted(labels))}{detail}")
print(f"correct {correct}/{len(key)}")
