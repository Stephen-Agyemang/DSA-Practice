class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        # Patterns is an array of strings
        # Word is a string

        # We are looking for number of strings in the array, patterns that exists as a substring in word.


        # We will have to go through Patterns
        # If we want to make look-ups O(n) we should make the string word a set.
        # We will first try the brute force approach, which means that at every string in patterns, we will stop and check if all it's elements are in the set we form from the string word.

        count_substring = 0

        for chars in patterns:
                    
            if chars in word:
                count_substring += 1
        
        return count_substring



        
