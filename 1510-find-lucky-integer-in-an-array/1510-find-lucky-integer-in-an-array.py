class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freqMap = {}
        largest_lucky = -1
        for i in arr:
            if i in freqMap: freqMap[i] += 1
            else: freqMap[i] = 1
        
        for f in freqMap:
            if freqMap[f] == f:
                largest_lucky = max(largest_lucky, f)
        
        return largest_lucky