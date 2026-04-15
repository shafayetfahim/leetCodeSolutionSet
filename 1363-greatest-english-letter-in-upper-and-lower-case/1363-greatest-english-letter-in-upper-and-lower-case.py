class Solution:
    def greatestLetter(self, s: str) -> str:
        char_set = set(s)
        for i in range(ord('Z'), ord('A') - 1, -1):
            upper = chr(i)
            lower = chr(i + 32)
            if upper in char_set and lower in char_set: return upper
        return ""