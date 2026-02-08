class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        unique = {}
        for a in arr:
            if a not in unique: unique[a] = 1
            else:
                unique[a] += 1
        return len(list(unique.values())) == len(set(unique.values()))
        