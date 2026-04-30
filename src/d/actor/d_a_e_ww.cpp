#include <cstdint>

typedef unsigned int u32;

class Model {
public:
    void setUserArea(u32 area) {}
};

class daE_WW_c {
public:
    int calcJumpSpeed() {
        // Fix for: unused variable 'unused'
        int unused = 0;
        (void)unused;
        return 1;
    }

    void CreateHeap(Model* model) {
        // Fix for: cast from 'daE_WW_c*' to 'u32' loses precision
        model->setUserArea((u32)(uintptr_t)this);
    }
};
