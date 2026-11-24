#ifndef BL4S_WEEK2_RUN_ACTION_HH
#define BL4S_WEEK2_RUN_ACTION_HH
#include "G4UserRunAction.hh"
#include "globals.hh"
#include <fstream>
class G4Run;
namespace Week2 {
class RunAction final : public G4UserRunAction {
public:
    RunAction() = default;
    ~RunAction() override = default;
    void BeginOfRunAction(const G4Run* run) override;
    void EndOfRunAction(const G4Run* run) override;
    void WriteHit(G4int eventID, G4int trackID, G4int parentID, G4int pdgCode,
        G4int planeID, G4double x, G4double y, G4double z,
        G4double ux, G4double uy, G4double uz, G4double kineticEnergy,
        G4double globalTime, G4double energyDeposit);
    void WriteTrackPoint(G4int eventID, G4int trackID, G4int stepNumber,
        G4double x, G4double y, G4double z, G4double kineticEnergy,
        G4double energyDeposit, const G4String& processName);
private:
    std::ofstream fHitsOutput;
    std::ofstream fTracksOutput;
};
}  // namespace Week2
#endif
