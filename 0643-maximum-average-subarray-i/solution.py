class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        right = k - 1
        left = 0

        curr_sum = sum(nums[left:right + 1])
        max_sum = curr_sum

        while right < len(nums) - 1:
            curr_sum -= nums[left]

            right += 1
            left += 1

            curr_sum += nums[right]

            max_sum = max(max_sum, curr_sum)

        return max_sum / k
            


        
