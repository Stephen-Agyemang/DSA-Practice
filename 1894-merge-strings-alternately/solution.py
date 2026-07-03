class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        lst = []
        idx = 0

        if not word1:
            return word2
        
        if not word2:
            return word1

        while idx < len(word1) and idx < len(word2):
            lst.append(word1[idx])
            lst.append(word2[idx])
            idx += 1

        if idx < len(word1):
            lst.append(word1[idx:len(word1)])

        if idx < len(word2):
            lst.append(word2[idx:len(word2)])
        
        return "".join(lst)


