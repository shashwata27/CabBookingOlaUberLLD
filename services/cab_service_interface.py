from abc import ABC,abstractmethod

class CabServiceInterface(ABC):
    @abstractmethod
    def createCab(id,location,driverName):
        pass
    
    @abstractmethod
    def updateCabLocation(cab,location):
        pass
    
    @abstractmethod
    def updateCabIsAvailable(cab,bool):
        pass

    @abstractmethod
    def getCabsWithADistance(location,maxDistance):
        pass
