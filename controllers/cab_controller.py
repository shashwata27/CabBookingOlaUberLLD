from services.cab_service import CabService

class CabController:
    def __init__(self) -> None:
        self.CabServiceInterface=CabService()

    def registerCab(self,id,location,driverName):
        return self.CabServiceInterface.createCab(id,location,driverName)

    def updateLocation(self,cab,location):
        self.CabServiceInterface.updateCabLocation(cab,location)

    def updateCabAvaibility(self,cab,state):
        self.CabServiceInterface.updateCabIsAvailable(cab,state)