#!/usr/bin/env python3
from pathlib import Path
import json
root=Path(__file__).resolve().parents[1]
manifest=json.loads((root/'data/archive.json.parts/manifest.json').read_text())
out=root/manifest['original_path']
out.parent.mkdir(parents=True, exist_ok=True)
with out.open('wb') as dst:
    for p in manifest['parts']:
        dst.write((root/p['path']).read_bytes())
print(f'reconstructed {out} ({out.stat().st_size} bytes)')
