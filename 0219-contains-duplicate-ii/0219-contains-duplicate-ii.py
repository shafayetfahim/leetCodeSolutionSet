class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        index_map = {}
        
        for i, val in enumerate(nums):
            # Check if the value has been seen before
            if val in index_map:
                # Calculate the distance between current index and last seen index
                if i - index_map[val] <= k:
                    return True
            
            # Update the dictionary with the current index
            index_map[val] = i
            
        return False
        