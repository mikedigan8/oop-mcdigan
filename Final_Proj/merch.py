from inventory import Inventory

class Merch(Inventory):
    def __init__(self, name : str, cost : float, quantity : int, sellPrice : float, inProcess : int = 0):
        super(Merch, self).__init__(name, cost, quantity)
        if sellPrice < 0.0:
            sellPrice = 0.0
        self._sellPrice = sellPrice
        
        if inProcess < 0:
            inProcess = 0
        self._inProcess = inProcess

    @property
    def sellPrice(self) -> float:
        return self._sellPrice

    def setSellPrice(self, newPrice : float) -> None:
        if newPrice < 0.0:
            self._sellPrice = 0.0
        else:
            self._sellPrice = newPrice
    
    @property
    def inProcess(self) -> int:
        return self._inProcess

    def finishGoods(self, amount : int) -> None:
        if amount > self._inProcess:
            amount = self._merchList[name].inProcess
        self._quantity += amount
        self._inProcess -= amount

    def buyMore(self, amount : int) -> None:
        self._inProcess += amount

    def sellGoods(self, amount : int) -> None:
        if amount > self._quantity:
            amount = self._quantity
        self._quantity -= amount

    def getCash(self, amount : int) -> float:
        if amount > self._quantity:
            amount = self._quantity
        return self._cost * amount