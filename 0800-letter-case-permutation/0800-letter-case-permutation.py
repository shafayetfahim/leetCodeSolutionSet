class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        result = []
        stack = [(0, "")]

        while stack:
            i, curr = stack.pop()
            if i == len(s):
                result.append(curr)
                continue
            c = s[i]
            if c.isalpha():
                stack.append((i + 1, curr + c.upper()))
                stack.append((i + 1, curr + c.lower()))
            else: stack.append((i + 1, curr + c))
        return result
