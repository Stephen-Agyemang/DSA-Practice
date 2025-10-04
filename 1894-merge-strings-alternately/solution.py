class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        left = right = 0
        result = [] 
        
        while right < len(word1) and left < len(word2):
            result.append(word1[right])
            result.append(word2[left])
            left += 1 
            right += 1
        
        result.append(word1[right:])
        result.append(word2[left:])

        return "".join(result)

