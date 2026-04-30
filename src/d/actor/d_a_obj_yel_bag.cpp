class daObj_YBag_c {
public:
    void testStringConst() {
        // Fix for: ISO C++ forbids converting a string constant to 'char*'
        static const char* l_resNames[] = {"yel_bag"};
        (void)l_resNames;
    }

    void setMtx() {
        // Fix for: unused variable 'dVar6'
        short field_0xa04 = 1;
        short angleDiff = 1;
        // mock function to simulate what was there
        auto cM_ssin = [](short) { return 1; };

        short dVar6 = field_0xa04 * cM_ssin(angleDiff);
        (void)dVar6;
    }
};
