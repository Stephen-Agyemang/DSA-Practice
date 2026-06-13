class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:

        total_sum = 0
        dct = {}

        for num in nums:

            if num in dct:
                dct[num] += 1
            
            else: 
                dct[num] = 1

        for key, val in dct.items():
            if val % k == 0:
                total_sum += key * val

        return total_sum

        
