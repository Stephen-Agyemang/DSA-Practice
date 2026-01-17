class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        # The XOR way 

        result = len(nums)

        for i, num in enumerate(nums):
            result ^= i ^ num
        return result
