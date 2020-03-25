import unittest

from citem import CItem
from mask import Mask
from weapon import Weapon
from typing import List

class CItemTest(unittest.TestCase):

    def testInitializer(self):
        citem = CItem("Bottle")
        #testing all defaults
        self.assertEqual(citem.name, "Bottle")
        self.assertEqual(citem.acquired, False)
        self.assertEqual(citem.cApplied, "none")
        self.assertEqual(citem.inUse, False)

        #testing to make sure you can't assign C direction to a bad location
        citem2 = CItem("Seeds",True,"up",True)
        self.assertEqual(citem2.acquired, True)
        self.assertEqual(citem2.cApplied, "none")
        self.assertEqual(citem2.inUse, False)

        #testing that you can set an item to be in use if it's been acquired and assigned to a good location
        citem3 = CItem("Moon Tear",True, "down", True)
        self.assertEqual(citem3.acquired, True)
        self.assertEqual(citem3.cApplied, "down")
        self.assertEqual(citem3.inUse, True)   

    def testSetters(self):
        citem = CItem("Title Deed")
        citem.using()
        
        #testing to make sure you can't use an unacquired item
        self.assertEqual(citem.acquired, False)
        self.assertEqual(citem.inUse, False)

        citem.beenAcquired()
        citem.using()
        #testing to make sure you can't use an item that's unassigned
        self.assertEqual(citem.acquired, True)
        self.assertEqual(citem.inUse, False)

        citem.applyC("up")
        citem.using()
        #testing to make sure you can't use an item assigned to a bad C direction
        #testing to make sure you can't assign an item to a bad C direction
        self.assertEqual(citem.cApplied, "none")
        self.assertEqual(citem.inUse, False)

        citem.applyC("down")
        citem.using()
        #testing to make sure you can assign an item to a good C direction
        #testing to make sure you can use an item that's been aquired and assigned a good C direction
        self.assertEqual(citem.cApplied, "down")
        self.assertEqual(citem.inUse, True)

        citem.stopUsing()
        #testing to make sure I can stop using an item
        self.assertEqual(citem.inUse, False)

        citem.using()
        citem.applyC("none")
        #testing to make sure an item is no longer in use after taking it off of the C menu
        self.assertEqual(citem.inUse, False)


