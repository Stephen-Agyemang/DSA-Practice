class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:

        sorted_nums = sorted(nums)
        dct = {}
        result = []


        for i, num in enumerate(sorted_nums):

            if num not in dct:
                dct[num] = i 

            
        for num in nums:
            result.append(dct[num])

        return result

                


        
        

