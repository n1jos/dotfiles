#!/usr/bin/env python3

import csv, json, sys
from pathlib import Path

folder = Path.cwd()
csvs = list(folder.glob("*.csv"))

if not csvs:
    print("No CSV files found in current folder.")
    sys.exit(0)

for src in csvs:
    dst = src.with_suffix(".json")
    try:
        with open(src) as f:
            data = list(csv.DictReader(f))
        with open(dst, 'w') as f:
            json.dump(data, f, indent=2)
        print(f"✓ {src.name} → {dst.name}")
    except Exception as e:
        print(f"✗ {src.name} failed: {e}")