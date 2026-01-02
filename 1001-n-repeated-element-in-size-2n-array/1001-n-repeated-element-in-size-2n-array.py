from collections import Counter
class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        n = len(nums)//2
        counts = Counter(nums)
        return next(item for item, count in counts.items() if count == n)