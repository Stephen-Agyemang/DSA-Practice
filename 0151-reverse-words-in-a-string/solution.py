class Solution:
    def reverseWords(self, s: str) -> str:
        
        # string_stack = s.split()
        # string_stack = string_stack[::-1]

        # new_string = []
        # right = len(string_stack) - 1

        # while right >= 0:
        #     new_string.append(string_stack.pop())
        #     right -= 1

        return " ".join(s.split()[::-1])

        
