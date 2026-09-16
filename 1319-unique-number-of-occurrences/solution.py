from collections import Counter

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:

        freqs = Counter(arr) 
        set_freqs = set(freqs.values())

        return len(set_freqs) == len(freqs)





