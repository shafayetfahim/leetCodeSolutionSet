class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}
        topK = []
        for i in range(len(nums)):
            if nums[i] in freqMap: freqMap[nums[i]] += 1
            else: freqMap[nums[i]] = 1

        for j in range(k):
            kth = max(freqMap, key=freqMap.get)
            topK.append(kth)
            del freqMap[kth]
        
        return topK