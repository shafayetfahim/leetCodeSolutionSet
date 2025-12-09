class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        output = [0]*len(nums)
        nums_sum = 0
        for i in range(len(nums)):
            nums_sum += nums[i]
            output[i] = nums_sum
        return output
        