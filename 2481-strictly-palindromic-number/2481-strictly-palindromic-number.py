class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        for i in range(2, (n-1)):
            digits = []
            temp = n
            while temp != 0:
                digits.append(temp % i)
                temp //= i
            left, right = 0, len(digits)-1
            while left < right:
                if digits[left] != digits[right]: return False
                else:
                    left += 1
                    right -= 1
        return True