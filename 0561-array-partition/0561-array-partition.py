class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        if len(nums) < 4: return min(nums)
        n = len(nums)//2
        total = 0

        nums = sorted(nums, reverse=True)
        for i in range(n):
            max_min = min(nums[(i*2):(i*2)+2])
            print(max_min)
            total += max_min

        return total