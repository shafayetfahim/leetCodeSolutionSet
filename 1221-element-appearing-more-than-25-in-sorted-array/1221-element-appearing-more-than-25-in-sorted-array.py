from collections import Counter
class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        freqMap = Counter(arr)
        return freqMap.most_common(1)[0][0]
        