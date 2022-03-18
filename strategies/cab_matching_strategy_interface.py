from abc import ABC,abstractmethod

class CabMatchingStrategyInterface(ABC):
    @abstractmethod
    def matchCab(closeByCabs):
        pass
    