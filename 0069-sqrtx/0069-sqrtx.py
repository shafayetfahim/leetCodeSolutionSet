class Solution:
    def mySqrt(self, x: int) -> int:
        for i in range(x): 
            if i*i > x: return i-1
        if x == 0 or x == 1: return x
        return x-1