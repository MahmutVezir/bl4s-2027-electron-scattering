# Week 2 — Mahmut: Programming and 3D Simulations

**Status:** Source package prepared; Colab execution and validation still required.

## Task mapping

| Assigned requirement | Implementation |
|---|---|
| Build Geant4 skills with C++ | Independent Geant4 11.4.x C++ application |
| More complex 3D setup | Air world, target envelope and six idealized silicon tracker planes |
| Sensitive detectors | Custom G4VSensitiveDetector::ProcessHits() |
| Record particle interactions | G4VHit / G4THitsCollection with event, track, plane, position, direction, energy, time and step energy deposit |
| Visualize particle tracks | Primary-electron step CSV, rendered as a 3D Matplotlib view in Colab |
| Export to ROOT | PyROOT converts hit CSV to a ROOT TTree and analysis histograms |
| Demonstrate learning | Control/target runs, comparison plots and short explanation |

## Geometry and beam

The demonstrator uses 100 MeV/c electrons. Geant4's particle gun is configured with the corresponding kinetic energy using:

T = sqrt(p^2 + m_e^2) - m_e.

The target envelope is 20 mm × 20 mm × 0.1 mm and is filled with air for the control run or aluminium for the target run. Six idealized silicon planes are positioned at z = -150, -100, -50, +50, +100 and +150 mm.

These dimensions are training parameters, not confirmed CLEAR settings. The six-plane telescope is virtual and must not be described as CERN's available Timepix3 arrangement.

## Data flow

1. TrackerSD registers one hit per primary electron per plane and event.
2. EventAction reads the event hit collection and writes hits.csv.
3. SteppingAction writes primary-electron trajectory points to tracks.csv.
4. Colab plots the trajectory and reconstructs incoming/outgoing directions from the three upstream and three downstream planes.
5. PyROOT writes a portable ROOT file with the hit TTree and histograms.
6. A manifest records file sizes and SHA-256 digests.

## Important method limitations

- Only primary electrons are included in tracker hits and trajectory plots.
- The tracker planes are idealized sensitive silicon slabs; charge transport, pixel clustering, thresholds, electronic noise, dead time, time-walk and the full Timepix3 response are not simulated.
- The reconstructed direction is based on a straight-line fit to three planes on each side. Magnetic fields and alignment imperfections are not included.
- The same random seed pair is used for both target materials. Identical seeds aid reproducibility but do not guarantee event-by-event paired histories.
- Geant4 writes CSV; PyROOT produces ROOT. Native Geant4 ROOT output is not assumed.

## Validation still required

This package has not yet been compiled or run in the user's Colab runtime. Before delivery, run the Colab notebook and verify:

- CMake configuration and C++ compilation succeed;
- both material conditions exit with code 0;
- hit records include plane IDs 0–5;
- primary-electron tracks are written;
- PyROOT can reopen the output ROOT file;
- TTree entries and histogram entries match the CSV records;
- generated plots and metadata are saved with SHA-256.

## Offline note

After Geant4 11.4.3, its data sets, compiler, CMake and PyROOT are installed locally, the simulation and analysis steps do not require network access. A new Colab runtime still requires access to fetch the notebook/repository and to install uncached packages. Full air-gapped execution requires exporting the prepared environment and data sets as a separate bundle.

## References

- Geant4 11.4 FAQ — Tracks and steps: https://geant4.web.cern.ch/documentation/dev/faq_html/FAQ/tracksAndSteps.html
- Geant4 11.4 Basic Examples: https://geant4.web.cern.ch/documentation/dev/bfad_html/ForApplicationDevelopers/Examples/BasicCodes.html
- Geant4 11.4 Run: https://geant4.web.cern.ch/documentation/dev/bfad_html/ForApplicationDevelopers/Fundamentals/run.html
