class Solution:
    def addDigits(self, num: int) -> int:
        while True:
            if len(str(num)) == 1: return num
            else: num = sum([int(digit) for digit in str(num)])
        
        