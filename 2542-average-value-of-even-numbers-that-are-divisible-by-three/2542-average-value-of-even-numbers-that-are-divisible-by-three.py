class Solution:
    def averageValue(self, nums: List[int]) -> int:
        numSum, count = 0, 0
        for i in range(len(nums)):
            if nums[i]%6 == 0:
                numSum += nums[i]
                count += 1
        if count > 0: return numSum//count
        return 0
        