#ifndef BL4S_WEEK2_ACTION_INITIALIZATION_HH
#define BL4S_WEEK2_ACTION_INITIALIZATION_HH
#include "G4VUserActionInitialization.hh"
namespace Week2 {
class ActionInitialization final : public G4VUserActionInitialization {
public:
    ActionInitialization() = default;
    ~ActionInitialization() override = default;
    void BuildForMaster() const override;
    void Build() const override;
};
}  // namespace Week2
#endif
