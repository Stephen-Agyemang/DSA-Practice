class Solution:
    def compress(self, chars: List[str]) -> int:
        
        s = ""        
        left, right = 0, 0
        

        while left < len(chars):
            count = 0 
            s += chars[left]
            
            while right < len(chars) and chars[right] == chars[left]: 
                    count += 1
                    right += 1
            
            left = right
            
            if count > 1:
                s += str(count)            

        chars[:] = list(s)
        return len(chars)
