#include "Mask.h"
#include "gtest/gtest.h"
#include <iostream>

using namespace std;
using namespace item;

TEST(Mask, Defaults) {
    Mask mask("Deku Mask","Turns Link into a Deku shurb");
    ASSERT_EQ(mask.getName(),"Deku Mask");
    ASSERT_EQ(mask.getProperties(),"Turns Link into a Deku shurb");
    ASSERT_EQ(mask.getIsOn(),false);
    ASSERT_EQ(mask.getAcquired(),false);
    ASSERT_EQ(mask.getCDirection(),"none");
    ASSERT_EQ(mask.getUsing(),false);
}

TEST(Mask, Setters) {
    
    Mask mask("Goron Mask","Turns Link into a Goron");

    //test to make sure I can't wear a mask if it's not aquired
    mask.putOn();
    ASSERT_EQ(mask.getIsOn(),false);

    mask.beenAcquired();
    //still can't wear because I haven't applied it to a C direction
    ASSERT_EQ(mask.getIsOn(), false);

    mask.setCDirection("down");
    //still can't wear because it is not in use
    ASSERT_EQ(mask.getIsOn(),false);

    mask.useItem();
    //test to make sure I can use it once it's acquired, applied, and in use        
    mask.putOn();
    ASSERT_EQ(mask.getIsOn(),true);

    //if I take the mask off it's not on
    mask.takeOff();
    ASSERT_EQ(mask.getIsOn(),false);

    //if I stop using the mask it is off
    mask.putOn();
    mask.stopUsing();
    ASSERT_EQ(mask.getIsOn(),false);

    //if I unassign the mask from a C direction it is no longer on
    mask.useItem();
    mask.putOn();
    mask.setCDirection("none");
    ASSERT_EQ(mask.getIsOn(),false);
}

int main(int args, char** argv) {
    ::testing::InitGoogleTest(&args, argv);
    return RUN_ALL_TESTS();
}