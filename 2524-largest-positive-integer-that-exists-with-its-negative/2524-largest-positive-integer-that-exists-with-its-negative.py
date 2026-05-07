class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        numsSet = set(nums)
        both = []
        for i in range(len(nums)):
            if (nums[i] * -1) in nums:
                both.append(abs(nums[i]))
        if len(both) == 0: return -1
        return max(both)
        