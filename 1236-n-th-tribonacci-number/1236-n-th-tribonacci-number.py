class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0: return 0

        t = [0, 1, 1]
        for i in range(2, n):
            temp = sum(t[i-2:i+1])
            t.append(temp)
        return t[-1]

        