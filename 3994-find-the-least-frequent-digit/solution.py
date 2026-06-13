class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:

        dct = {}
        min_frequency = float('inf')
        least_num = 0

        for num in str(n):
            if int(num) in dct:
                dct[int(num)] += 1 

            else:
                dct[int(num)] = 1


        for key, val in dct.items():
            if val < min_frequency:
                least_num = key
                min_frequency = val

            elif val == min_frequency:
                least_num = min(least_num, key)

        return least_num

            

        
