#ifndef BL4S_WEEK2_PRIMARY_GENERATOR_ACTION_HH
#define BL4S_WEEK2_PRIMARY_GENERATOR_ACTION_HH
#include "G4VUserPrimaryGeneratorAction.hh"
class G4ParticleGun;
class G4Event;
namespace Week2 {
class PrimaryGeneratorAction final : public G4VUserPrimaryGeneratorAction {
public:
    PrimaryGeneratorAction();
    ~PrimaryGeneratorAction() override;
    void GeneratePrimaries(G4Event* event) override;
private:
    G4ParticleGun* fParticleGun = nullptr;
};
}  // namespace Week2
#endif
