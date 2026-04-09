class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)   
        rank_map = {}

        for index, value in enumerate(sorted_nums):
            if value not in rank_map:
                rank_map[value] = index
                
        return [rank_map[num] for num in nums]