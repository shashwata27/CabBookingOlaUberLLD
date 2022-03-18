from models.cab import Cab
from services.location_service import LocationService
from services.cab_service_interface import CabServiceInterface

class CabService(CabServiceInterface):
    cabs={}
    @staticmethod
    def createCab(id,location,driverName):
        cab=Cab(id,location,driverName)
        CabService.cabs[id]=cab
        return cab
        
    
    @staticmethod
    def updateCabLocation(cab,location):
        cab.setLocation(location)
    
    @staticmethod
    def updateCabIsAvailable(cab,bol):
        cab.setIsAvailable(bol)

    @staticmethod
    def getCabsWithADistance(location,maxDistance):
        closeByCabs=[]
        for cab in CabService.cabs.values():
            cabLocation=cab.getLocation()
            if LocationService.distance(cabLocation,location)<=maxDistance:
                closeByCabs.append(cab)

        return closeByCabs