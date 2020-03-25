from citem import CItem
from typing import List

class Mask(CItem):
    def __init__(self, name: str, properties: str, isOn: bool = False):
        super(Mask,self).__init__(name)
        self._properties = properties
        if self._inUse == False:
            self._isOn = False
        else:
            self._isOn = isOn

    @property
    def isOn(self) -> bool:
        return self._isOn

    def putOn(self) -> None:
        if self._inUse == True:
            self._isOn = True
    
    def takeOff(self) -> None:
        self._isOn = False

    @property
    def properties(self) -> str:
        return self._properties

    def stopUsing(self) -> None:
        self._inUse = False   
        self._isOn = False 

    def applyC(self, newDirect: str) -> None:
        if newDirect not in self.ACCEPTABLE_DIRECTIONS or self._acquired == False:
            self._cApplied = "none"
        else:
            self._cApplied = newDirect
        if self._cApplied == "none":
            self._inUse = False
            self._isOn = False