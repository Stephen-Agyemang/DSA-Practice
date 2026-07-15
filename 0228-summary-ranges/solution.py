class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        lst_ranges = []

        left = 0

        while left < len(nums):
            right = left 

            while right < len(nums) - 1 and nums[right+1] == nums[right] + 1:
                right += 1

            if nums[left] == nums[right]:
                lst_ranges.append(str(nums[left]))

            else:
                lst_ranges.append(f"{nums[left]}->{nums[right]}")
            
            left = right + 1

        return lst_ranges
