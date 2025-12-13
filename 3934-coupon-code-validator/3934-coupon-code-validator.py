import re
from typing import List

class Solution:
    def validateCoupons(self, code: List[str], businessLine: List[str], isActive: List[bool]) -> List[str]:
        order = {
            "electronics": 0,
            "grocery": 1,
            "pharmacy": 2,
            "restaurant": 3,
        }

        pattern = r'^[a-zA-Z0-9_]+$'
        valid = [
            (order[businessLine[i]], code[i])
            for i in range(len(code)) if isActive[i]
            and re.match(pattern, code[i])
            and businessLine[i] in order
        ]

        valid.sort()
        return [c for _, c in valid]
