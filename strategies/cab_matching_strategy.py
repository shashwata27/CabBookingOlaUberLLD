from strategies.cab_matching_strategy_interface import CabMatchingStrategyInterface

class CabMatchingStrategy(CabMatchingStrategyInterface):
    @staticmethod
    def matchCab(closeByCabs):
        for cab in closeByCabs:
            if cab.getIsAvailable():
                return cab

    