class Solution:
    def sortSentence(self, s: str) -> str:
        s = s.split()
        res = ['']*len(s)

        for segment in s:
            index = int(segment[-1])-1
            res[index] = segment[:len(segment)-1:]
        
        return " ".join(res)



        