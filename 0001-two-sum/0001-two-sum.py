class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:        
        visited = {}
        for index, value in enumerate(nums):
            goal = target - value
            if goal in visited: return [visited[goal], index]
            else: visited[value] = index

