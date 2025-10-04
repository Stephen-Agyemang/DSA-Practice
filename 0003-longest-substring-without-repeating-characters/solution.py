class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        window_chars = {}
        left = 0 
        max_len = 0

        for right, char in enumerate(s):
            if char in window_chars and window_chars[char] >= left:
                left = window_chars[char] + 1
            
            window_chars[char] = right
            max_len = max(max_len, right - left + 1)

        return max_len
        
        
