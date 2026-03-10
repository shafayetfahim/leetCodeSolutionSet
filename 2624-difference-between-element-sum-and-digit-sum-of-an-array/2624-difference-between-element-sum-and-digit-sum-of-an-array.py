class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        element_sum = sum(nums)
        digit_sum = 0
        temp = "".join(map(str, nums))
        for t in temp:
            digit_sum += int(t)
        return abs(element_sum - digit_sum)
        