# Week 2 — Mahmut: Programming and 3D Simulations

**Status:** Source package prepared. Colab compilation and runtime validation are pending.

## Task mapping

| Assigned requirement | Implementation |
|---|---|
| Develop Geant4 skills using C++ | Independent Geant4 11.4 C++ application |
| Build a more complex 3D setup | Air world, target volume and six virtual tracker planes |
| Model sensitive detectors | Custom `G4VSensitiveDetector::ProcessHits()` |
| Record interactions | `G4VHit` and `G4THitsCollection` with event, track, plane, position, direction, energy, time and step energy deposit |
| Visualise particle tracks | Primary-electron step CSV rendered as a 3D Matplotlib plot |
| Export data to ROOT | PyROOT converts the hit CSV into a ROOT `TTree` and histograms |
| Demonstrate learning | Air-control and aluminium-target runs, comparison plots and a short technical explanation |

## Demonstrator geometry and beam

- Primary particle: electron.
- Nominal momentum: 100 MeV/c.
- Geant4 particle gun receives kinetic energy calculated from momentum and electron mass:
  `T = sqrt(p^2 + m_e^2) - m_e`.
- World: air, 1 m × 1 m × 1 m.
- Target envelope: 20 mm × 20 mm × 0.1 mm, centred at z = 0.
- Target material: air for the control run or aluminium for the target run.
- Six thin air scoring planes: z = -150, -100, -50, +50, +100 and +150 mm.
- Each scoring plane has a 14.08 mm × 14.08 mm transverse footprint.

The six planes are a **virtual training telescope**. They are not a statement that six tracker planes or this geometry are available at CERN CLEAR. The scoring volumes are air-filled and are not a silicon sensor or a Timepix3 detector-response model. All beam and geometry values are educational parameters pending facility confirmation.

## Data flow

1. `TrackerSD` records one primary-electron hit per plane and event.
2. `EventAction` reads the event's hit collection and writes `hits.csv`.
3. `SteppingAction` writes primary-electron step positions, kinetic energy, step energy deposit and the process defining each step to `tracks.csv`.
4. The Colab notebook fits straight lines to the three upstream and three downstream virtual planes to estimate incoming and outgoing directions.
5. Matplotlib creates a 3D trajectory plot and comparison plots.
6. PyROOT writes a ROOT file with one hit `TTree` per material condition plus histograms.
7. The notebook reopens the ROOT file, checks tree/histogram entry counts, and writes metadata and SHA-256 hashes.

## Method limitations

- Only primary electrons are included in the tracking hit and trajectory outputs; secondary particles are not reconstructed.
- The planes are idealised air scoring volumes, not a detector-response simulation.
- Pixel charge transport, clustering, thresholds, noise, dead time, time-walk, sensor response and alignment uncertainties are not modelled.
- Direction reconstruction uses straight-line fits to three points on each side. Magnetic fields and multiple-scattering-aware track fitting are not included.
- The 100 MeV/c beam and all dimensions are demonstration settings, not confirmed CLEAR settings.
- Identical random seeds improve run reproducibility but do not guarantee event-by-event paired transport histories after the material changes.
- Geant4 writes portable CSV. PyROOT creates the ROOT file; native Geant4 ROOT-backend support is not assumed.

## Validation checklist

Do not mark this task complete until the Colab runtime confirms:

- CMake configuration succeeds with the installed Geant4 11.4.x environment.
- The C++ executable builds.
- Both material conditions finish with exit code 0.
- Hit data contain the expected plane IDs 0–5.
- Primary-electron trajectory records are non-empty.
- At least some events have all six plane hits and can be reconstructed.
- The ROOT file reopens; TTree and histogram entry counts match the CSV-derived counts.
- 3D and comparison figures are created.
- Metadata and a SHA-256 manifest are saved.

## Offline operation

Once Geant4 11.4.3, its datasets, CMake, a compatible C++ compiler and PyROOT are already installed locally, build, simulation and analysis can run without network access. A fresh Colab runtime still needs internet access to retrieve the notebook/repository and install uncached packages. A genuinely air-gapped Linux computer needs the source bundle and a separate archive of the Geant4 environment and datasets. The full offline archive has not yet been tested on a second machine.

## References

- Geant4 11.4 FAQ — Tracks and steps: https://geant4.web.cern.ch/documentation/dev/faq_html/FAQ/tracksAndSteps.html
- Geant4 11.4 Basic examples: https://geant4.web.cern.ch/documentation/dev/bfad_html/ForApplicationDevelopers/Examples/BasicCodes.html
- Geant4 11.4 CMake usage: https://geant4.web.cern.ch/documentation/dev/ig_html/InstallationGuide/buildtools.html
