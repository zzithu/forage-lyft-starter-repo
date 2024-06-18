from abc import ABC

from Tires import Tires


class CarriganTires(Tires, ABC):
    def __init__(self, tireData):
        self.tireData = tireData

    def needs_service(self):
        for x in self.tireData:
            if(x > .9):
                return True
        
        return False