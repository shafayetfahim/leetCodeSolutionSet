import collections
class Solution:
    def firstUniqChar(self, s: str) -> int:
        freqMap = Counter(s)
        print(freqMap)
        for i in range(len(s)):
            if freqMap[s[i]] == 1: return i
        return -1
        