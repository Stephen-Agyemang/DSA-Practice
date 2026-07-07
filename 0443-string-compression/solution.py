class Solution:
    def compress(self, chars: List[str]) -> int:
   
        if not chars:
            return 0
        
        
        ## Using the sliding window / two-pointer approach for an O(1) space comlexity
        left = 0
        new_chars_len = 0

        while left < len(chars):
            right = left 

            while right < len(chars) and chars[right] == chars[left]:
                right += 1

            count = right - left

            chars[new_chars_len] = chars[left] 
            new_chars_len += 1

            if count > 1:
                for digit in str(count):
                    chars[new_chars_len] = digit
                    new_chars_len += 1
            
            left = right

        return new_chars_len

        

            
            

            
        
        
                



