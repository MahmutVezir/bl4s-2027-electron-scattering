# BL4S Week 2 — Sensitive Tracker Demonstrator

## Purpose

This is a small serial Geant4 C++ demonstrator for the Week 2 task. It contains:

- a 100 MeV/c primary electron beam (momentum, not kinetic energy);
- a 100 µm target envelope, filled with air for the control run or aluminium for the target run;
- three idealized silicon tracking planes upstream and three downstream;
- a custom G4VSensitiveDetector, G4VHit and G4THitsCollection;
- primary-electron step recording for offline 3D track visualization;
- CSV output that can be converted to a ROOT TTree and histograms with PyROOT.

## Important scientific boundary

The six silicon planes are a virtual training telescope. They are **not** a claim that six such planes are available at CERN CLEAR. The plane active area is set to 14.08 mm × 14.08 mm to resemble the published Timepix3 pixel matrix footprint; the silicon thickness is an illustrative simulation parameter, not a verified Timepix3 sensor specification.

The beam momentum, spot size, divergence, target dimensions and plane positions are demonstrator parameters. They must not be presented as approved BL4S/CLEAR settings. This is not a validated detector-response simulation.

Only the primary beam electron is stored in tracker hits and trajectory CSV. Secondary particles are not included in the tracking analysis.

## Geometry

- World: air, 1 m × 1 m × 1 m.
- Target envelope: 20 mm × 20 mm × 0.1 mm, centred at z = 0.
- Target material: air (control) or aluminium (target run).
- Tracker planes: z = -150, -100, -50, +50, +100, +150 mm.
- Plane material: silicon.
- Plane active area: 14.08 mm × 14.08 mm.

## Build in the existing Geant4 environment

From this directory:

~~~bash
cmake -S . -B build -DCMAKE_PREFIX_PATH="$CONDA_PREFIX"
cmake --build build -j2
~~~

Run the control condition:

~~~bash
WEEK2_TARGET_MATERIAL=air \
WEEK2_HITS_CSV=results/control/hits.csv \
WEEK2_TRACKS_CSV=results/control/tracks.csv \
./build/week2_tracker macros/run_demo.mac
~~~

Run the aluminium condition:

~~~bash
WEEK2_TARGET_MATERIAL=aluminium \
WEEK2_HITS_CSV=results/aluminium/hits.csv \
WEEK2_TRACKS_CSV=results/aluminium/tracks.csv \
./build/week2_tracker macros/run_demo.mac
~~~

The output directories must exist before running.

## ROOT workflow

Geant4 writes portable CSV files. The companion Colab notebook reads those records with PyROOT and writes a ROOT file containing a TTree plus histograms. This avoids assuming that the installed Geant4 build has its native ROOT analysis backend enabled.

## Reproducibility

The macro sets the Geant4 random seeds before initialization. Both material conditions use the same seed pair. This makes the runs reproducible under the same software and configuration; it does **not** guarantee event-by-event paired random histories after the material change, because particle transport can consume random numbers differently.

Record the Geant4 version, compiler, CMake version, physics list, seeds, event count, target material, source configuration and source commit with each output.

## Offline operation

The source tree and macro are self-contained. Once Geant4 11.4.3, its data libraries, CMake, compiler and PyROOT are present in the local environment, the build, runs, ROOT conversion and plotting require no network access. A fresh Colab runtime still needs an initial download/install step; Colab itself cannot be launched in a fully disconnected environment. For a genuinely air-gapped computer, export the prepared environment and Geant4 data libraries together with this source tree.
