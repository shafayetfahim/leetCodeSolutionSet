class Solution:
    def hammingWeight(self, n: int) -> int:
        oneCount = 0
        n = bin(n)
        for i in range(len(n)): 
            if n[i] == "1": oneCount += 1
        return oneCount
