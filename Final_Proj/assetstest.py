import unittest

from assets import Assets

class AssetsTest(unittest.TestCase):
    
    def testInit(self):
        cash = 10000
        AR = 5000
        supplies = 2000
        inventory = 0
        merch = 0
        asset = Assets(cash, AR, supplies, inventory, merch)
        self.assertEqual(asset.cashOnHand, cash)
        self.assertEqual(asset.accountsReceivable, AR)
        self.assertEqual(asset.suppliesOnHand, supplies)
        self.assertEqual(asset.inventoryAccount, inventory)
        self.assertEqual(asset.merchAccount, merch)

    def testInventory(self):
        cash = 10000
        AR = 5000
        supplies = 0
        inventory = 0
        merch = 0
        asset = Assets(cash, AR, supplies, inventory, merch)
        asset.newInventory("Computer", 250, 10)
        asset.newInventory("Chair", 125.50, 30)
        self.assertEqual(asset.cashOnHand, 3735)
        self.assertEqual(asset.inventoryAccount, 6265)
        asset.buyInventory("Computer", 3)
        self.assertEqual(asset.cashOnHand, 2985)
        self.assertEqual(asset.inventoryAccount, 7015)

    def testSupplies(self):
        cash = 10000
        AR = 5000
        supplies = 0
        inventory = 0
        merch = 0
        asset = Assets(cash, AR, supplies, inventory, merch)
        asset.newSupplies("Pens", 4.50, 100)
        asset.newSupplies("Sticky Notes", 3.50, 50)
        self.assertEqual(asset.cashOnHand, 9375)
        self.assertEqual(asset.suppliesOnHand, 625)
        asset.useSupplies("Pens", 75)
        asset.useSupplies("Sticky Notes", 25)
        asset.expenseSupplies("Pens", 50)
        asset.expenseSupplies("Sticky Notes", 25)
        self.assertEqual(asset.suppliesOnHand, 312.50)
        self.assertEqual(asset.cashOnHand, 9375)
        asset.buySupplies("Pens", 20)
        self.assertEqual(asset.cashOnHand, 9285)

    def testMerch(self):
        cash = 10000
        AR = 5000
        supplies = 0
        inventory = 0
        merch = 0
        asset = Assets(cash, AR, supplies, inventory, merch)
        asset.newMerch("Bread", 6.50, 300, 13, 150)
        asset.newMerch("Cookies", 2.75, 250, 7, 100)
        self.assertEqual(asset.cashOnHand, 7362.5)
        self.assertEqual(asset.merchAccount, 2637.5)
        asset.sellMerchOnCash("Bread", 100)
        asset.sellMerchOnCash("Cookies", 100)
        self.assertEqual(asset.cashOnHand, 9362.5)
        self.assertEqual(asset.merchAccount, 1712.5)
        asset.toFinishedGoods("Bread", 100)
        asset.toFinishedGoods("Cookies", 75)
        asset.sellMerchOnCred("Bread", 100)
        asset.sellMerchOnCash("Cookies", 75)
        self.assertEqual(asset.cashOnHand, 9887.5)
        self.assertEqual(asset.accountsReceivable, 6300)
        self.assertEqual(asset.merchAccount, 856.25)
        asset.collectAccRec(1000)
        self.assertEqual(asset.cashOnHand, 10887.5)
        self.assertEqual(asset.accountsReceivable, 5300)
        asset.newSellPrice("Bread", 15)
        asset.buyMerch("Bread", 300)
        asset.buyMerch("Cookies", 200)
        self.assertEqual(asset.cashOnHand, 8387.5)
        self.assertEqual(asset.merchAccount, 3356.25)
        asset.toFinishedGoods("Bread", 150)
        asset.sellMerchOnCash("Bread", 100)
        self.assertEqual(asset.cashOnHand, 9887.5)
        self.assertEqual(asset.merchAccount, 2706.25)