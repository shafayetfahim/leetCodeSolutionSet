import statistics
class Solution:
    def trimMean(self, arr: List[int]) -> float:
        trimSize = int(0.05*len(arr))
        return statistics.mean(sorted(arr)[trimSize:len(arr)-trimSize:])