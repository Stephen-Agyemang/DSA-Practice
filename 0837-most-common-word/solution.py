import re 
from typing import List

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:

        dct = {}
        banned_word = set(banned)


        clean_paragraph = re.sub(r'[^\w\s]', ' ', paragraph.lower())
        words = clean_paragraph.split()

        for word in words:

            if word in banned_word:
                continue
           
            if word in dct:
                dct[word] += 1
            else:
                dct[word] = 1

        print(dct)
        max_appearance = ""
        freq = 0
        for key in dct:
            if dct[key] > freq:
                freq = dct[key]
                max_appearance = key 

        return max_appearance
