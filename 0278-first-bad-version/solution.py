# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:

        if isBadVersion(1) == True: 
            return 1

        right = n 
        left = 1

        while left < right:
            mid = (left + right) // 2

            if isBadVersion(mid) == True:
                right = mid

            else:
                left = mid + 1

        return left
        
