class Solution:
    def numberOfSubstrings(self, s: str) -> int:

        abc = {'a': -1, 'b': -1, 'c': -1}

        num_substrings = 0 
        for i, char in enumerate(s):
            abc[char] = i

            min_idx = min(abc['a'], abc['b'], abc['c'])

            if min_idx >= 0:
                num_substrings += min_idx + 1

        return num_substrings



