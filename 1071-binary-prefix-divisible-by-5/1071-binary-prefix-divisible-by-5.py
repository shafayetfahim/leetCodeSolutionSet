class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        sum = 0
        output = []

        for i, num in enumerate(nums):
            sum = sum * 2 + num
            if sum%5 == 0: output.append(True)
            else: output.append(False)
        
        return output