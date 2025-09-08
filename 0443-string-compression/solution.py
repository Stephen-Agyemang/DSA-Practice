class Solution:
    def compress(self, chars: List[str]) -> int:
        s = ""
        left = 0

        while left < len(chars):
            char = chars[left]
            count = 0

            while left < len(chars) and chars[left] == char:
                    count += 1
                    left += 1
            
            s += char 
            if count > 1:
                s += str(count)

        chars[:] = list(s)
        return len(chars)
