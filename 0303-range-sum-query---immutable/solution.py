class NumArray:

    def __init__(self, nums: List[int]):
        self.prefix_sum = [0] * (len(nums) + 1) 

        for i in range(1, len(nums) + 1):
            self.prefix_sum[i] = self.prefix_sum[i-1] + nums[i-1]

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix_sum[right+1] - self.prefix_sum[left]
        

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)


# nums = [10, 2, 1, 5, 7, 6, 4]
#               0.   1.  2. 3.  4.  5   6
# prefix_sum = [10, 12, 13, 18, 25, 31, 35] 
# sumRange(0, 3) left = 0, right = 3

# prefix_sum = [0, 0, 0, 0, 0, 0, 0]



