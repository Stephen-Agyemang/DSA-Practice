class Solution:
    def thirdMax(self, nums: List[int]) -> int:


        if not nums:
            return -1

        first = second = third = float('-inf')

        for num in nums:
            if num in (first, second, third):
                continue 

            if num > first:
                first, second, third = num, first, second

            elif num > second:
                second, third = num, second

            elif num > third:
                third = num

        if third == float('-inf'):
            return max(nums)

        else: 
            return third




        ## WE have the first, second, third anology



