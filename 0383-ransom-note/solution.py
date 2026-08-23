from collections import Counter

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        # dct = Counter(magazine)

        # # for letter in magazine:
        # #     if letter not in dct:
        # #         dct[letter] = 1

        # #     else:
        # #         dct[letter] += 1

        # for char in ransomNote:
        #     if dct[char] <= 0:
        #         return False

        #     dct[char] -= 1

        # return True


        return not(Counter(ransomNote) - Counter(magazine))


            
