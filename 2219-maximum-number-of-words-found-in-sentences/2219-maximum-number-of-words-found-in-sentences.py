import re
class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        output = [0]*len(sentences)
        for i in range(len(sentences)):
            output[i] = (sentences[i].count(" "))
        return max(output)+1

        