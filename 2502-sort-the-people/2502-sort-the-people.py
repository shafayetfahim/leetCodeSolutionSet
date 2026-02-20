class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        combined = reversed(sorted(zip(names, heights), key=lambda x: x[1]))
        return [i for i, _ in combined]
        