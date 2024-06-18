from abc import ABC

from Tires import Tires


class OctoprimeTires(Tires, ABC):
    def __init__(self, tireData):
        self.tireData = tireData
        #store in own array

    def needs_service(self):
        for x in self.tireData:
            result += x
        
        #Add values, compare, done
        return result > 3