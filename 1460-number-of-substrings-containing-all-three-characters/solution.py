class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        
        count_substring = 0
        dct = {'a': -1, 'b': -1, 'c': -1}

        for i, char in enumerate(s):

            dct[char] = i
            
            if dct['a'] != -1 and dct['b'] != -1 and dct['c'] != -1:
                farthest_left_boundary = min(dct['a'], dct['b'], dct['c'])

                count_substring += farthest_left_boundary + 1

        return count_substring



                

        
