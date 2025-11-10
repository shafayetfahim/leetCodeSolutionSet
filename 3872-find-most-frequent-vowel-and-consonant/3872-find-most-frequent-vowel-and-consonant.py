class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowels = ['a', 'e', 'i', 'o', 'u']
        consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 
                      'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']
        
        vowelsDict = dict.fromkeys(vowels, 0)
        consonantsDict = dict.fromkeys(consonants, 0)

        for char in s.lower():
            if char in vowelsDict:
                vowelsDict[char] += 1
            elif char in consonantsDict:
                consonantsDict[char] += 1

        max_vowel = max(vowelsDict.values()) if vowelsDict else 0
        max_consonant = max(consonantsDict.values()) if consonantsDict else 0

        return max_vowel + max_consonant
