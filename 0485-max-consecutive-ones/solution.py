class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:

        max_freq = 0 
        left = 0 

        # while left < len(nums) and nums[left] != 1:  # finding our first one in nums
        #     left += 1

        # curr_freq = 0

        while left < len(nums):

            if nums[left] == 0: # finding our first one in the while loop instead
                left += 1
                continue

            right = left 
            while right < len(nums) - 1 and nums[right + 1] == 1:
                right += 1
                # curr_freq += 1

            max_freq = max(max_freq, right - left + 1) 
            # curr_freq = 0 
            left = right + 1

        return max_freq
            


        
        
        
