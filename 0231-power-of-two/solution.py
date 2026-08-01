# from math import sqrt
import math 
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        
        # if n < 1:
        #     return False 

        # if n == 1:
        #     return True

        # while n >= 1:
        #     n = n / 2

        #     if n == 1:
        #         return True 

        # return False

        ### OR ###

        # if n <= 0:
        #     return False

        # if n == 1:
        #     return True

        # return n > 0 and log2(n).is_integer()


        return n > 0 and (n & (n-1)) == 0



            
