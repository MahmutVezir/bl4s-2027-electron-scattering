#ifndef BL4S_WEEK2_TRACKER_HIT_HH
#define BL4S_WEEK2_TRACKER_HIT_HH
#include "G4Allocator.hh"
#include "G4THitsCollection.hh"
#include "G4ThreeVector.hh"
#include "G4VHit.hh"
#include "globals.hh"
#include <cstddef>

namespace Week2 {
class TrackerHit final : public G4VHit {
public:
    TrackerHit(G4int trackID, G4int parentID, G4int pdgCode, G4int planeID,
        const G4ThreeVector& position, const G4ThreeVector& direction,
        G4double kineticEnergy, G4double globalTime, G4double energyDeposit);
    ~TrackerHit() override = default;
    void* operator new(std::size_t);
    void operator delete(void* hit);
    void Draw() override {}
    void Print() override {}
    G4int GetTrackID() const { return fTrackID; }
    G4int GetParentID() const { return fParentID; }
    G4int GetPDGCode() const { return fPDGCode; }
    G4int GetPlaneID() const { return fPlaneID; }
    const G4ThreeVector& GetPosition() const { return fPosition; }
    const G4ThreeVector& GetDirection() const { return fDirection; }
    G4double GetKineticEnergy() const { return fKineticEnergy; }
    G4double GetGlobalTime() const { return fGlobalTime; }
    G4double GetEnergyDeposit() const { return fEnergyDeposit; }
private:
    G4int fTrackID, fParentID, fPDGCode, fPlaneID;
    G4ThreeVector fPosition, fDirection;
    G4double fKineticEnergy, fGlobalTime, fEnergyDeposit;
};
using TrackerHitsCollection = G4THitsCollection<TrackerHit>;
extern G4ThreadLocal G4Allocator<TrackerHit>* TrackerHitAllocator;
}  // namespace Week2
#endif
