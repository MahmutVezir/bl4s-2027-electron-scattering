# Offline and closed-environment workflow

## What is self-contained now?

The Week 2 application source, CMake project, macro, Colab notebook, Python requirements and environment recipe are stored in this repository. The source-only ZIP helper collects those project files.

The Geant4 simulation and PyROOT analysis require these installed components:

- Geant4 11.4.3 and all data libraries used by that build;
- CMake and a compatible C++ compiler;
- Python with NumPy, pandas and Matplotlib;
- PyROOT compatible with the Python runtime.

Once these components are already present on a compatible Linux machine, configuration, compilation, simulation, ROOT conversion, plotting and checksum generation do not need internet access.

## Important platform limitation

Google Colab is a hosted service. Opening a notebook from GitHub and creating a fresh Colab runtime requires internet access. A running Colab session can continue to work without network access only when the required source and packages are already present in that runtime.

A genuinely disconnected computer must receive the source bundle **and** the prepared Geant4 environment/data libraries separately. The source ZIP alone is not a complete software environment.

## Preparing a full environment archive from Colab

The Week 2 notebook includes an optional cell guarded by EXPORT_FULL_OFFLINE_BUNDLE. When enabled, it:

1. creates a source-only ZIP;
2. downloads the Python analysis wheels into a local wheelhouse;
3. uses conda-pack to archive the installed Geant4 environment, including its installed Geant4 data packages;
4. writes restore instructions and SHA-256 hashes.

The resulting environment archive can be large. Check available disk space before running it. Do not commit a multi-gigabyte environment archive to GitHub; store it on approved external storage or a team Drive and keep its hash and location in this repository.

## Restore on a compatible offline Linux machine

1. Copy the source ZIP, Geant4 environment archive and Python wheelhouse to the offline machine.
2. Extract the Geant4 environment to a writable directory.
3. Run the extracted environment's conda-unpack script once to repair embedded paths.
4. Activate the extracted environment.
5. Install Python analysis packages from the wheelhouse with pip --no-index --find-links.
6. Build the C++ application and run the supplied macro.
7. Re-run the validation and checksum steps.

The environment archive is platform-specific. Use a compatible Linux x86_64 system and a compatible Python ABI. Windows users should use a suitable Linux environment such as WSL2 or a Linux machine; do not assume a Linux Geant4 binary archive runs natively on Windows.

## Reproducibility records

For each result package, keep:

- Geant4 version and data-set environment;
- compiler and CMake versions;
- physics list, primary particle, momentum and target settings;
- macro contents and random seeds;
- source commit SHA;
- raw CSV, ROOT file, logs and figures;
- SHA-256 manifest.

Never mark the offline workflow as verified until the archive has been extracted and successfully run on a second environment with network access disabled.
