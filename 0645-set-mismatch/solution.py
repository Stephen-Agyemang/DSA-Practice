class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        
        repeatedN = 0
        seen = set()          

        for num in nums:
            if num in seen:
                repeatedN = num
            
            else:
                seen.add(num)

        n = len(nums)
        total = n * (n + 1) // 2
        missing = total - (sum(nums) - repeatedN)

        return [repeatedN, missing]



        
        
        
