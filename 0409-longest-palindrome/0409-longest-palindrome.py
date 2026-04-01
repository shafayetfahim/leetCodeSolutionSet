from collections import Counter

class Solution:
    def longestPalindrome(self, s: str) -> int:
        counts = Counter(s)
        length = 0
        has_odd_count = False
        
        for count in counts.values():
            length += (count // 2) * 2
            if count % 2 == 1: has_odd_count = True
        return length + 1 if has_odd_count else length