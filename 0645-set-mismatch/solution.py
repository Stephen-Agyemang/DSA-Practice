class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        repeated_num = -1

        for num in nums:
            idx = abs(num) - 1

            if nums[idx] < 0:
                repeated_num = abs(num)

            else:
                nums[idx] *= - 1


        missing_num = -1 

        for i in range(len(nums)):
            if nums[i] > 0:
                missing_num = i + 1

        return [repeated_num, missing_num]

    
