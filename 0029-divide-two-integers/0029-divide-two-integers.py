class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == divisor: return 1
        if dividend == -2**31 and divisor == -1: return (2**31) - 1 
        if divisor == 1: return dividend
        
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
        dividend, divisor = abs(dividend), abs(divisor)
        quotient = 0

        while dividend >= divisor:
            leftshift = 0
            while dividend >= (divisor << leftshift):
                leftshift += 1

            leftshift -= 1
            dividend -= (divisor << leftshift)
            quotient += (1 << leftshift)

        return min(max(sign * quotient, -2**31), 2**31 - 1)


            
        