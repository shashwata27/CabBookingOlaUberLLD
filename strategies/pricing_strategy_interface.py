from abc import ABC,abstractmethod

class PricingStrategyInterface(ABC):
    @abstractmethod
    def generatePrice(startLocation,endLocation):
        pass
    