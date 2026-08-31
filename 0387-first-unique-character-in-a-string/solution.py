class Solution:
    def firstUniqChar(self, s: str) -> int:

        dct = {}

        for i, char in enumerate(s):
            if char not in dct:
                dct[char] = i

            else:
                dct[char] = -1

        first_index = float('inf')

        for key in dct:
            if dct[key] >= 0 and dct[key] < first_index:
                first_index = dct[key]

        return first_index if first_index != float('inf') else -1
