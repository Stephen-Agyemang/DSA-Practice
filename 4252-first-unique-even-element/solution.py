class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        
        dct = {}
        
        for num in nums:
            if num % 2 != 0:
                continue

            else:
                if num not in dct and num % 2 == 0:
                    dct[num] = 1

                else:
                    dct[num] += 1

        
        for key in dct:
            if dct[key] == 1:
                return key
        
        return -1
                
            
        
