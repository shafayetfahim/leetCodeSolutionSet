class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if len(word) == 1: return True

        if ord(word[0]) <= 90 and ord(word[1]) <= 90:
            for i in range(len(word)):
                if ord(word[i]) > 90: return False
        else: 
            for j in range(1, len(word)):
                if ord(word[j]) < 97: 
                    return False
        return True
        