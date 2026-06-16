class Solution:
    def firstUniqChar(self, s: str) -> int:

        dct = {}
        negate = -1

        for i, char in enumerate(s):
            
            if char not in dct:
                dct[char] = i

            else:
                dct[char] = negate

        for key in dct:
            if dct[key] != negate:
                return dct[key]

        return negate
    



        
