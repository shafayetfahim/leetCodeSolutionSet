class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights)-1
        maximum = 0
        while left < right:
            smaller = min(heights[left], heights[right])
            container = (right-left) * smaller
            maximum = max(maximum, container)
            if smaller == heights[left]: left += 1
            else: right -= 1
        return maximum