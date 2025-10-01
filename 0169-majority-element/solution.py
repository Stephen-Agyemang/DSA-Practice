class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}
        n = len(nums)

        
        for num in nums:
            if num in hashmap:
                hashmap[num] += 1
            
            else:
               hashmap[num] = 1
        
        for key in hashmap:
            if hashmap[key] > n/2:
                return key
        
        return null 
        
