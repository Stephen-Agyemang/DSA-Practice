class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        dct = {}
        seen_stuff = set()

        for i, char in enumerate(s):
            if char not in dct:
                if t[i] in seen_stuff:
                    return False

                dct[char] = t[i]
                seen_stuff.add(t[i])

            else:
                if dct[char] != t[i]:
                    return False
        return True
        
