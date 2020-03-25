import unittest

from citem import CItem
from mask import Mask

class MaskTest(unittest.TestCase):

    def testDefaults(self):
        mask = Mask("Deku Mask","Turns Link into a Deku shrub",True)
        self.assertEqual(mask.name,"Deku Mask")
        self.assertEqual(mask.properties,"Turns Link into a Deku shrub")
        self.assertEqual(mask.isOn, False)
        self.assertEqual(mask.acquired,False)
        self.assertEqual(mask.cApplied,"none")
        self.assertEqual(mask.inUse,False)

    def testSetters(self):
        mask = Mask("Goron Mask","Turns Link into a Goron")

        #test to make sure I can't wear a mask if it's not aquired
        mask.putOn()
        self.assertEqual(mask.isOn,False)

        mask.beenAcquired()
        #still can't wear because I haven't applied it to a C direction
        self.assertEqual(mask.isOn,False)

        mask.applyC("down")
        #still can't wear because it is not in use
        self.assertEqual(mask.isOn,False)
        
        mask.using()
        #test to make sure I can use it once it's acquired, applied, and in use        
        mask.putOn()
        self.assertEqual(mask.isOn,True)

        #if I take the mask off it's not on
        mask.takeOff()
        self.assertEqual(mask.isOn,False)

        #if I stop using the mask it is off
        mask.putOn()
        mask.stopUsing()
        self.assertEqual(mask.isOn,False)

        #if I unassign the mask from a C direction it is no longer on
        mask.using()
        mask.putOn()
        mask.applyC("none")
        self.assertEqual(mask.isOn,False)


