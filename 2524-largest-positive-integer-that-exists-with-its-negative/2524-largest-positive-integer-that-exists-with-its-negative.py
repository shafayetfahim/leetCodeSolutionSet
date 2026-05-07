class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        numsSet = set(nums)
        both = set()
        for i in range(len(nums)):
            if (nums[i] * -1) in nums:
                both.add(abs(nums[i]))
        if len(both) == 0: return -1
        return max(both)
        