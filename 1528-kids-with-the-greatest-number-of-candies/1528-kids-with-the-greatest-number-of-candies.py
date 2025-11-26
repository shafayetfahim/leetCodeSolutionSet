class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = max(candies)
        outputList = [False] * len(candies)
        for i in range(len(candies)):
            if (candies[i] + extraCandies) >= maxCandies: outputList[i] = True
            else: outputList[i] = False
        return outputList

            
        