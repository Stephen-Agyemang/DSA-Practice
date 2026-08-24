class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        # return len(s.split()[-1])


        # OR

        if not s:
            return 0

        right = len(s) - 1

        while right >= 0 and not s[right].isalnum():
            right -= 1

        left = right

        while left >= 0 and s[left].isalnum():
            left -= 1 

        return right - left

