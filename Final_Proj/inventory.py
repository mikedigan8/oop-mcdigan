class Inventory:

    def __init__(self, name : str, cost : float, quantity : int):
        self._name = name
        if cost < 0:
            self._cost = 0
        else:
            self._cost = cost
        if quantity < 0:
            self._quantity = 0
        else:
            self._quantity = quantity

    @property
    def name(self) -> str:
        return self._name
    
    @property
    def cost(self) -> float:
        return self._cost

    @property
    def quantity(self) -> int:
        return self._quantity

    def buyMore(self, amount : int) -> None:
        self._quantity += amount
