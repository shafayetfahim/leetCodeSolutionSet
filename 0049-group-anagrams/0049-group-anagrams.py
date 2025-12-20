from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for string in strs:
            canonical = tuple(sorted(string))
            groups[canonical].append(string)
        return list(groups.values())