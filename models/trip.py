from constants.constants import TripStatus
class Trip:
    def __init__(self,id,rider,startLocation,endLocation,tripStatus=TripStatus.IN_PROGRESS,cab=None,price=None) -> None:
        self.id=id
        self.rider=rider
        self.startLocation=startLocation
        self.endLocation=endLocation
        self.tripStatus=tripStatus
        self.cab=cab
        self.price=price

    def __str__(self) -> str:
        return f'{self.rider.name} rides with {self.cab.driverName} with price {self.price} and trip is still {self.tripStatus}'


    def getId(self):
        return self.id
    def setId(self,id):
        self.id=id

    def getRider(self):
        return self.rider
    def setRider(self,rider):
        self.rider=rider

    def getStartLocation(self):
        return self.startlocation
    def setStartLocation(self,startlocation):
        self.startlocation=startlocation

    def getEndLocation(self):
        return self.endlocation
    def setEndLocation(self,endlocation):
        self.endlocation=endlocation

    def getTripStatus(self):
        return self.tripStatus
    def setTripStatus(self,tripStatus):
        self.tripStatus=tripStatus

    def getCab(self):
        return self.cab
    def setCab(self,cab):
        self.cab=cab

    def getPrice(self):
        return self.price
    def setPrice(self,price):
        self.price=price