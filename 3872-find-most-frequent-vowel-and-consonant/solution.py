from collections import Counter

class Solution:
    def maxFreqSum(self, s: str) -> int:

        vowel_freq = 0
        consonant_freq = 0 

        char_frequencies = Counter(s)

        for key in char_frequencies:
            if key in 'aeiou' and char_frequencies[key] > vowel_freq:
                vowel_freq = char_frequencies[key]

            elif key not in 'aeiou' and char_frequencies[key] > consonant_freq:
                consonant_freq = char_frequencies[key]

        return vowel_freq + consonant_freq

        


        
