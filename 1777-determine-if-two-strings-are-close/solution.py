from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # Shuffle? Maybe...

        if len(word1) != len(word2):
            return False

        dct_word1 = {}
        for char in word1:
            if char in dct_word1:
                dct_word1[char] += 1

            else: 
                dct_word1[char] = 1

        dct_word2 = {}
        for char in word2:
            if char in dct_word2:
                dct_word2[char] += 1

            else:
                dct_word2[char] = 1

        if set(dct_word1.keys()) != set(dct_word2.keys()):
            return False

        return sorted(dct_word1.values()) == sorted(dct_word2.values())
        

