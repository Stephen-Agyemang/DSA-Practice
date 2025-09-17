class Solution:
    def isPalindrome(self, x: int) -> bool:
        word = str(x)
        left = 0 
        right = len(word) - 1

        while left <= right:
            if word[left] == word[right]:
                left += 1
                right -= 1
            else:
                return False

        return True 


        
