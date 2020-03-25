from citem import CItem
from typing import List

class Weapon(CItem):
    DEFAULT_BAG_SIZE: int = 20
    DEFAULT_QUANTITY: int = 0
    def __init__(self, name: str, bagSize: int = DEFAULT_BAG_SIZE, quantity: int = DEFAULT_QUANTITY):
        super(Weapon,self).__init__(name)
        self._bagSize = bagSize
        if quantity > bagSize:
            self._quantity = self._bagSize
        else:
            self._quantity = quantity
    
    @property
    def bagSize(self) -> int:
        return self._bagSize

    def icreaseBag(self, newBag) -> None:
        self._bagSize = newBag

    @property
    def quantity(self) -> int:
        return self._quantity

    def fire(self) -> None:
        if self._inUse and self._quantity > 0:
            self._quantity -= 1
    
    def refill(self, amount: int) -> None:
        if self._quantity + amount > self._bagSize:
            self._quantity = self._bagSize
        else:
            self._quantity += amount
        