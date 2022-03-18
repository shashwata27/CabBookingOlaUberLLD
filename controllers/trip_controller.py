from services.trip_service import TripService

class TripController:
    def __init__(self) -> None:
        self.TripServiceInterface=TripService()

    def createTrip(self,id,rider,startLocation,endLocation):
        return self.TripServiceInterface.createTrip(id,rider,startLocation,endLocation)

    def endTrip(self,trip):
        self.TripServiceInterface.endTrip(trip)

    def allTripsByUsers(self,userId):
        return self.TripServiceInterface.allTripsByUsers(userId)