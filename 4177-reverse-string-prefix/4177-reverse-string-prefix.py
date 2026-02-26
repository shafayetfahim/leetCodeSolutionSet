class Solution:
    def reversePrefix(self, s: str, k: int) -> str:
        if len(s) == 1 or k == 1: return s
        if len(s) == k: return s[::-1]

        return s[:k][::-1] + s[k::]
        