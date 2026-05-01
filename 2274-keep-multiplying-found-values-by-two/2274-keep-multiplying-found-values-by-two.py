class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        nums_set = set(nums)
        for i in range(len(nums)):
            if original in nums_set: 
                original *= 2
                i = 0
        return original
        