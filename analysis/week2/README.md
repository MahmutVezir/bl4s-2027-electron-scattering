# Week 2 analysis

The canonical event-level analysis is currently produced by the target-boundary recovery notebook.

Expected analysis products:

- Per-condition event-level table with `event_id`, `theta_target_mrad`, entry/exit kinetic energy and `energy_loss_MeV`.
- Descriptive statistics for angle and energy loss, with sample counts and uncertainty intervals.
- Independent-sample air-versus-aluminium comparison (Welch mean comparison and distributional comparison as appropriate).
- Outlier candidate ranking for aluminium angle and energy loss.
- Trace exports for selected events, including boundary records, hits and primary-electron step records.

## Rules

- Read the verified ROOT file; do not alter the raw ROOT/CSV source files.
- Use the measurement definitions in `docs/week2/README.md`.
- Treat air and aluminium as independent samples. Do not use paired tests based on matching event IDs.
- Report p-values with adequate precision; do not print underflow as a literal probability of zero.
- Keep mean, median, spread, confidence interval and tail quantiles distinct.
- Do not remove or winsorize outliers by default.
- Every published table and figure must identify its source archive/hash and analysis-code revision.

No summary table is included yet because the latest regenerated output manifest and trace-audit files have not been reviewed into this repository.
