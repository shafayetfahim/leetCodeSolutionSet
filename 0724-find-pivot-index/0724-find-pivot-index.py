class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix_sum, subtotal = 0, sum(nums)
        for i in range(len(nums)):
            prefix_sum += nums[i]
            if prefix_sum == subtotal: return i
            else: subtotal -= nums[i]
            print(f"({prefix_sum}, {subtotal})")
        return -1
        
        '''
        Process
        nums = [1,7,3,6,5,6]
        At index 1:
        l_sum, r_sum = 1, 28
        At index 2:
        l_sum, r_sum = 1+
        '''