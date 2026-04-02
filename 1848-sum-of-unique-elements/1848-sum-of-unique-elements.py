class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        freqMap = {}
        for i in range(len(nums)):
            if nums[i] in freqMap: freqMap[nums[i]] += 1
            else: freqMap[nums[i]] = 1
        
        freqMap = {key: value for key, value in freqMap.items() if value <= 1}
        return sum(freqMap)

        
        