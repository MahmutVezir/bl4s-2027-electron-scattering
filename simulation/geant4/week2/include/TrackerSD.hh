#ifndef BL4S_WEEK2_TRACKER_SD_HH
#define BL4S_WEEK2_TRACKER_SD_HH
#include "G4VSensitiveDetector.hh"
#include "TrackerHit.hh"
#include <set>
#include <utility>
class G4Step;
class G4HCofThisEvent;
namespace Week2 {
class TrackerSD final : public G4VSensitiveDetector {
public:
    explicit TrackerSD(const G4String& name);
    ~TrackerSD() override = default;
    void Initialize(G4HCofThisEvent* hce) override;
    G4bool ProcessHits(G4Step* step, G4TouchableHistory* history) override;
private:
    TrackerHitsCollection* fHitsCollection = nullptr;
    G4int fCollectionID = -1;
    std::set<std::pair<G4int, G4int>> fRecordedTrackPlanePairs;
};
}  // namespace Week2
#endif
