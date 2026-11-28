# Week 2 — Target-boundary Geant4 production and analysis

## Purpose

Week 2 extends the Geant4 training demonstrator to record the primary electron at the actual aluminium/air target boundaries. It compares an air-control condition with an aluminium-target condition using the same nominal geometry and beam setup.

This remains a software and simulation exercise. The virtual six-plane tracker and the model settings are not claims about the detector configuration or approved beam parameters at CERN CLEAR.

## Current source of truth

- Geant4 application: `simulation/geant4/week2/`
- Public-repository Week 2 Colab demonstrator: `notebooks/colab/mahmut_week2_sensitive_tracker.ipynb`
- Existing source/build repair: `fix/week2-colab-reliability-2026-11-24`, merged to `main` before this evidence-structure change.
- Boundary-regeneration and trace-audit notebook: the separately delivered Colab recovery notebook. Its final executed copy and output manifest must be added to the repository only after the run evidence is collected and checked.

## Measurement definitions

For each event with both target-boundary records:

- Entry and exit directions are the momentum-direction vectors recorded at the corresponding target-boundary crossing.
- Target angular deflection is

  `theta_target_mrad = acos(clip(u_entry · u_exit, -1, 1)) * 1000`

  where the vectors are unit directions and the angle is in milliradians.
- Target kinetic-energy change is

  `energy_loss_MeV = entry_energy_MeV - exit_energy_MeV`

- Events that do not cross the target remain explicit in the event accounting. They are not silently converted into zero-angle measurements.

The definition uses the recorded boundary state at the post-step point for both entry and exit. Do not substitute a tracker-plane fit for this target-boundary measurement without recording a separate analysis definition.

## Comparison design

Air and aluminium are independent Monte Carlo samples with distinct seed pairs. The analysis is an independent-sample comparison, not a paired-event comparison. Equal event IDs across conditions do not establish matched particle histories.

## Outlier policy

Large angle or energy-loss values are candidates for inspection, not automatic errors. Preserve every event. Inspect the corresponding target-boundary records, tracker hits and primary-electron step records, then document the physical/process explanation. Never delete an event solely because it is extreme.

## Validation gates

A production dataset is publishable only after the run manifest, source revision, software versions, event counts, seeds, CSV/ROOT consistency checks, file hashes and outlier trace audit are available. See [evidence status](evidence_status.md) and [delivery procedure](github_delivery.md).
