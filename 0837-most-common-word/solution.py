import re
from collections import Counter

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:

        # let say am able to make paragraph into a dctionary of without adding any of the stuff that are not needed like the symbols and also with everything in lowercase

        # The next parts of what I would do is creating a string word, which will have the string to return
        # I will also have max_freq which would be the freq of that word not to return but guide in finding the word to return

        # I will go through the dictionary, the word I encounter is in there set of banned_words, which is set(banned), for O(1) look-up, I would continue or skip it 

        # I will also use the iteration to update the values of both max_freq and word to find the word with the highest value or dct_paragraph[char] and store it everytime until the process is over which will end up getting me the word I need.

        # words = re.findall(r'\w+', paragraph.lower()) # This converts paragraph into a list of all accepted words.

        # # or we can do this

        cleaner = []

        for char in paragraph:
            if char.isalnum():
                cleaner.append(char)

            else:
                cleaner.append(" ")

        clean_string = "".join(cleaner)

        words = clean_string.lower().split()

        set_banned = set(banned)
        counts = Counter(words)

        most_common = ""
        max_freq = 0 

        for word in counts:
            if word not in set_banned and counts[word] > max_freq:
                most_common = word 
                max_freq = counts[word] 

        return most_common

