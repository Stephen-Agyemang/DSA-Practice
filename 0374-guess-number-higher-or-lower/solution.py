# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        
        # if not n:
        #     return 0

        left = 1
        right = n 

        # if guess(left) == 0:
        #     return left

        # if guess(right) == 0:
        #     return right
        
        while left <= right:
            mid = (left + right) // 2
            api_response = guess(mid)

            if api_response == 0:
                return mid 

            elif api_response == -1:
                right = mid - 1

            else:
                left = mid + 1

        return -1

        
