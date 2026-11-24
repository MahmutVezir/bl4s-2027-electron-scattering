# Mahmut — BL4S 2027 software and simulation work log

**Last updated:** 24 November 2026  
**Working repository:** MahmutVezir/bl4s-2027-electron-scattering  
**Execution policy:** Google Colab is the preferred run environment; GitHub is the durable source and evidence store.

This log distinguishes completed work from source code that has only been prepared and still requires execution.

## First assignment — Python, ROOT/PyROOT, Geant4, FLUKA/Flair and GATE/OpenGATE

### 1. Python / NumPy / Matplotlib — completed

- [x] Deterministic synthetic hit dataset with 480 records: 240 no-target reference and 240 aluminium-labelled synthetic examples.
- [x] Histograms for both synthetic groups.
- [x] Mean, sample standard deviation and standard error of the mean (SEM).
- [x] Mean ± SEM plot.
- [x] Reproducible analysis script: `analysis/analyze_synthetic_hits.py`.
- [x] Ten tests passed in the Colab run recorded in the working conversation.
- [x] Python/NumPy/Matplotlib versions recorded in the Colab session.

**Boundary:** the sample is synthetic training data. It does not demonstrate physical electron scattering and is not CERN beam data. SEM describes the uncertainty of the sample mean, not the distribution width or systematic uncertainty.

### 2. ROOT / PyROOT — completed in Colab

- [x] ROOT 6.40.00 available in Colab through the PyPI ROOT package.
- [x] Two TH1D histograms generated from the synthetic CSV data.
- [x] ROOT file written and reopened.
- [x] Histogram entry counts verified: 240 in h_reference and 240 in h_aluminium.

**Boundary:** PyPI ROOT was an alpha distribution in the tested runtime. This is a successful educational/prototype workflow, not a production deployment qualification.

### 3. Geant4 — initial demonstrator completed

- [x] Geant4 11.4.3 and its data libraries installed in Colab through Micromamba.
- [x] Official Basic Example B1 inspected, configured, compiled and run in batch mode.
- [x] Independent electron–aluminium training application created in Colab.
- [x] 5 MeV primary electron, 0.1 mm aluminium target and one downstream scoring slab.
- [x] Air-filled control and aluminium target runs completed with 1,000 events each.
- [x] Hit CSV files and three plots created; hit records checked for missing values and unit direction vectors.
- [x] A comparison table was produced.

Pilot comparison recorded in the Colab session:

| Metric | Air control | Aluminium target |
|---|---:|---:|
| Hit records | 1,000 | 1,000 |
| Mean kinetic energy | 4.965384 MeV | 4.920348 MeV |
| Energy sample SD | 0.074033 MeV | 0.118808 MeV |
| Mean recorded angle | 3.07646° | 5.78446° |
| Angle sample SD | 2.093571° | 4.079586° |
| Mean hit radius | 3.679245 mm | 9.155216 mm |

**Important seed caveat:** the macro used in the two runs contained the seed pair 12345 and 67890. A metadata record listed a different seed pair for the aluminium case, but the executed macro was not changed in the run loop. Therefore the differing seed metadata must not be treated as executed seeds. Preserve the CSV/logs as a pilot result, but use corrected explicit seed handling for future runs.

**Scientific boundary:** this was a 5 MeV software demonstrator, not a CLEAR beam simulation and not a detector-response model. One downstream plane does not independently measure a per-particle scattering angle; the recorded direction came from Geant4 tracking information.

### 4. FLUKA / Flair — documentation study completed

- [x] FLUKA's independent Monte Carlo particle-transport role reviewed.
- [x] Flair's role as a FLUKA input, geometry, run and results interface reviewed.
- [x] Differences from Geant4 documented.

No FLUKA/Flair installation or transport run was performed as part of the first assignment.

### 5. GATE / OpenGATE — documentation study completed

- [x] GATE's Geant4 basis reviewed.
- [x] Main use cases in PET/SPECT, CT, radiotherapy and dosimetry documented.

No OpenGATE simulation was required or performed for the first assignment.

## Week 2 — Programming and 3D simulations

**Branch:** `research/week2-geant4-sensitive-tracker-2026-11-24`  
**Status:** source package and Colab notebook prepared; runtime validation pending.

Assigned outcomes and implementation:

- [x] Separate Geant4 11.4.x C++ project created under `simulation/geant4/week2/`.
- [x] 100 MeV/c primary electron beam configured; the kinetic energy is calculated from momentum and electron mass.
- [x] Air-control and aluminium target material options use the same target envelope.
- [x] Six virtual silicon tracker planes defined: three upstream and three downstream.
- [x] Custom TrackerHit, TrackerSD, G4VSensitiveDetector::ProcessHits and G4THitsCollection source added.
- [x] EventAction writes event-level sensitive detector hits to CSV.
- [x] SteppingAction records primary electron trajectory points to CSV.
- [x] Serial run configuration and fixed seed macro added.
- [x] Colab notebook created to configure/build, run both target conditions, validate records, reconstruct line directions, produce 3D plots and export ROOT TTrees/histograms through PyROOT.
- [x] SHA-256 and metadata generation included in the notebook.

Still required before marking Week 2 complete:

- [ ] Run the notebook in Colab from a clean or documented runtime.
- [ ] Fix any compile/runtime errors revealed by actual execution.
- [ ] Confirm hit plane IDs 0–5 are all present.
- [ ] Confirm the ROOT file can be reopened and TTree/histogram entry counts match CSV.
- [ ] Inspect the 3D track and comparison plots.
- [ ] Commit the executed notebook outputs or the corresponding output evidence package.
- [ ] Complete the short explanation for the team meeting.

### Week 2 scientific boundaries

- The six-plane device is a virtual training telescope, not the confirmed CERN CLEAR detector arrangement.
- The 14.08 mm × 14.08 mm plane footprint is illustrative; the model is not a full Timepix3 response simulation.
- Only primary electrons are written to the tracker hit and trajectory outputs.
- The simple straight-line fits do not include magnetic fields, alignment errors, pixel clustering, thresholds, dead time or electronic noise.
- The 100 MeV/c source and target/plane geometry are demonstrator settings, not approved CLEAR parameters.
- Geant4 writes portable CSV; PyROOT creates the ROOT TTree and histograms. Native Geant4 ROOT output is not assumed.
- Identical seeds do not guarantee event-by-event paired histories between different materials.

## Execution and evidence policy

- Do not claim successful compilation or simulation until the Colab log shows a successful exit code and expected files.
- Store the Geant4 version, physics list, compiler, CMake version, macro, random seeds, event count, environment and source commit.
- Preserve raw CSV outputs. Derived tables and figures are separate.
- Use a SHA-256 manifest for deliverable files.
- GitHub Actions is not the simulation execution route; Colab is the preferred execution and validation environment.
- A fresh Colab runtime needs network access to obtain the repository and uncached packages. After Geant4 and its datasets are installed locally, build/run/analysis can be executed without network access. Fully air-gapped execution requires exporting the binaries and datasets as well as the source tree.

## Key artifacts

- First assignment notebook: `Untitled3.ipynb`.
- First assignment report: `BL4S_2027_Technical_Preparation_Report_Mahmut_Vezir.docx` (shared separately).
- Week 2 Geant4 source: `simulation/geant4/week2/`.
- Week 2 Colab notebook: `notebooks/colab/mahmut_week2_sensitive_tracker.ipynb`.
- Week 2 technical note: `docs/week2_geant4_demonstrator.md`.
