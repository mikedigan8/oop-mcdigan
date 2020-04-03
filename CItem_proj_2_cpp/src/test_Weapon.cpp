#include "Weapon.h"
#include "gtest/gtest.h"

using namespace std;
using namespace item;

TEST(Weapon, Defaults) {
    Weapon weapon("Bow");
    ASSERT_EQ(weapon.getName(),"Bow");
    ASSERT_EQ(weapon.getBagSize(),Weapon::DEFAULT_BAG_SIZE);
    ASSERT_EQ(weapon.getQuantity(),Weapon::DEFAULT_QUANTITY);
    ASSERT_EQ(weapon.getAcquired(),false);
    ASSERT_EQ(weapon.getCDirection(),"none");
    ASSERT_EQ(weapon.getUsing(),false);
    
    Weapon weapon2("Slingshot",50,30);
    ASSERT_EQ(weapon2.getBagSize(),50);
    ASSERT_EQ(weapon2.getQuantity(),30);
    
    Weapon weapon3("Bomb Bag",30,50);
    ASSERT_EQ(weapon3.getBagSize(),30);
    ASSERT_EQ(weapon3.getQuantity(),30);
}

TEST(Weapon, Setters) {
    Weapon weapon("Bombchu");
    
    //change the size of the bag
    int new_bag_size = 40;
    weapon.setBagSize(new_bag_size);
    ASSERT_EQ(weapon.getBagSize(),new_bag_size);
    
    //make sure I can't overfill the bag
    weapon.setQuantity(50);
    ASSERT_EQ(weapon.getQuantity(),new_bag_size);
    
    //I should not be able to fire unless I have aquired the weapon, it has been assigned a C direction, and it is in use
    weapon.fire();
    ASSERT_EQ(weapon.getQuantity(),new_bag_size);
    
    //the quantity should decrease when it's fired
    weapon.beenAcquired();
    weapon.setCDirection("right");
    weapon.useItem();
    for(int i = 0; i < 10; i++) weapon.fire();
    ASSERT_EQ(weapon.getQuantity(),new_bag_size - 10);

    //the quantity cannot go below zero
    for(int i = 0; i < 50; i++) weapon.fire();
    ASSERT_EQ(weapon.getQuantity(),0);
}

int main(int args, char** argv) {
    ::testing::InitGoogleTest(&args, argv);
    return RUN_ALL_TESTS();
}