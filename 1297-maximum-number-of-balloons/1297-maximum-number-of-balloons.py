from collections import Counter

class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        counts = Counter(text)
        
        # Step 2: Determine how many of each required character we have
        # We use .get(char, 0) to avoid KeyErrors if a letter is missing
        b = counts['b']
        a = counts['a']
        l = counts['l'] // 2  # Each "balloon" needs two 'l's
        o = counts['o'] // 2  # Each "balloon" needs two 'o's
        n = counts['n']
        
        # Step 3: The bottleneck (minimum) is our answer
        return min(b, a, l, o, n)
            