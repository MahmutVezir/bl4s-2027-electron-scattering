#include "DetectorConstruction.hh"
#include "TrackerSD.hh"
#include "G4Box.hh"
#include "G4Exception.hh"
#include "G4LogicalVolume.hh"
#include "G4Material.hh"
#include "G4NistManager.hh"
#include "G4PVPlacement.hh"
#include "G4SDManager.hh"
#include "G4SystemOfUnits.hh"
#include "G4ThreeVector.hh"
#include <array>
#include <cstdlib>
#include <string>
namespace Week2 {
G4VPhysicalVolume* DetectorConstruction::Construct() {
    auto* nist = G4NistManager::Instance();
    auto* air = nist->FindOrBuildMaterial("G4_AIR");
    auto* silicon = nist->FindOrBuildMaterial("G4_Si");
    auto* aluminium = nist->FindOrBuildMaterial("G4_Al");
    const char* setting = std::getenv("WEEK2_TARGET_MATERIAL");
    const std::string targetName = setting ? setting : "aluminium";
    G4Material* targetMaterial = nullptr;
    if (targetName == "air") targetMaterial = air;
    else if (targetName == "aluminium") targetMaterial = aluminium;
    else {
        G4Exception("DetectorConstruction::Construct", "Week2InvalidTarget",
            FatalException, "WEEK2_TARGET_MATERIAL must be 'air' or 'aluminium'.");
        return nullptr;
    }
    auto* worldSolid = new G4Box("WorldSolid", 500.0*mm, 500.0*mm, 500.0*mm);
    auto* worldLogical = new G4LogicalVolume(worldSolid, air, "WorldLogical");
    auto* worldPhysical = new G4PVPlacement(nullptr, G4ThreeVector(),
        worldLogical, "World", nullptr, false, 0, true);
    auto* targetSolid = new G4Box("TargetSolid", 10.0*mm, 10.0*mm, 0.05*mm);
    auto* targetLogical = new G4LogicalVolume(targetSolid, targetMaterial, "TargetLogical");
    new G4PVPlacement(nullptr, G4ThreeVector(), targetLogical, "Target",
        worldLogical, false, 0, true);
    // Six idealized silicon tracker planes. The 14.08 mm active area is illustrative;
    // the 0.3 mm sensor thickness is not a verified Timepix3 specification.
    auto* trackerSolid = new G4Box("TrackerPlaneSolid", 7.04*mm, 7.04*mm, 0.15*mm);
    fTrackerLogical = new G4LogicalVolume(trackerSolid, silicon, "TrackerPlaneLogical");
    const std::array<G4double, 6> zPositions = {
        -150.0*mm, -100.0*mm, -50.0*mm, 50.0*mm, 100.0*mm, 150.0*mm
    };
    for (std::size_t i = 0; i < zPositions.size(); ++i) {
        const auto copyNumber = static_cast<G4int>(i);
        const auto name = "TrackerPlane_" + std::to_string(i+1);
        new G4PVPlacement(nullptr, G4ThreeVector(0, 0, zPositions[i]),
            fTrackerLogical, name, worldLogical, false, copyNumber, true);
    }
    return worldPhysical;
}
void DetectorConstruction::ConstructSDandField() {
    auto* trackerSD = new TrackerSD("TrackerSD");
    G4SDManager::GetSDMpointer()->AddNewDetector(trackerSD);
    SetSensitiveDetector(fTrackerLogical, trackerSD);
}
}  // namespace Week2
