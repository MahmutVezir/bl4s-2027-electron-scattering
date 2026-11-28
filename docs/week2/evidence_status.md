# Week 2 — Evidence register

**Repository state reviewed:** `main` at `6ff9428f27bbb6f4b792d9996f8827a8e26a4117`  
**Evidence-structure branch:** `submission/week2-boundary-evidence-structure-2026-11-28`

This register deliberately separates code preparation, reported execution and evidence that is actually stored in the repository.

| Gate | Status | Evidence required before marking complete |
|---|---|---|
| Geant4 Week 2 source package | Present in repository | Existing source under `simulation/geant4/week2/` |
| Corrected public Week 2 Colab notebook | Present in repository | `notebooks/colab/mahmut_week2_sensitive_tracker.ipynb` |
| Target-boundary recovery workflow | Delivered separately; not yet tracked in this repository | Final executed notebook copy, with code/metadata review |
| 10-event smoke test for both materials | Not independently evidenced in this repository revision | Captured test summary and logs |
| 2,000-event air + 2,000-event aluminium regeneration | Not independently evidenced in this repository revision | Production manifest and per-condition CSV/log file hashes |
| ROOT export and branch-by-branch CSV round-trip | Not independently evidenced in this repository revision | ROOT export manifest and validation summary |
| Stage 6 outlier trace audit | User reported the corrected stage ran without interruption; results have not yet been reviewed here | Outlier report, selected-event trace files and audit hash |
| Final dataset archive | Not yet registered in this repository | ZIP path/name, byte size and SHA-256 |
| Statistical report and figures | Pending evidence review | Derived tables, figures, methods and reproducibility metadata |

## Interpretation

The user reported that the corrected notebook ran without interruption after the Stage 6 fix. That report is useful operational context, but without the generated manifest, logs, ROOT checks and archive hash it is not sufficient to mark the simulation or audit as independently verified.

No numerical result is certified by this evidence-structure change. Previously reported statistics from an earlier temporary Colab session must not be silently attached to a newly regenerated dataset. The earlier raw files were unavailable after the runtime reset; a regeneration is a new production unless file hashes prove identity.

## Required evidence bundle

At minimum, register:

1. Exact source commit SHA and Geant4 version.
2. Primary particle, momentum, geometry, material, physics list, event counts and random seeds for each condition.
3. Smoke-test and production logs, including missed-target event accounting.
4. CSV file inventory, row counts and SHA-256 hashes.
5. ROOT file hash, TTree names/entry counts and branch-by-branch CSV round-trip result.
6. Stage 6 outlier candidate list, event trace exports and audit report.
7. ZIP archive byte size and SHA-256.

Update this file only from actual generated evidence. Do not infer a passed gate from the existence of a notebook or source code.
