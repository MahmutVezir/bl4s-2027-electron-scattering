# CERN Beamline for Schools 2027 — GeV Hunters Preparation Workspace

This repository is the shared technical and research workspace for the GeV Hunters team. It stores the team's experiment ideas, feasibility research, software studies, reproducible simulations, analysis notebooks and evidence.

## Current research directions

**Provisional baseline:** measure how thin aluminium foils broaden the downstream transverse position distribution of a low-intensity CLEAR electron beam, using the CERN-listed Timepix3 detector.

**Proposed extension under evaluation — SHADOWPRINT:** test whether pre-defined layered target arrangements with the same total aluminium thickness can be distinguished from downstream electron hit distributions. This remains a hypothesis to test, not a selected or CERN-approved experiment.

Neither direction is a final experiment proposal. Detector geometry, target mounting, beam configuration and event-separation strategy require confirmation from BL4S/CLEAR or the allocated facility.

## Scientific integrity

- No CERN beam time has taken place through this project.
- No real experimental data or measured result is claimed.
- Synthetic data are explicitly labelled and are not beam measurements.
- Analytical scattering estimates are not Geant4 simulations or measurements.
- A single Timepix3 plane measures hit positions and timing; it does not by itself reconstruct an incoming and outgoing track or directly measure a scattering angle.
- The Week 2 six-plane silicon tracker is a virtual training telescope, not a claim that six tracker planes are available at CERN CLEAR.
- All Geant4 beam, target and geometry settings in the training demonstrators must be distinguished from official CLEAR settings.
- The final BL4S proposal must be written and understood by the student team. CERN's 2027 feasibility guidance says not to use AI to write or generate the proposal. This repository supports learning, feasibility checks, reproducible calculations and planning—not a substitute for the team's own scientific reasoning or writing.

## Repository map

### Research and team coordination

- `docs/competition_requirements.md` — BL4S 2027 requirements and boundaries.
- `docs/experiment_concept.md` — provisional electron-scattering concept.
- `docs/feasibility_and_risks.md` — CLEAR constraints, unresolved points and design risks.
- `docs/data_analysis_plan.md` — proposed measurement and analysis protocol.
- `docs/questions_for_bl4s.md` — technical questions for the organisers.
- `docs/physics_basis.md` — multiple-scattering model and limitations.
- `docs/week2_geant4_demonstrator.md` — Mahmut's Week 2 implementation plan and validation status.
- `docs/team/` — team roles, weekly work and meeting decisions (to be populated).

### Software and simulation

- `analysis/` — NumPy/Matplotlib and PyROOT examples.
- `data/synthetic/` — explicitly synthetic training data.
- `figures/` — generated plots.
- `physics/scattering_estimates.py` — first-order analytical estimate.
- `tests/` — tests for the analytical estimate and data checks.
- `simulation/geant4/week2/` — independent Geant4 11.4.3 six-plane sensitive-tracker demonstrator.
- `notebooks/colab/` — Colab notebooks for execution, simulation and analysis.
- `tools/package_week2_source.py` — source-only offline transfer bundle helper.
- `requirements-week2-analysis.txt` — Python analysis dependencies for the Week 2 notebook.

## Mahmut's completed first software study

The first software-study deliverables are documented in `docs/mahmut_task_log.md` and the Colab notebook `Untitled3.ipynb`. They cover:

- NumPy/Matplotlib analysis of synthetic hit data, summary statistics, SEM and figures.
- PyROOT histogram creation and ROOT file verification.
- Geant4 11.4.3 B1 example setup and an initial electron–aluminium scattering demonstrator.
- Literature-level comparison of Geant4, FLUKA/Flair and GATE/OpenGATE.

These are learning outputs; the synthetic data and training simulations are not CERN beam measurements.

## Week 2 — Mahmut's advanced Geant4 task

Open `notebooks/colab/mahmut_week2_sensitive_tracker.ipynb` in Colab. It builds the independent C++ application in `simulation/geant4/week2/`, runs air-control and aluminium-target conditions, exports hit and track CSV records, reconstructs directions from three upstream and three downstream virtual planes, creates 3D and comparison plots, and uses PyROOT to write and reopen a ROOT TTree and histograms.

**Current status:** source code and notebook are prepared on the Week 2 development branch. The application must still be compiled and run in the user's Colab runtime before it can be marked validated. See `docs/week2_geant4_demonstrator.md`.

## Reproducible workflow

- GitHub is the durable source, documentation and evidence store.
- Google Colab is the preferred run and analysis environment instead of relying on GitHub Actions for simulation execution.
- Save source revisions, run parameters, random seeds, tool versions, logs, outputs and SHA-256 checksums.
- Keep raw and simulated outputs separate from processed summaries.
- Never label synthetic, analytical or simulated outputs as CERN measurements.
- Once Geant4, its data libraries, compiler, CMake and PyROOT are already installed locally, the simulation and analysis steps do not require network access. A fresh Colab runtime still needs initial access to retrieve the notebook/repository and install uncached packages. Full air-gapped execution requires exporting the prepared environment and Geant4 datasets in addition to the source bundle.

## First local checks

Run the analytical calculator:

    python physics/scattering_estimates.py

Run its tests:

    python -m unittest discover -s tests -v

For the Week 2 Geant4 workflow, use the Colab notebook listed above. It records execution and validation evidence separately from the source code.
