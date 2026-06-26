class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        dct = {}
        num_of_operations = 0

        for num in nums:
            complement = k - num

            if complement in dct and dct[complement] > 0:
                num_of_operations += 1
                dct[complement] -= 1
            
            else:
                if num not in dct: 
                    dct[num] = 1

                else:
                    dct[num] += 1

        return num_of_operations



        
