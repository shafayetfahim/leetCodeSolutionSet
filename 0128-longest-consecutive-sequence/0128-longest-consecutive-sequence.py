class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        nums = set(nums)
        starts = {}
        for num in nums:
            if num-1 not in nums: starts[num] = 0

        for start in starts:
            i = start
            while i in nums: 
                starts[start] += 1
                i += 1
        
        return max(starts.values())
        