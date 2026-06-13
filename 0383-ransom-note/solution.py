class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        if len(ransomNote) > len(magazine):
            return False

        dct = {} 

        for letter in magazine:
            if letter not in dct:
                dct[letter] = 1

            else:
                dct[letter] += 1
        
        for letter in ransomNote:

            if letter not in dct or dct[letter] == 0:
                return False

            else:
                dct[letter] -= 1

        return True
            

