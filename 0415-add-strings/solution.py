class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        

        p1 = len(num1) - 1
        p2 = len(num2) - 1

        carry = 0 
        res = []

        while p1 >= 0 or p2 >= 0 or carry:
            
            if p1 >= 0:
                digit1 = ord(num1[p1]) - ord('0')

            else:
                digit1 = 0 

            if p2 >= 0:
                digit2 = ord(num2[p2]) - ord('0')

            else:
                digit2 = 0


            patch_sum = digit1 + digit2 + carry
            carry = patch_sum // 10

            res.append(str(patch_sum % 10))

            p1 -= 1
            p2 -= 1 

        return "".join(res[::-1])



        
