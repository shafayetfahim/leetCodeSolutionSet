from collections import Counter
class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        nums = [i for i in nums if i % 2 == 0]
        freq_map = Counter(nums)
        if freq_map:
            max_freq = max(freq_map.values())
            highest_keys = [k for k, v in freq_map.items() if v == max_freq]
        else: return -1
        return min(highest_keys)
        
        