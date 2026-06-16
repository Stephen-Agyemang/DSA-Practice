class Solution:
    def processStr(self, s: str) -> str:

        result = ""

        if not s:
            return result

        for char in s:
            if char.isalpha():
                result += char

            elif char == "*" and result:
                result = result[:-1]

            elif char == "#":
                result += result

            else:
                result = result[::-1]

        return result
        
