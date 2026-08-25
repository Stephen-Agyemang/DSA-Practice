class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:


        if not nums:
            return []

        dct = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in dct:
                return [dct[complement], i]

            dct[num] = i

        return []
            
            

            
        
