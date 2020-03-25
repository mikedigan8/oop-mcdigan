from typing import List

class CItem:
    ACCEPTABLE_DIRECTIONS: List[str] = ["left", "right", "down", "none"]

    def __init__(self, name: str, acquired: bool = False, cApplied: str = "none", inUse: bool = False):
        self._name = name
        self._acquired = acquired
        if cApplied not in self.ACCEPTABLE_DIRECTIONS or self._acquired == False:
            self._cApplied = "none"
        else:
            self._cApplied = cApplied
        if self._cApplied == "none":
            self._inUse = False
        else:
            self._inUse = inUse
    
    @property
    def name(self) -> str:
        return self._name

    @property
    def acquired(self) -> bool:
        return self._acquired

    def beenAcquired(self) -> None:
        self._acquired = True
    
    @property
    def cApplied(self) -> str:
        return self._cApplied

    def applyC(self, newDirect: str) -> None:
        if newDirect not in self.ACCEPTABLE_DIRECTIONS or self._acquired == False:
            self._cApplied = "none"
        else:
            self._cApplied = newDirect
        if self._cApplied == "none":
            self._inUse = False

    @property
    def inUse(self) -> bool:
        return self._inUse
    
    def using(self) -> None:
        if self._cApplied != "none":
            self._inUse = True

    def stopUsing(self) -> None:
        self._inUse = False