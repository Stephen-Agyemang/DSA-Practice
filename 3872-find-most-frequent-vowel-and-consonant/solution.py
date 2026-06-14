class Solution:
    def maxFreqSum(self, s: str) -> int:
        
        freq_consonant = 0
        freq_vowel = 0
        vowels = set("aeiou")
        dct = {}

        for letter in s:
            if letter in dct:
                dct[letter] += 1
            
            else:
                dct[letter] = 1

        for key in dct:
            if key in vowels and dct[key] > freq_vowel:
                freq_vowel = dct[key]

            if key not in vowels and dct[key] > freq_consonant:
                freq_consonant = dct[key]

        return freq_vowel + freq_consonant


