#include "SteppingAction.hh"
#include "RunAction.hh"
#include "G4Event.hh"
#include "G4RunManager.hh"
#include "G4Step.hh"
#include "G4StepPoint.hh"
#include "G4Track.hh"
namespace Week2 {
SteppingAction::SteppingAction(RunAction* runAction) : fRunAction(runAction) {}
void SteppingAction::UserSteppingAction(const G4Step* step) {
    if (step == nullptr || fRunAction == nullptr) return;
    const auto* track = step->GetTrack();
    if (track->GetParentID() != 0 || track->GetDefinition()->GetPDGEncoding() != 11) return;
    const auto* post = step->GetPostStepPoint();
    const auto* event = G4RunManager::GetRunManager()->GetCurrentEvent();
    if (post == nullptr || event == nullptr) return;
    const auto& p = post->GetPosition();
    fRunAction->WriteTrackPoint(event->GetEventID(), track->GetTrackID(),
        track->GetCurrentStepNumber(), p.x(), p.y(), p.z(), post->GetKineticEnergy());
}
}  // namespace Week2
