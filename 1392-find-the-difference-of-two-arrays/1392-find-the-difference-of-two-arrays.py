class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        nums1, nums2 = set(nums1), set(nums2)
        answer = [[],[]]
        for i in nums1:
            if i not in nums2: answer[0].append(i)
        for j in nums2:
            if j not in nums1: answer[1].append(j)
        return answer

        