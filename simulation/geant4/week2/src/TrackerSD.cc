#include "TrackerSD.hh"
#include "G4HCofThisEvent.hh"
#include "G4SDManager.hh"
#include "G4Step.hh"
#include "G4StepPoint.hh"
#include "G4SystemOfUnits.hh"
#include "G4Track.hh"
#include "G4TouchableHandle.hh"
namespace Week2 {
TrackerSD::TrackerSD(const G4String& name) : G4VSensitiveDetector(name) {
    collectionName.insert("TrackerHits");
}
void TrackerSD::Initialize(G4HCofThisEvent* hce) {
    fHitsCollection = new TrackerHitsCollection(SensitiveDetectorName, collectionName[0]);
    if (fCollectionID < 0) {
        fCollectionID = G4SDManager::GetSDMpointer()->GetCollectionID(
            SensitiveDetectorName + "/" + collectionName[0]);
    }
    hce->AddHitsCollection(fCollectionID, fHitsCollection);
    fRecordedTrackPlanePairs.clear();
}
G4bool TrackerSD::ProcessHits(G4Step* step, G4TouchableHistory*) {
    if (step == nullptr || fHitsCollection == nullptr) return false;
    const auto* track = step->GetTrack();
    const auto* pre = step->GetPreStepPoint();
    if (track->GetParentID() != 0 ||
        track->GetDefinition()->GetPDGEncoding() != 11) return false;
    const auto touchable = pre->GetTouchableHandle();
    const G4int planeID = touchable->GetCopyNumber(0);
    const auto key = std::make_pair(track->GetTrackID(), planeID);
    if (!fRecordedTrackPlanePairs.insert(key).second) return false;
    auto* hit = new TrackerHit(
        track->GetTrackID(), track->GetParentID(),
        track->GetDefinition()->GetPDGEncoding(), planeID,
        pre->GetPosition(), pre->GetMomentumDirection(),
        pre->GetKineticEnergy(), pre->GetGlobalTime(),
        step->GetTotalEnergyDeposit());
    fHitsCollection->insert(hit);
    return true;
}
}  // namespace Week2
