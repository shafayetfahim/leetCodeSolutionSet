class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        s = s.split(" ")[::-1]
        s = [word for word in s if word != ""]
        result = " ".join(s)
        return result