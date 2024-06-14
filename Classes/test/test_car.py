import unittest
from datetime import datetime

from ..CarParts import *
import car
#Naming convention out window

class TestEngine(unittest.TestCase):
    def test_sternman_engine_should_be_serviced(self):
        

        Engine = SternmanEngine(True)
        self.assertTrue(Engine.needs_service())
        
    def test_sternman_engine_should_not_be_serviced(self):

        Engine = SternmanEngine(False)
        self.assertFalse(Engine.needs_service())

    def test_capulet_engine_should_be_serviced(self):
        current_mileage = 80000
        last_service_mileage = 40000

        Engine = CapuletEngine(last_service_mileage, current_mileage)
        self.assertTrue(Engine.needs_service())

    def test_capulet_engine_should_not_be_serviced(self):
        current_mileage = 40000
        last_service_mileage = 40000

        Engine = CapuletEngine(last_service_mileage, current_mileage)
        self.assertFalse(Engine.needs_service())

    def test_willoughby_engine_should_be_serviced(self):
        current_mileage = 120000
        last_service_mileage = 40000

        Engine = CapuletEngine(last_service_mileage, current_mileage)
        self.assertTrue(Engine.needs_service())

    def test_willoughby_engine_should_be_not_serviced(self):
        current_mileage = 70000
        last_service_mileage = 60000

        Engine = CapuletEngine(last_service_mileage, current_mileage)
        self.assertFalse(Engine.needs_service())

    





class TestBattery(unittest.TestCase):
    def test_nubbin_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)
        

        Battery = NubbinBattery(last_service_date, today)
        self.assertTrue(Battery.needs_service())

    def test_spindler_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        

        Battery = SpindlerBattery(last_service_date, today)
        self.assertTrue(Battery.needs_service())

    def test_nubbin_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 2)
       

        Battery = NubbinBattery(last_service_date, today)
        self.assertFalse(Battery.needs_service())

    def test_spindler_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)
        

        Battery = SpindlerBattery(last_service_date, today)
        self.assertFalse(Battery.needs_service())