from strategies.pricing_strategy_interface import PricingStrategyInterface
import constants.constants as cons
from services.location_service import LocationService

class PricingStrategy(PricingStrategyInterface):
    @staticmethod
    def generatePrice(startLocation,endLocation):
        distance=LocationService.distance(startLocation,endLocation)
        return distance* cons.__PRICE_PER_UNIT__
    