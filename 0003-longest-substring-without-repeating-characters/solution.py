class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        seen = set()
        max_length = 0 
        j = 0

        for i in range(len(s)):

            while s[i] in seen:
                seen.remove(s[j])
                j += 1

            seen.add(s[i])
            max_length = max(max_length, i - j + 1)

        return max_length

