class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}
        for i in range(len(nums)):
            if nums[i] in freqMap: freqMap[nums[i]] += 1
            else: freqMap[nums[i]] = 1
        
        return [num for num, count in sorted(freqMap.items(), key=lambda x: x[1], reverse=True)[:k]]
