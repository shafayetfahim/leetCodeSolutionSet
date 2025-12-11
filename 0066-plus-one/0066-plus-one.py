class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        running_sum = 0
        digits.reverse()
        for i in range(len(digits)):
            running_sum += (digits[i]*(10**i))
        running_sum += 1

        return [int(digit) for digit in str(running_sum)]

        

        