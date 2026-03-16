class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        nums_sorted = sorted(nums)[::-1]
        if nums_sorted[0] >= 2*nums_sorted[1]: return nums.index(nums_sorted[0])
        else: return -1
        