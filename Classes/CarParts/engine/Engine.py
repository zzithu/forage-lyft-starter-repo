from abc import ABC, abstractmethod
#I don't fully understand this?  >  update I now understand.

class Engine:
    @abstractmethod
    def needs_service():
        print("Generic Engine, Unknown Service")
        return True
