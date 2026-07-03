class Solution:
    def reverseVowels(self, s: str) -> str:
       
        set_vowels = set("aeiouAEIOU")
        rep_s = ""
        lst_stack = []

        for char in s:
            if char in set_vowels:
                lst_stack.append(char)

        p_s = 0

        while p_s < len(s):
            if s[p_s] in set_vowels:
                rep_s += lst_stack.pop()

            else:
                rep_s += s[p_s]

            p_s += 1
        
        return rep_s

            


                



        




