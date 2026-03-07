import math
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        all_pos = nums[-1] * nums[-2] * nums[-3]
        two_neg = nums[0] * nums[1] * nums[-1]
        return max(all_pos, two_neg)