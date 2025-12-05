import re
class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        sentences = [re.sub(r"[^ ]", "", sentence) for sentence in sentences]
        return len(max(sentences))+1            

        