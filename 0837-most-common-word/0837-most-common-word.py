import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        pattern = r"[!?',;.]"
        paragraph = re.sub(pattern, " ", paragraph)
        paragraph = paragraph.lower().strip().split()
        print(paragraph)

        freqMap = {}
        for word in paragraph:
            if word not in banned:
                if word not in freqMap: freqMap[word] = 1
                else: freqMap[word] += 1
        
        return max(freqMap, key=freqMap.get)

        