class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        # set_nums = set(nums)
        # set_range = set()

        # for num in range(1, len(nums) + 1):
        #     set_range.add(num)

        # print(set_range)

        # return list(set_range - set_nums)

        # if not nums:
        #     return None 

        # if len(nums) == 1:
        #     return []

        # res_lst = []
        # set_nums = set(nums)

        # if 1 not in set_nums:
        #     res_lst.append(1)

        # for digit in range(2,len(nums) + 1):

        #     if digit not in set_nums:
        #         res_lst.append(digit)

        # return res_lst

        for num in nums:
            index = abs(num) - 1

            if nums[index] > 0:
                nums[index] = -nums[index]

        res_lst = []

        for i in range(len(nums)):
            if nums[i] > 0:
                res_lst.append(i + 1)

        return res_lst







