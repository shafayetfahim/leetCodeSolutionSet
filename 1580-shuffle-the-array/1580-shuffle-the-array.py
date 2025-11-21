class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        out = [0] * (2 * n)
        for i in range(n):
            out[2*i] = nums[i]
            out[2*i + 1] = nums[i + n]
        return out
