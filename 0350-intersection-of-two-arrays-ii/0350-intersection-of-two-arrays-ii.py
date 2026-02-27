class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        freqMap, freqMap2 = {}, {}
        for num in nums1:
            if num in freqMap: freqMap[num] += 1
            else: freqMap[num] = 1
        
        for num in nums2:
            if num in freqMap2: freqMap2[num] += 1
            else: freqMap2[num] = 1

        overlap = {k: min(freqMap[k], freqMap2[k]) for k in freqMap if k in freqMap2}
        output = []
        for num, count in overlap.items():
            output.extend([num] * count)
        return output




        
        
        