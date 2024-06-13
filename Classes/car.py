from abc import ABC

#Note, even if a part is serviced, its important only that part gets the service date / milage, otherwise there is the 
#potential of a false positive, ie in the case the engine was just serviced and now the battery should be serviced, but 
#is given an exception.
class Car(ABC):
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery

    
    def needs_service(self):
        return self.battery.needs_service() or self.engine.needs_service()
