class Solution:
    def getLucky(self, s: str, k: int) -> int:
        numeric_str = "".join(str(ord(ch) - ord('a') + 1) for ch in s)
        for _ in range(k):
            current_sum = 0
            for digit in numeric_str:
                current_sum += int(digit)
            numeric_str = str(current_sum)
        return int(numeric_str)