from cmath import sqrt
from models.location import Location
from services.location_service_interface import LocationServiceInterface

class LocationService(LocationServiceInterface):
    @staticmethod
    def createLocation(x,y):
        return Location(x,y)
    
    @staticmethod
    def distance(LocationA,locationB):
        distance=((LocationA.getX()-locationB.getX())**2+(LocationA.getY()-locationB.getY())**2)**(1/2)
        return distance
