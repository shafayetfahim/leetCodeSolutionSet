class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        output = ['0']*len(s)
        for char, index in zip(s, indices):
            output[index] = char
        return "".join(output)
        