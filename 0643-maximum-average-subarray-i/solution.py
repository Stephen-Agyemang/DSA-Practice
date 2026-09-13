class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        curr_sum = sum(nums[:k])
        max_sum = curr_sum
        left = 0 
        # right = k

        for i in range(k, len(nums)):
            curr_sum += nums[i] - nums[left]
            max_sum = max(max_sum, curr_sum)
            left += 1
            # right += 1

        return max_sum/k
