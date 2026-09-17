class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        # Python in built (in) helps with this time complexity: O(N * M), N is the number of patterns and M is the length of word

        count_substrings = 0 

        for char in patterns:
            if char in word:
                count_substrings += 1

        return count_substrings
        
        

        
