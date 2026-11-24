#ifndef BL4S_WEEK2_EVENT_ACTION_HH
#define BL4S_WEEK2_EVENT_ACTION_HH
#include "G4UserEventAction.hh"
#include "globals.hh"
class G4Event;
namespace Week2 {
class RunAction;
class EventAction final : public G4UserEventAction {
public:
    explicit EventAction(RunAction* runAction);
    ~EventAction() override = default;
    void EndOfEventAction(const G4Event* event) override;
private:
    RunAction* fRunAction = nullptr;
    G4int fHitsCollectionID = -1;
};
}  // namespace Week2
#endif
