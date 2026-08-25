from collections import Counter
class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:

        # dct = {}

        # for i, num in enumerate(nums):
        #     if num not in dct and num % 2 == 0:
        #         dct[num] = i 

        #     elif num in dct:
        #         dct[num] = -1

        # min_index = 100
        # even_number = -1

        # for key in dct:
        #     if dct[key] < min_index and dct[key] >= 0:
        #         even_number = key
        #         min_index = dct[key]

        # return even_number

        counts = Counter(nums)

        for num in nums:
            if num % 2 == 0 and counts[num] == 1:
                return num

        return -1
