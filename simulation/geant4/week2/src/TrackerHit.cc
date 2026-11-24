#include "TrackerHit.hh"

namespace Week2 {
G4ThreadLocal G4Allocator<TrackerHit>* TrackerHitAllocator = nullptr;

TrackerHit::TrackerHit(
    G4int trackID, G4int parentID, G4int pdgCode, G4int planeID,
    const G4ThreeVector& position, const G4ThreeVector& direction,
    G4double kineticEnergy, G4double globalTime, G4double energyDeposit)
    : fTrackID(trackID), fParentID(parentID), fPDGCode(pdgCode),
      fPlaneID(planeID), fPosition(position), fDirection(direction),
      fKineticEnergy(kineticEnergy), fGlobalTime(globalTime),
      fEnergyDeposit(energyDeposit) {}

void* TrackerHit::operator new(std::size_t) {
    if (TrackerHitAllocator == nullptr) {
        TrackerHitAllocator = new G4Allocator<TrackerHit>;
    }
    return TrackerHitAllocator->MallocSingle();
}

void TrackerHit::operator delete(void* hit) {
    if (TrackerHitAllocator != nullptr) {
        TrackerHitAllocator->FreeSingle(static_cast<TrackerHit*>(hit));
    }
}
}  // namespace Week2
