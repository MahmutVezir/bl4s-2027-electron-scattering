# Week 2 — GitHub delivery procedure

## Keep source and evidence separate

- Commit source code, notebooks, analysis methods, documentation and small derived tables to Git.
- Keep raw simulation CSV files, ROOT production files and full trace bundles in the persistent Google Drive production folder during analysis.
- Publish the immutable ZIP evidence archive as a GitHub Release asset only after validation; record its exact name, size and SHA-256.
- Commit concise derived summaries and figures only after regenerating them from the verified archive.
- Never commit credentials, access tokens, personal Drive links or temporary Colab paths.

## Branch and review policy

1. Work on the dedicated Week 2 branch.
2. Preserve Week 1 deliverables unchanged.
3. Inspect the branch comparison against main.
4. Keep PR #6 in draft until the actual run evidence has been checked.
5. Merge only after scientific-method and evidence review.

## Large files

Do not commit large ROOT, raw CSV, log or ZIP outputs into normal source history. Keep them in the dated Drive production folder and attach the verified archive to a draft GitHub Release. The receipt and inventory belong in Git; the immutable raw archive belongs in Release assets.

## Colab publication steps

The repository includes tools/publish_week2_evidence.py. After notebook Stage 7 prints the ZIP location, run the following in the same Colab session. Replace the example path with the exact path printed by Stage 7:

```python
from pathlib import Path
import os, subprocess, sys
from google.colab import userdata

ARCHIVE_PATH = "/content/drive/MyDrive/CERN_BL4S_2027/Week2_boundary_recovery_YYYYMMDDTHHMMSSZ.zip"
PUBLISHER = Path("/content/week2-evidence-publisher")

if not PUBLISHER.exists():
    subprocess.run([
        "git", "clone", "--depth", "1", "--single-branch",
        "--branch", "submission/week2-boundary-evidence-structure-2026-11-28",
        "https://github.com/MahmutVezir/bl4s-2027-electron-scattering.git",
        str(PUBLISHER)
    ], check=True)

# Create a Colab Secret named GITHUB_TOKEN. Required repository access:
# Contents read/write and Pull requests read. Never print or commit the token.
os.environ["GITHUB_TOKEN"] = userdata.get("GITHUB_TOKEN")

# First run: local ZIP, manifest, CSV, ROOT-hash and trace validation only.
subprocess.run([
    sys.executable, str(PUBLISHER / "tools/publish_week2_evidence.py"),
    "--archive", ARCHIVE_PATH
], check=True)
```

Review the complete output. Continue only when it states WEEK 2 ARCHIVE VALIDATION: PASS and the event counts, seeds, ROOT hash and trace folders are expected. Then run:

```python
subprocess.run([
    sys.executable, str(PUBLISHER / "tools/publish_week2_evidence.py"),
    "--archive", ARCHIVE_PATH,
    "--publish-draft"
], check=True)
```

The second command repeats validation, checks that PR #6 is still open with the expected branches, creates a draft GitHub Release, uploads the ZIP plus SHA-256 and inventory sidecars, and writes a release receipt under results/week2/releases/ on the Week 2 PR branch. It does not merge the PR or write to main. Review the draft Release and receipt before publishing the Release or merging the PR.

The validator intentionally stops if the pinned source, fixed seeds, missed-event IDs, manifest, CSV counts, ROOT hash/tree counts, round-trip declaration or outlier trace package differ. Investigate discrepancies; do not weaken checks just to force an upload.
