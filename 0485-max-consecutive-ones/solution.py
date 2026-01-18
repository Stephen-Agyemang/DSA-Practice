class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        
        maxConsecOnes = 0 
        tempOnesCounter = 0

        for num in nums:
            if num == 1:
                tempOnesCounter += 1
                
            else:
                maxConsecOnes = max(maxConsecOnes, tempOnesCounter)
                tempOnesCounter = 0 

        return max(maxConsecOnes, tempOnesCounter)

        
        
