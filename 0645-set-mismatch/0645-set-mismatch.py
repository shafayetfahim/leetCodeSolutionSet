from collections import Counter
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        res = [0]*2
        freq = Counter(nums)
        res[0] = max(freq, key=freq.get)
        for i in range(1, len(nums) + 1):
            if i not in freq:
                res[1] = i
                break
        return res
