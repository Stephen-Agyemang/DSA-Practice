class Solution:
    def isPalindrome(self, x: int) -> bool:
        
       # Using math to solve this question

        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reversed_num = 0 
        original_num = x

        while x > 0:
            last_digit = x % 10

            reversed_num = (reversed_num * 10) + last_digit
            x = x // 10

        return reversed_num == original_num


    
    
