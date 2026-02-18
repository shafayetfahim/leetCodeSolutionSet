class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        string = bin(n)
        for i in range(3, len(string)):
            if string[i] == string[i-1]: return False
        return True

        