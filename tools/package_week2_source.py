"""Create a source-only ZIP for offline transfer of the Week 2 demonstrator.

This does not include the Geant4 installation or Geant4 datasets. Those must be
exported separately for a fully air-gapped machine.
"""
from __future__ import annotations

import hashlib
import json
import zipfile
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "results" / "week2_source_bundle.zip"
INCLUDE = [
    Path("simulation/geant4/week2"),
    Path("notebooks/colab/mahmut_week2_sensitive_tracker.ipynb"),
    Path("docs/week2_geant4_demonstrator.md"),
    Path("requirements-week2-analysis.txt"),
]

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
manifest: list[dict[str, object]] = []

with zipfile.ZipFile(OUTPUT, "w", compression=zipfile.ZIP_DEFLATED) as archive:
    for relative in INCLUDE:
        source = ROOT / relative
        if not source.exists():
            continue
        paths = [source] if source.is_file() else sorted(p for p in source.rglob("*") if p.is_file())
        for path in paths:
            archive_name = path.relative_to(ROOT).as_posix()
            data = path.read_bytes()
            archive.writestr(archive_name, data)
            manifest.append({
                "path": archive_name,
                "size_bytes": len(data),
                "sha256": hashlib.sha256(data).hexdigest(),
            })

    archive.writestr(
        "SOURCE_BUNDLE_MANIFEST.json",
        json.dumps({
            "created_utc": datetime.now(timezone.utc).isoformat(),
            "note": "Source-only bundle; Geant4 binaries and datasets are not included.",
            "files": manifest,
        }, indent=2),
    )

print(f"Created: {OUTPUT}")
print(f"Files: {len(manifest)}")
print(f"SHA-256: {hashlib.sha256(OUTPUT.read_bytes()).hexdigest()}")
