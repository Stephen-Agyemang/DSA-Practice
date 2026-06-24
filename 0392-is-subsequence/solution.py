class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

##Approach 1    
        # if not s and not t:
        #     return True

        # new_s = set(s)
        # copy_t = ""

        # for char in t:
        #     if char in new_s:
        #         copy_t += char

        # print(copy_t)
        # print(new_s)

        # if len(copy_t) != len(s):
        #     return False

        # for i in range(len(copy_t)):
        #     if s[i] != copy_t[i]:
        #         return False

        # return True

## Approach 2
        if len(t) < len(s):
            return False

        pointer_s = 0
        pointer_t = 0

        while pointer_t < len(t) and pointer_s < len(s):
            if s[pointer_s] == t[pointer_t]:
                pointer_s += 1

            pointer_t += 1

        if pointer_s < len(s):
            return False
            
        return True
        
        
