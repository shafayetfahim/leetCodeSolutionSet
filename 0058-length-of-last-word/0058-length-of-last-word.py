class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        length = 0
        for char in reversed(s):
            print(char)
            if char != " ": length += 1
            else: break
        return length