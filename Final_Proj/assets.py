from inventory import Inventory
from supplies import Supplies
from merch import Merch

class Assets:
    def __init__(self, cash : float, accRec : float, supplies : float):
        if cash < 0.0:
            cash = 0.0
        self._cash = cash
        if accRec < 0.0:
            accRec = 0.0
        self._accRec = accRec
        if supplies < 0.0:
            supplies = 0.0
        self._supplies = supplies

        self._inventoryList = {}
        self._suppliesList = {}
        self._merchList = {}
    
    @property 
    def cashOnHand(self) -> float:
        return self._cash

    @property
    def accountsReceivable(self) -> float:
        return self._accRec

    @property
    def suppliesOnHand(self) -> float:
        return self._supplies

    def newInventory(self, name : str, cost : float, quantity : int) -> None:
        if name not in self._inventoryList:
            self._inventoryList.update({name : Inventory(name, cost, quantity)})
            self._cash -= cost * quantity

    def newSupplies(self, name : str, cost : float, quantity : int, using : int = 0) -> None:
        if name not in self._suppliesList:
            self._cash -= cost * quantity
            self._suppliesList.update({name : Supplies(name, cost, quantity, using)})
            self._supplies += cost * quantity

    def newMerch(self, name : str, cost : float, quantity : int, sellPrice : float, inProcess : int = 0) -> None:
        if name not in self._merchList:
            self._cash -= cost * quantity
            self._merchList.update({name : Merch(name, cost, quantity, sellPrice, inProcess)})

    def buyInventory(self, name : str, quantity : int) -> None:
        if quantity > 0:
            self._inventoryList[name].buyMore(quantity)
            self._cash -= self._inventoryList[name].cost * quantity

    def useSupplies(self, name : str, quantity : int) -> None:
        self._suppliesList[name].startUsing(quantity)

    def buySupplies(self, name : str, quantity : int) -> None:
        if quantity > 0:
            self._suppliesList[name].buyMore(quantity)
            self._cash -= self._suppliesList[name].cost * quantity

    def buyMerch(self, name : str, quantity : int) -> None:
        if quantity > 0:
            self._merchList[name].buyMore(quantity)
            self._cash -= self._merchList[name].cost * quantity

    def newSellPrice(self, name : str, price : float) -> None:
        self._merchList[name].setSellPrice(price)

    def expenseSupplies(self, name : str, amount : int) -> None:
        self._supplies -= self._suppliesList[name].getExpense(amount)
        self._suppliesList[name].expense(amount)

    def toFinishedGoods(self, name : str, amount : int) -> None:
        self._merchList[name].finishGoods(amount)

    def sellMerchOnCash(self, name : str, amount : int) -> None:
        self._cash += self._merchList[name].getCash(amount)
        self._merchList[name].sellGoods(amount)

    def sellMerchOnCred(self, name : str, amount : int) -> None:
        self._accRec += self._merchList[name].getCash(amount)
        self._merchList[name].sellGoods(amount)

    def collectAccRec(self, amount : float) -> None:
        if amount > self._accRec:
            amount = self._accRec
        self._cash += amount
        self._accRec -= amount