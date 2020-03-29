#include "CItem.h"
#include "gtest/gtest.h"

using namespace std;
using namespace item;

TEST(CItem, Defaults) {
    CItem citem("Bottle");
    //testing all defaults
    ASSERT_EQ(citem.getName(), "Bottle");
    ASSERT_EQ(citem.getAcquired(), false);
    ASSERT_EQ(citem.getCDirection(), "none");
    ASSERT_EQ(citem.getUsing(), false);

    //testing to make sure you can't assign C direction to a bad location
    CItem citem2("Seeds", true, "up", true);   
    ASSERT_EQ(citem2.getAcquired(),true);
    ASSERT_EQ(citem2.getCDirection(), "none");
    ASSERT_EQ(citem2.getUsing(), false);
    
    //testing that you can set an item to be in use if it's been acquired and assigned to a good location
    CItem citem3("Moon Tear", true, "down", true);
    ASSERT_EQ(citem3.getAcquired(), true);
    ASSERT_EQ(citem3.getCDirection(), "down");
    ASSERT_EQ(citem3.getUsing(),true);
}

TEST(CItem, Setters) {
    CItem citem("Title Deed");

    citem.useItem();
        
    //testing to make sure you can't use an unacquired item
    ASSERT_EQ(citem.getAcquired(),false);
    ASSERT_EQ(citem.getUsing(),false);    

    citem.beenAcquired();
    citem.useItem();    
    
    //testing to make sure you can't use an item that's unassigned
    ASSERT_EQ(citem.getAcquired(), true);
    ASSERT_EQ(citem.getUsing(), false);

    citem.setCDirection("up");
    citem.useItem();
    //testing to make sure you can't use an item assigned to a bad C direction
    //testing to make sure you can't assign an item to a bad C direction
    ASSERT_EQ(citem.getCDirection(), "none");
    ASSERT_EQ(citem.getUsing(),false);

    citem.setCDirection("down");
    citem.useItem();
    //testing to make sure you can assign an item to a good C direction
    //testing to make sure you can use an item that's been aquired and assigned a good C direction
    ASSERT_EQ(citem.getCDirection(), "down");
    ASSERT_EQ(citem.getUsing(), true);

    citem.stopUsing();
    //testing to make sure I can stop using an item
    ASSERT_EQ(citem.getUsing(), false);

    citem.useItem();
    citem.setCDirection("none");
    //testing to make sure an item is no longer in use after taking it off of the C menu
    ASSERT_EQ(citem.getUsing(), false);
}


int main(int args, char** argv) {
    ::testing::InitGoogleTest(&args, argv);
    return RUN_ALL_TESTS();
}