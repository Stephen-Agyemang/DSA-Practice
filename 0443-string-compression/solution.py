class Solution:
    def compress(self, chars: List[str]) -> int:
   
        if not chars:
            return 0

        char_counter = 0 
        s = ""

        for i in range(len(chars)):
            char_counter += 1
            
            if (i + 1) == len(chars) or chars[i] != chars[i+1]:
                s += chars[i]

                if char_counter > 1:
                    s += str(char_counter)
                char_counter = 0
      
        chars[:] = list(s)

        return len(chars)
            
            

            
        
        
                



