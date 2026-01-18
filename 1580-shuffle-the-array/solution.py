class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        
        result = [] 

        for first in range(n):
            result.append(nums[first])
            result.append(nums[first + n])

        return result
        
