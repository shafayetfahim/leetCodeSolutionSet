from math import inf
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr = sorted(arr)
        min_diff = float('inf')
        output = []
        
        for i in range(len(arr)-1):
            min_diff = min(min_diff, abs(arr[i+1] - arr[i]))

        for j in range(len(arr)-1):
            curr_diff = abs(arr[j+1] - arr[j])
            if curr_diff == min_diff: output.append([arr[j], arr[j+1]])
        
        return output



        

            


        