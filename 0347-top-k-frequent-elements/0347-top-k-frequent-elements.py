class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}
        topK = []
        for i in range(len(nums)):
            if nums[i] in freqMap: freqMap[nums[i]] += 1
            else: freqMap[nums[i]] = 1
        

        # My initial solution.
        # j = 1        
        # while j <= k:
        #     kth = max(freqMap, key=freqMap.get)
        #     topK.append(kth)
        #     del freqMap[kth]
        #     j += 1
        # return topK

        # List comprehension and lambda functions for sorting.
        return [num for num, _ in sorted(freqMap.items(), key=lambda x: x[1], reverse=True)[:k]]
