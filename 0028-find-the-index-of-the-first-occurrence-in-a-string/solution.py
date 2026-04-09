class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        if not needle or not haystack:
            return -1
        
        n = len(haystack)
        m = len(needle)

        for i in range(n - m + 1):
            if haystack[i:i+m] == needle:
                return i

        return -1
        
