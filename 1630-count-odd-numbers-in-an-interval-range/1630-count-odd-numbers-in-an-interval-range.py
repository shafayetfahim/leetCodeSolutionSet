class Solution:
    def countOdds(self, low: int, high: int) -> int:
        
        if low%2 != 0 and high%2 != 0: return ceil((high-low)/2)+1
        else: return ceil((high-low)/2)