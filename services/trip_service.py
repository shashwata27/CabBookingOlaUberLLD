from models.trip import Trip
import constants.constants as cons 
from services.trip_service_interface import TripServiceInterface

from strategies.cab_matching_strategy import CabMatchingStrategy
from strategies.pricing_strategy import PricingStrategy

from services.cab_service import CabService


class TripService(TripServiceInterface):
    trips={}

    @staticmethod
    def createTrip(id,rider,startLocation,endLocation):
        trip=Trip(id,rider,startLocation,endLocation)

        #strageties
        closeByCabs=CabService.getCabsWithADistance(startLocation,cons.__MAXIMUM_DISTANCE_A_DRIVER_HAS_TO_TRAVEL__)

        selectedCab=CabMatchingStrategy.matchCab(closeByCabs)
        CabService.updateCabIsAvailable(selectedCab,False)

        totalPrice=PricingStrategy.generatePrice(startLocation,endLocation)

        trip.setCab(selectedCab)
        trip.setPrice(totalPrice)


        riderID=trip.rider.getId()
        if riderID not in TripService.trips.keys():
            TripService.trips[riderID]=[trip]
        else:
            TripService.trips[riderID].append(trip)

        return trip
    
    @staticmethod
    def endTrip(trip):
        CabService.updateCabIsAvailable(trip.getCab(),True)
        trip.setTripStatus(cons.TripStatus.FINISHED)

    @staticmethod
    def allTripsByUsers(userId):
        return TripService.trips[userId]
    
