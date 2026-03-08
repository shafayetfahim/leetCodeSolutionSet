class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected, enumerator = sorted(heights), 0
        for h, e in zip(heights, expected):
            if h != e: enumerator += 1
        
        return enumerator
        