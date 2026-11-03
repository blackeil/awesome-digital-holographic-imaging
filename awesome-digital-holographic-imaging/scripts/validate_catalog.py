#!/usr/bin/env python3
"""Validate schema, IDs, URLs, and resource pages. Uses standard library only."""
from pathlib import Path
import csv, re, sys
ROOT=Path(__file__).resolve().parents[1]
CSV=ROOT/'data/resources.csv'
with CSV.open(encoding='utf-8-sig',newline='') as file:
    rows=list(csv.DictReader(file))
assert rows, 'empty resource catalog'
ids=[r['id'] for r in rows]
assert len(ids)==len(set(ids)), 'duplicate IDs'
for r in rows:
    assert r['category'] in {'reviews','software','hardware','datasets','learning'}, r
    assert re.match(r'https://[^ ]+$',r['url']), (r['id'],r['url'])
    assert r['priority'] in {'core','related'},r
    assert r['last_checked'], r
    assert r['description_zh'],r
    assert (ROOT/'resources'/f"{r['category']}.md").is_file(),r
print(f'PASS: {len(rows)} curated resources, no duplicate IDs, valid scheme and required fields.')
