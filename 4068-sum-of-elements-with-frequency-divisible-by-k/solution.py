from collections import Counter
class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:

        num_freq = Counter(nums)

        sum_freq = 0
        for key in num_freq:
            if num_freq[key] % k == 0:
                sum_freq += (key * num_freq[key])

        return sum_freq

