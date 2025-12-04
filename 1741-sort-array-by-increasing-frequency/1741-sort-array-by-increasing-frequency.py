from collections import Counter
class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freqMap = Counter(nums)
        return sorted(nums, key=lambda x: (freqMap[x], -x))
            
        