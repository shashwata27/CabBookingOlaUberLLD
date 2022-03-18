from services.location_service import LocationService

class LocationController:
    def __init__(self) -> None:
        self.LocationServiceInterface=LocationService()
    def createLocation(self,x,y):
        return self.LocationServiceInterface.createLocation(x,y)
