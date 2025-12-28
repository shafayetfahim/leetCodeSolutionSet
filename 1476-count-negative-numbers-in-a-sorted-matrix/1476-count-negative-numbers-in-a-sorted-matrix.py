import itertools
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        G = sorted(list(itertools.chain(*grid)))
        for g in range(len(G)):
            if G[g] >= 0: return g
        return len(G)
        

            
        