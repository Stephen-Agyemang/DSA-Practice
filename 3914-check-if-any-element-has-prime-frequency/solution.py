from collections import Counter

class Solution:
    def factorCounter(self, number: int) -> bool:
        
        if number <= 1:
            return False
        
        factor_count = 2
        num = number // factor_count

        while num > 1:
            if number % num == 0:
                return False

            num = number // factor_count
            factor_count += 1

        return True

    def checkPrimeFrequency(self, nums: List[int]) -> bool:

        frequencies = Counter(nums)

        for key in frequencies:
            print(frequencies[key])
            print(self.factorCounter(frequencies[key]))
            if self.factorCounter(frequencies[key]):
                return True

        return False 

