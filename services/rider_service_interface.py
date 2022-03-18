from abc import ABC,abstractmethod

class RiderServiceInterface(ABC):
    @abstractmethod
    def createRider(id,name):
        pass
    