class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
            # Step 1: Initialize the total sum and the running left sum
        total_sum = sum(nums)
        left_sum = 0
        answer = []
        
        for x in nums:
            # Step 2: The sum of elements to the right of 'x' is 
            # (Total remaining sum) - (current element)
            right_sum = total_sum - left_sum - x
            
            # Step 3: Calculate the absolute difference
            diff = abs(left_sum - right_sum)
            answer.append(diff)
            
            # Step 4: Update left_sum for the next iteration
            left_sum += x
            
        return answer
