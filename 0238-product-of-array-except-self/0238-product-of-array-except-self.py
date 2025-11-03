import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zero_count = nums.count(0)
        productList = []
        totalProduct = math.prod(nums)

        sansZero = [num for num in nums if num != 0]
        if len(sansZero) == 0: sansZero = 0
        else: sansZero = math.prod(sansZero)

        for i in range(len(nums)):
            if zero_count > 1: productList.append(0)
            elif nums[i] == 0: productList.append(sansZero)
            else: productList.append(int(totalProduct * (nums[i] ** -1)))
        return productList
        