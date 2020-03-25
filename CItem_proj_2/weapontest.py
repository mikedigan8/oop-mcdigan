import unittest

from citem import CItem
from weapon import Weapon

class WeaponTest(unittest.TestCase):

    def testDefaults(self):
        weapon = Weapon("Bow")
        self.assertEqual(weapon.name,"Bow")
        self.assertEqual(weapon.bagSize,weapon.DEFAULT_BAG_SIZE)
        self.assertEqual(weapon.quantity, weapon.DEFAULT_QUANTITY)
        self.assertEqual(weapon.acquired,False)
        self.assertEqual(weapon.cApplied,"none")
        self.assertEqual(weapon.inUse,False)

        weapon2 = Weapon("Slingshot",50,30)
        self.assertEqual(weapon2.bagSize,50)
        self.assertEqual(weapon2.quantity,30)

        weapon3 = Weapon("Bomb Bag",30,50)
        self.assertEqual(weapon3.bagSize,30)
        self.assertEqual(weapon3.quantity,30)

    def testSetters(self):
        weapon = Weapon("Bombchu")

        #change the size of the bag
        new_bag_size = 40
        weapon.icreaseBag(new_bag_size)
        self.assertEqual(weapon.bagSize,new_bag_size)

        #make sure I can't overfill the bag
        weapon.refill(50)
        self.assertEqual(weapon.quantity, new_bag_size)

        #I should not be able to fire unless I have aquired the weapon, it has been assigned a C direction, and it is in use
        weapon.fire()
        self.assertEqual(weapon.quantity, new_bag_size)

        #the quantity should decrease when it's fired
        weapon.beenAcquired()
        weapon.applyC("right")
        weapon.using()
        for i in range(10):
            weapon.fire()
        self.assertEqual(weapon.quantity,new_bag_size - 10)

        #the quantity cannot go below zero
        for i in range(50):
            weapon.fire()
        self.assertEqual(weapon.quantity,0)