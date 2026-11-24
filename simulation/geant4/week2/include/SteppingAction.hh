#ifndef BL4S_WEEK2_STEPPING_ACTION_HH
#define BL4S_WEEK2_STEPPING_ACTION_HH
#include "G4UserSteppingAction.hh"
class G4Step;
namespace Week2 {
class RunAction;
class SteppingAction final : public G4UserSteppingAction {
public:
    explicit SteppingAction(RunAction* runAction);
    ~SteppingAction() override = default;
    void UserSteppingAction(const G4Step* step) override;
private:
    RunAction* fRunAction = nullptr;
};
}  // namespace Week2
#endif
