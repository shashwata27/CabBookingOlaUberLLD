from services.rider_service import RiderService

class RiderController:
    def __init__(self) -> None:
        self.RiderServiceInterface=RiderService()

    def registerRider(self,id,name):
        return self.RiderServiceInterface.createRider(id,name)
