#include "PrimaryGeneratorAction.hh"
#include "G4Event.hh"
#include "G4Exception.hh"
#include "G4ParticleGun.hh"
#include "G4ParticleTable.hh"
#include "G4SystemOfUnits.hh"
#include "G4ThreeVector.hh"
#include "Randomize.hh"
#include <cmath>
namespace Week2 {
PrimaryGeneratorAction::PrimaryGeneratorAction() {
    fParticleGun = new G4ParticleGun(1);
    auto* electron = G4ParticleTable::GetParticleTable()->FindParticle("e-");
    if (electron == nullptr) {
        G4Exception("PrimaryGeneratorAction::PrimaryGeneratorAction",
            "Week2ElectronMissing", FatalException,
            "Could not find the electron definition.");
        return;
    }
    // Set 100 MeV/c momentum; G4ParticleGun takes kinetic energy.
    const G4double p = 100.0*MeV;
    const G4double m = electron->GetPDGMass();
    const G4double kineticEnergy = std::sqrt(p*p + m*m) - m;
    fParticleGun->SetParticleDefinition(electron);
    fParticleGun->SetParticleEnergy(kineticEnergy);
}
PrimaryGeneratorAction::~PrimaryGeneratorAction() { delete fParticleGun; }
void PrimaryGeneratorAction::GeneratePrimaries(G4Event* event) {
    const G4double x = G4RandGauss::shoot(0.0, 0.25*mm);
    const G4double y = G4RandGauss::shoot(0.0, 0.25*mm);
    const G4double tx = G4RandGauss::shoot(0.0, 0.2*mrad);
    const G4double ty = G4RandGauss::shoot(0.0, 0.2*mrad);
    fParticleGun->SetParticlePosition(G4ThreeVector(x, y, -230.0*mm));
    fParticleGun->SetParticleMomentumDirection(G4ThreeVector(tx, ty, 1.0).unit());
    fParticleGun->GeneratePrimaryVertex(event);
}
}  // namespace Week2
