class Solution:
    def minElement(self, nums: List[int]) -> int:
        minimum = 100000
        for i in range(len(nums)):
            nums[i] = sum(list(map(int, str(nums[i]))))
            minimum = min(nums[i], minimum)
        
        return minimum
            
        