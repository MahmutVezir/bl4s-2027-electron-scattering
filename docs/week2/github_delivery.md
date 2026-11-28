# Week 2 — GitHub delivery procedure

## Keep source and evidence separate

- Commit source code, notebooks, analysis methods, documentation and small derived tables to Git.
- Keep raw simulation CSV files, ROOT production files and full trace bundles in the persistent Google Drive production folder during analysis.
- Once validated, publish the immutable ZIP evidence archive as a GitHub Release asset (or another durable archive location) and commit its name, byte size and SHA-256 in the evidence register.
- Commit concise derived summaries and figures only after they have been regenerated from the verified archive.
- Never put credentials, access tokens, personal Drive links or temporary Colab paths in the repository.

## Branch and review policy

1. Work on a dedicated Week 2 branch.
2. Keep Week 1 deliverables unchanged.
3. Compare the branch against `main` and inspect the changed-file list.
4. Open a pull request for review.
5. Merge only after the evidence and scientific-method checks pass.

The evidence-structure PR is intentionally not a claim that the production dataset has been validated. It creates the place and the rules for adding that evidence without mixing it with the first assignment.

## Large files

Do not commit large `.root`, raw `.csv`, logs or ZIP archives directly into the normal source history by default. Preserve them in the dated Drive run folder and distribute the validated immutable archive through a Release asset. The manifest and summaries in Git must point to the exact archive hash.
