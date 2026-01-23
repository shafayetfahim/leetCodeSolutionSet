class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        longest, temp = 0, 0
        for num in nums:
            if num == 1: 
                temp += 1
                longest = max(longest, temp)
            elif num == 0: temp = 0
        return longest