class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        i = 0
        while i < len(s)/2:
            temp = s[i]
            s[i] = s[len(s)-i-1]
            s[len(s)-i-1] = temp
            i += 1

    # at s[i], replace with len(i-1) and replace len(i-1) with s[i]
    # "o e l l o"
    # Approach: sto