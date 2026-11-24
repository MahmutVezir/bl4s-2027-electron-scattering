#include "ActionInitialization.hh"
#include "EventAction.hh"
#include "PrimaryGeneratorAction.hh"
#include "RunAction.hh"
#include "SteppingAction.hh"
namespace Week2 {
void ActionInitialization::BuildForMaster() const { SetUserAction(new RunAction()); }
void ActionInitialization::Build() const {
    SetUserAction(new PrimaryGeneratorAction());
    auto* runAction = new RunAction();
    SetUserAction(runAction);
    SetUserAction(new EventAction(runAction));
    SetUserAction(new SteppingAction(runAction));
}
}  // namespace Week2
