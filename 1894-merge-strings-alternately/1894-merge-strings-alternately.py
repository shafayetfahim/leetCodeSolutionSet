class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        base_string = ""
        index_seen = 0
        for i, j in zip(word1, word2):
            index_seen += 1
            base_string += i + j
        longer_string = max(word1, word2, key=len)
        return base_string + longer_string[index_seen::]
        