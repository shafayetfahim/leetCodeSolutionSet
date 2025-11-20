class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        theSum = 0
        operator = 1
        for num in nums:
            theSum += (operator * num)
            operator *= -1
        return theSum

        