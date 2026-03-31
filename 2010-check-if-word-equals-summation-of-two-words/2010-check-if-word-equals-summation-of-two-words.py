class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        def getLetterValue(letter: str) -> int:
            return str(ord(letter)-97)
        
        def parseWord(word: str) -> int:
            concatenation = ""
            for letter in word:
                concatenation += getLetterValue(letter)
            return int(concatenation)

        firstResult, secondResult, targetResult = parseWord(firstWord), parseWord(secondWord), parseWord(targetWord)
        print(firstResult)
        print(secondResult)
        print(targetResult)
        return (firstResult + secondResult) == targetResult


        