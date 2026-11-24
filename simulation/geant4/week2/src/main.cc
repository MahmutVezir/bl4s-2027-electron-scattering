#include "ActionInitialization.hh"
#include "DetectorConstruction.hh"
#include "QBBC.hh"
#include "G4RunManagerFactory.hh"
#include "G4UImanager.hh"
#include <iostream>
int main(int argc, char** argv) {
    if (argc != 2) {
        std::cerr << "Usage: week2_tracker run_demo.mac\n";
        return 2;
    }
    auto* runManager = G4RunManagerFactory::CreateRunManager(G4RunManagerType::Serial);
    runManager->SetUserInitialization(new Week2::DetectorConstruction());
    auto* physicsList = new QBBC();
    physicsList->SetVerboseLevel(0);
    runManager->SetUserInitialization(physicsList);
    runManager->SetUserInitialization(new Week2::ActionInitialization());
    const G4String command = G4String("/control/execute ") + argv[1];
    const G4int status = G4UImanager::GetUIpointer()->ApplyCommand(command);
    delete runManager;
    return status == 0 ? 0 : 1;
}
