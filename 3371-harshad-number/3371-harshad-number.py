class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        digits = sum([int(x) for x in str(x)])
        if x%digits == 0: return digits
        return -1
        
        