class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        length = len(nums)
        answers = [1] * length

        running_prefix = 1
        for i in range(length):
            answers[i] = running_prefix
            running_prefix *= nums[i] 

        running_suffix = 1
        for i in reversed(range(length)):
            answers[i] *= running_suffix 
            running_suffix *= nums[i]

        return answers
        




            
