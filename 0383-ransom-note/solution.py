class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        '''
        Understanding: * We have two strings return boolean(True or False) after method.
                       * ransomNote and magazine -> See if ransomNote can be constructed from magazine, return True if it can and False if it cannot
                       * Each letter magazine can be used once in RansomNote.
                       * maagazine can be an empty string
        
        Planning: * Check if magazine is empty. We just return False
                  * Put all the characters in magazine.
                  * We check it against ransomNote and if that particular character is in the dictionary that we created from magazine we decrease that particular key's value
                  * We would check all the values of the keys in the dictionary and return False if even one key has a value that is greater than 0.
                  *return True

                
        Implementation:
'''

        if not magazine:
            return False

        dct = {}

        for char in magazine:
            if char not in dct:
                dct[char] = 1
            else:
                dct[char] += 1
        
        for char in ransomNote:
            if char not in dct:
                return False

            dct[char] -= 1

            if dct[char] < 0:
                return False

        return True

            
                
            
        
