from math import isqrt

def is_prime(num):
    if num <= 1:
        return False

    for i in range(2, isqrt(num) + 1):
        if num % i == 0:
            return False

    return True
    

class Solution:
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        
        dct = {}

        for num in nums:
            if num in dct:
                dct[num] += 1 

            else:
                dct[num] = 1

        for key in dct:
            if is_prime(dct[key]):
                return True

        return False

        
