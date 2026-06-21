#!/usr/bin/env python3

import csv, json, sys

if len(sys.argv) != 3:
    print("Usage: csv_to_json <input.csv> <output.json>")
    sys.exit(1)

with open(sys.argv[1]) as f:
    data = list(csv.DictReader(f))

with open(sys.argv[2], 'w') as f:
    json.dump(data, f, indent=2)