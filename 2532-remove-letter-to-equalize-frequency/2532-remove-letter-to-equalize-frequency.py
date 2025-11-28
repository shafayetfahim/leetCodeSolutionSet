from collections import Counter
class Solution:
    def equalFrequency(self, word: str) -> bool:
        freqMap = Counter(word)
        for char in freqMap:
            freqMap[char] -= 1
            values = [v for v in freqMap.values() if v > 0]
            if len(set(values)) == 1:
                return True
            freqMap[char] += 1
        return False
