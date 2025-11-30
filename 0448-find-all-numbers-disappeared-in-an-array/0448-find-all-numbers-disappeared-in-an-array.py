class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        nSet = set(nums)
        reference = set()
        disappeared = []

        # Creating reference set
        for i in range(1, len(nums)+1): reference.add(i)
        print(reference)

        # If numsSet(i) in reference set: 
        for ref in reference:
            if ref not in nSet: disappeared.append(ref)

        return disappeared

