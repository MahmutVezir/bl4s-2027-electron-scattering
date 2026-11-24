#ifndef BL4S_WEEK2_DETECTOR_CONSTRUCTION_HH
#define BL4S_WEEK2_DETECTOR_CONSTRUCTION_HH
#include "G4VUserDetectorConstruction.hh"
class G4LogicalVolume;
class G4VPhysicalVolume;
namespace Week2 {
class DetectorConstruction final : public G4VUserDetectorConstruction {
public:
    DetectorConstruction() = default;
    ~DetectorConstruction() override = default;
    G4VPhysicalVolume* Construct() override;
    void ConstructSDandField() override;
private:
    G4LogicalVolume* fTrackerLogical = nullptr;
};
}  // namespace Week2
#endif
