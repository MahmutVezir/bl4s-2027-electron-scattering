#include "RunAction.hh"
#include "G4Exception.hh"
#include "G4Run.hh"
#include "G4SystemOfUnits.hh"
#include <cstdlib>
#include <iomanip>
namespace Week2 {
void RunAction::BeginOfRunAction(const G4Run*) {
    const char* hitsPath = std::getenv("WEEK2_HITS_CSV");
    const char* tracksPath = std::getenv("WEEK2_TRACKS_CSV");
    fHitsOutput.open(hitsPath ? hitsPath : "hits.csv", std::ios::out|std::ios::trunc);
    fTracksOutput.open(tracksPath ? tracksPath : "tracks.csv", std::ios::out|std::ios::trunc);
    if (!fHitsOutput.is_open() || !fTracksOutput.is_open()) {
        G4Exception("RunAction::BeginOfRunAction", "Week2OutputOpenError",
            FatalException, "Could not open one or more CSV output files.");
        return;
    }
    fHitsOutput << "event_id,track_id,parent_id,pdg_code,plane_id,"
        << "x_mm,y_mm,z_mm,ux,uy,uz,kinetic_energy_MeV,global_time_ns,edep_MeV\n";
    fTracksOutput << "event_id,track_id,step_no,x_mm,y_mm,z_mm,"
        << "kinetic_energy_MeV,edep_MeV,process_name\n";
    fHitsOutput << std::setprecision(12);
    fTracksOutput << std::setprecision(12);
}
void RunAction::WriteHit(G4int eventID, G4int trackID, G4int parentID,
    G4int pdgCode, G4int planeID, G4double x, G4double y, G4double z,
    G4double ux, G4double uy, G4double uz, G4double kineticEnergy,
    G4double globalTime, G4double energyDeposit) {
    if (!fHitsOutput.is_open()) return;
    fHitsOutput << eventID << "," << trackID << "," << parentID << ","
        << pdgCode << "," << planeID << "," << x/mm << "," << y/mm << ","
        << z/mm << "," << ux << "," << uy << "," << uz << ","
        << kineticEnergy/MeV << "," << globalTime/ns << ","
        << energyDeposit/MeV << "\n";
}
void RunAction::WriteTrackPoint(G4int eventID, G4int trackID, G4int stepNumber,
    G4double x, G4double y, G4double z, G4double kineticEnergy,
    G4double energyDeposit, const G4String& processName) {
    if (!fTracksOutput.is_open()) return;
    fTracksOutput << eventID << "," << trackID << "," << stepNumber << ","
        << x/mm << "," << y/mm << "," << z/mm << ","
        << kineticEnergy/MeV << "," << energyDeposit/MeV << ","
        << processName << "\n";
}
void RunAction::EndOfRunAction(const G4Run*) {
    if (fHitsOutput.is_open()) fHitsOutput.close();
    if (fTracksOutput.is_open()) fTracksOutput.close();
}
}  // namespace Week2
