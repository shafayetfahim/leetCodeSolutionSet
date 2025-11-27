class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        candidate = []
        allowedCharacters = set(allowed)
        for i in range(len(words)):
            if set(words[i]) <= allowedCharacters: candidate.append(words[i])

        return len(candidate)