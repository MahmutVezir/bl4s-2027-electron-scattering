#include "EventAction.hh"
#include "RunAction.hh"
#include "TrackerHit.hh"
#include "G4Event.hh"
#include "G4HCofThisEvent.hh"
#include "G4SDManager.hh"
namespace Week2 {
EventAction::EventAction(RunAction* runAction) : fRunAction(runAction) {}
void EventAction::EndOfEventAction(const G4Event* event) {
    if (event == nullptr || fRunAction == nullptr) return;
    if (fHitsCollectionID < 0) {
        fHitsCollectionID = G4SDManager::GetSDMpointer()->GetCollectionID(
            "TrackerSD/TrackerHits");
    }
    auto* hce = event->GetHCofThisEvent();
    if (hce == nullptr) return;
    auto* hits = static_cast<TrackerHitsCollection*>(hce->GetHC(fHitsCollectionID));
    if (hits == nullptr) return;
    for (std::size_t i = 0; i < hits->GetSize(); ++i) {
        const auto* hit = (*hits)[i];
        const auto& p = hit->GetPosition();
        const auto& d = hit->GetDirection();
        fRunAction->WriteHit(event->GetEventID(), hit->GetTrackID(),
            hit->GetParentID(), hit->GetPDGCode(), hit->GetPlaneID(),
            p.x(), p.y(), p.z(), d.x(), d.y(), d.z(),
            hit->GetKineticEnergy(), hit->GetGlobalTime(), hit->GetEnergyDeposit());
    }
}
}  // namespace Week2
