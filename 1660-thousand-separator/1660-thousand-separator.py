class Solution:
    def thousandSeparator(self, n: int) -> str:
        s = str(n)
        res = []
        for i in range(len(s)):
            if i > 0 and i % 3 == 0: res.append('.')
            res.append(s[len(s) - 1 - i])
        return "".join(res[::-1])

                
        