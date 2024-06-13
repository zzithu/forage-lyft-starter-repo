from abc import ABC

from abc import abstractmethod


class Battery:
    
    @abstractmethod
    def needs_service(self):
        print("Generic Battery, Service Unknown")
        return True