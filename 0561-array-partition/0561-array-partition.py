class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        if len(nums) < 4: return min(nums)
        total = 0

        nums = sorted(nums, reverse=True)
        for i in range(len(nums)//2):
            index = i*2
            total += min(nums[(index):(index)+2])
        return total