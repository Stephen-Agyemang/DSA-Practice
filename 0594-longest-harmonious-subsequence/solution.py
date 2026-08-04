from collections import Counter 

class Solution:
    def findLHS(self, nums: List[int]) -> int:

        counts = Counter(nums)
        longest_len = 0

        for key in counts:
            if key + 1 in counts:
                longest_len = max(longest_len, counts[key] + counts[key+1])

        return longest_len
        
        
                

