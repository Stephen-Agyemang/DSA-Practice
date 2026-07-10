class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        if not nums:
            return 0

        right = len(nums) - 1
        left = 0

        while left <= right:
            if nums[left] == val and nums[right] != val:
                nums[right], nums[left] = nums[left], nums[right] 
                right -= 1
                left += 1

            elif nums[left] != val and nums[right] == val:
                left += 1
                right -= 1

            elif nums[left] != val and nums[right] != val:
                left += 1

            else:
                right -= 1

        return left
        
