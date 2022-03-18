from models.rider import Rider
from services.rider_service_interface import RiderServiceInterface

class RiderService(RiderServiceInterface):
    riders={}
    @staticmethod
    def createRider(id,name):
        rider=Rider(id,name)
        RiderService.riders[id]=rider
        return rider
    