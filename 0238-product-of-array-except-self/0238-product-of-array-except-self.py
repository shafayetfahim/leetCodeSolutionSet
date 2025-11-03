import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if nums.count(0) > 1: return [0]*len(nums)
        productList = []
        totalProduct = math.prod(nums)

        sansZero = [num for num in nums if num != 0]
        if len(sansZero) == 0: return [0]
        else: sansZero = math.prod(sansZero)

        for i in range(len(nums)):
            if nums[i] == 0: productList.append(sansZero)
            else: productList.append(int(totalProduct * (nums[i] ** -1)))
        return productList
        