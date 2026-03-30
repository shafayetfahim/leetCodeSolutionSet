class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]
        for num in nums:
            new_subsets = [current_subset + [num] for current_subset in result]
            result.extend(new_subsets)            
        return result