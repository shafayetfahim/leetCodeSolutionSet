import re
class Solution:
    def hammingWeight(self, n: int) -> int:
        return len(re.sub("[0a-z]", "", bin(n)))
