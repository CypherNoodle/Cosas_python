class fopAc_ac_c {};
class cXyz {};

struct obj_kita_class {
    fopAc_ac_c mActor;
};

void action(obj_kita_class* i_this) {
    // Fix: Remove unused variables 'a_this', 'cStack_24', 'cStack_30'
    // fopAc_ac_c* a_this = (fopAc_ac_c*)&i_this->mActor;
    // cXyz cStack_24;
    // cXyz cStack_30;
}

int daObj_Kita_Execute(obj_kita_class* i_this) {
    // Fix: Remove unused variable 'a_this'
    // fopAc_ac_c* a_this = (fopAc_ac_c*)&i_this->mActor;
    return 1;
}
