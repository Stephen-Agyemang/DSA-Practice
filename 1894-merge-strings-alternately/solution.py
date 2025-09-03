class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        right = 0
        left = 0
        merged_string = ""

        while right < len(word1) or left < len(word2):
            if right < len(word1):
                merged_string += word1[right]
                right += 1
            if left < len(word2):
                merged_string += word2[left]
                left += 1
        return merged_string

        
