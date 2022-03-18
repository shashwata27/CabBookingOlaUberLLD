from abc import ABC,abstractmethod

class LocationServiceInterface(ABC):
    @abstractmethod
    def createLocation(x,y):
        pass
    
    @abstractmethod
    def distance(locationA,locationB):
        pass
