class Solution:
    def mirrorDistance(self, n: int) -> int:
        p = int("".join(str(n))[::-1])
        return abs(n - p)
        
        