from .CarParts import *
import car
#May want to change for efficiency sake, but all imports :>

#consider adding some unique identifier, this will work I hope
class CarFactory:
    cars = {}

    def create_calliope(self, current_date, last_service_date, current_mileage, last_service_milage):
        self.cars.append(car(CapuletEngine(current_mileage, last_service_milage), SpindlerBattery(last_service_date, current_date)))
    
    def create_Glissade(self, current_date, last_service_date, current_mileage, last_service_milage):
        self.cars.append(car(WilloughbyEngine(current_mileage, last_service_milage), SpindlerBattery(last_service_date, current_date)))

    def create_Palindrome(self, current_date, last_service_date, warning_light_on):
        self.cars.append(car(SternmanEngine(warning_light_on), SpindlerBattery(last_service_date, current_date)))

    def create_Rorschach(self, current_date, last_service_date, current_mileage, last_service_milage):
        self.cars.append(car(WilloughbyEngine(current_mileage, last_service_milage), NubbinBattery(last_service_date, current_date)))

    def create_Thovex(self, current_date, last_service_date, current_mileage, last_service_milage):
        self.cars.append(car(CapuletEngine(current_mileage, last_service_milage), NubbinBattery(last_service_date, current_date)))    
    
    
    