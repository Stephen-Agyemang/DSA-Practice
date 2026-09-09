from collections import Counter
class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:

        dct_target = Counter(target)
        dct_s = Counter(s)

        # for char in s:
        #     if char in dct_target:
        #         if char not in dct_s:
        #             dct_s[char] = 1

        #         else:
        #             dct_s[char] += 1

        # if len(dct_s) < len(dct_target):
        #     return 0 
            
        min_occurences = []

        for key in dct_target:
            min_occurences.append(dct_s[key] // dct_target[key])

        return min(min_occurences)


