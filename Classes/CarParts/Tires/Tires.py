from abc import ABC, abstractmethod


class Tires:
    @abstractmethod
    def needs_service():
        print("Generic Tires, Unknown Service")
        return True
