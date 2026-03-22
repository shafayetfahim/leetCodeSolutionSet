class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
            current_max = -1
            for i in range(len(arr) - 1, -1, -1):
                current_val = arr[i]
                arr[i] = current_max
                if current_val > current_max: current_max = current_val
            return arr
            
        