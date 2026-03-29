class Solution:
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = [0, 0]
        nums2set = set(nums2)
        for i in range(len(nums1)):
            if nums1[i] in nums2set: res[0] += 1
        
        nums1set = set(nums1)
        for j in range(len(nums2)):
            if nums2[j] in nums1set: res[1] += 1
        
        return res
        
        
        