class Solution:
    def maxPower(self, s: str) -> int:
        current_streak = 1
        max_streak = 1
        
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                current_streak += 1
                if current_streak > max_streak: max_streak = current_streak
            else: current_streak = 1
        return max_streak
        