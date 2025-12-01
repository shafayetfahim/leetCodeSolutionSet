class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0
        for i in range(len(s)//2):
            right = len(s)-i-1
            temp = s[i]
            s[i] = s[right]
            s[right] = temp

    # at s[i], replace with len(i-1) and replace len(i-1) with s[i]
    # "o e l l o"
    # Approach: sto