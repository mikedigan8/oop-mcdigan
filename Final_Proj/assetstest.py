import unittest

from assets import Assets

class AssetsTest(unittest.TestCase):
    
    def testInit(self):
        cash = 10000
        AR = 5000
        supplies = 2000
        asset = Assets(cash, AR, supplies)
        self.assertEqual(asset.cashOnHand, cash)
        self.assertEqual(asset.accountsReceivable, AR)
        self.assertEqual(asset.suppliesOnHand, supplies)