from inventory import Inventory

class Supplies(Inventory):
    def __init__(self, name : str,  cost : float, quantity : int, using : int = 0):
        super(Supplies,self).__init__(name, cost, quantity)
        if using > quantity:
            using = quantity
        self._using = using
        self._available = self._quantity - self._using
    @property
    def using(self) -> int:
        return self._using

    @property
    def available(self) -> int:
        return self._available

    def startUsing(self, amount : int) -> None:
        if amount > self._available:
            amount = self._available
        self._using += amount
        self._available -= amount

    def expense(self, amount : int) -> None:
        if amount > self._using:
            amount = self._using
        self._using -= amount

    def getExpense(self, amount : int) -> float:
        if amount > self._using:
            amount = self._using
        return self._cost * amount