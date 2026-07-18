class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        if len(needle) > len(haystack):
            return -1 

        if needle not in haystack:
            return -1

        m = len(needle)
        n = len(haystack)

        for i in range(n - m + 1):

            if haystack[i:m+i] == needle:
                return i

        return -1

