class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = (list(sorted(set(nums))))[::-1]
        if len(nums) < 3: return max(nums)
        else: return nums[2]
