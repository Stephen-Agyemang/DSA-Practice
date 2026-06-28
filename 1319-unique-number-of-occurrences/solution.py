from collections import Counter 

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:

        dct = Counter(arr)

        return len(dct.values()) == len(set(dct.values()))
            
        
