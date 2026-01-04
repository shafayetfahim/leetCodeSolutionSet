class Solution:
    def toHex(self, num: int) -> str:
        if num == 0:
            return "0"
        
        # handle negative numbers using 32-bit two's complement
        if num < 0:
            num += 2 ** 32
        
        digits = "0123456789abcdef"
        res = []
        
        while num > 0:
            res.append(digits[num % 16])
            num //= 16
        
        return "".join(reversed(res))
