class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        sums = 0

        for stone in stones:
            if stone in jewels: sums += 1
        
        return sums
        
