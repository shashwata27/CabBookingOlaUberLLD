from abc import ABC,abstractmethod

class TripServiceInterface(ABC):
    @abstractmethod
    def createTrip(id,rider,startLocation,endLocation):
        pass
    
    @abstractmethod
    def endTrip(trip):
        pass

    @abstractmethod
    def allTripsByUsers(userId):
        pass
    
