class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        theSum = 0
        for i in range(len(nums)):
            if i%2 == 0: temp = 1
            else: temp = -1
            theSum += (temp * nums[i])
        return theSum

        