from collections import Counter
class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        
        # dct = Counter(nums)
        # operations_counter = 0

        # for num in dct.keys():
        #     complement = k - num

        #     if complement in dct and dct[complement] > 0 and dct[num] > 0:
        #         if num == complement:
        #             operations_counter += (dct[num] // 2)
        #             dct[num] = 0 
                
        #         else:
        #             pairs = min(dct[num], dct[complement]) 
        #             operations_counter += pairs
        #             dct[complement] -= pairs
        #             dct[num] -= pairs             

        # return operations_counter


        # Or use sorting and the two pointer approach

        nums.sort()
        operations_counter = 0

        left = 0 
        right = len(nums) - 1

        while left < right:
            sumNumbers = nums[left] + nums[right] 

            if sumNumbers == k:
                operations_counter += 1
                left += 1
                right -= 1

            elif sumNumbers < k:
                left += 1

            else:
                right -= 1

        return operations_counter



        
