class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        maximum = 0
        nums = sorted(nums)

        for i in range(len(nums)-1):
            gap = abs(nums[i]-nums[i+1])
            if gap > maximum: maximum = gap

        return maximum
            

            
        