class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        if not str:
            return True

        left = 0
        right = len(s) - 1

        while right > left:
            if not s[right].isalnum():
                right -= 1

            elif not s[left].isalnum():
                left += 1
        
            else:
                if s[right].lower() != s[left].lower():
                    return False
                right -= 1
                left += 1

        return True
