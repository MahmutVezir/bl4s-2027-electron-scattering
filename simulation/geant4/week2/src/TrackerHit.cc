#include "TrackerHit.hh"
namespace Week2 {
TrackerHit::TrackerHit(
    G4int trackID, G4int parentID, G4int pdgCode, G4int planeID,
    const G4ThreeVector& position, const G4ThreeVector& direction,
    G4double kineticEnergy, G4double globalTime, G4double energyDeposit)
    : fTrackID(trackID), fParentID(parentID), fPDGCode(pdgCode),
      fPlaneID(planeID), fPosition(position), fDirection(direction),
      fKineticEnergy(kineticEnergy), fGlobalTime(globalTime),
      fEnergyDeposit(energyDeposit) {}
}  // namespace Week2
