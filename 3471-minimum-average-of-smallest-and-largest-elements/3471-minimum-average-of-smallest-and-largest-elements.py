class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums = sorted(nums)
        n = len(nums)//2
        left, right = 0, (n*2-1)
        averages = 51
        while left < n:
            op = (nums[left] + nums[right]) / 2
            averages = min(averages, op)
            left += 1
            right -= 1
        return averages
            

            

        