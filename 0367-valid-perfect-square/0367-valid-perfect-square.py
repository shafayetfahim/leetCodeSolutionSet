class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1: return True
        for i in range(1, num):
            if i ** 2 > num: return False
            if i ** 2 == num: return True

        