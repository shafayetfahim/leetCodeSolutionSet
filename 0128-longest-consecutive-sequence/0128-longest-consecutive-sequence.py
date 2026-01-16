class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 1. Handle the empty case immediately
        if not nums:
            return 0
        
        # 2. Convert to set for O(1) lookups
        num_set = set(nums)
        max_length = 0

        for num in num_set:
            # 3. Check if 'num' is the START of a sequence
            if num - 1 not in num_set:
                current_num = num
                current_length = 1

                # 4. "Walk" the sequence
                while current_num + 1 in num_set:
                    current_num += 1
                    current_length += 1
                
                # 5. Update global max
                if current_length > max_length:
                    max_length = current_length

        return max_length