
from enum import auto,Enum

__MAXIMUM_DISTANCE_A_DRIVER_HAS_TO_TRAVEL__=10
__PRICE_PER_UNIT__=5

class TripStatus(Enum):
    IN_PROGRESS=auto()
    FINISHED=auto()

class CarType(Enum):
    TYPE1=auto()