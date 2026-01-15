class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        if not nums: 
            return []

        start = end = nums[0]
        result = []

        for num in nums[1:]: 

            if num == end + 1:
                end = num
            
            else:
                result.append(f"{start}" if start == end else f"{start}->{end}")
                start = end = num
            
        result.append(f"{start}" if start == end else f"{start}->{end}")

        return result
             








        
