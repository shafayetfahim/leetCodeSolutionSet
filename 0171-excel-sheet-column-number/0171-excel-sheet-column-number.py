class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        rev = columnTitle[::-1]
        pos = 0
        output = 0

        for i in range(len(rev)):
            asciiValue = ord(rev[i])-64
            output += (asciiValue * 26**i)

        return output