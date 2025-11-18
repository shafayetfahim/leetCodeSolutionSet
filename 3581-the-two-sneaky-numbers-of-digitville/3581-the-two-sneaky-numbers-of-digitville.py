from collections import Counter
class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        freqMap = Counter(nums)
        return [k for k, v in sorted(freqMap.items(), key=lambda x: x[1], reverse=True)[:2]]
        