class Solution:
    def processStr(self, s: str) -> str:

        # result = ""

        # for char in s:

        #     if char == "*":
        #         result = result[:len(result) - 1]

        #     elif char == "#":
        #         res = result 
        #         result = result + res

        #     elif char == "%":
        #         result = result[::-1]

        #     else: 
        #         result = result + char

        # return result


        # Or another better appraoch would be...


        stack = []

        for char in s:

            if char == "*":
                if stack:
                    stack.pop()

            elif char == "#":
                stack.extend(stack)

            elif char == "%":
                stack.reverse()

            else: 
                stack.append(char)

        return "".join(stack)
