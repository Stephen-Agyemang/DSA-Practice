class Solution:
    def addDigits(self, num: int) -> int:

    #     digit = num
    #     while digit >= 10:
    #         digit = self.addelements(digit)

    #     return digit


    # def addelements(self, num: int) -> int:
    #     if num <= 0:
    #         return num

    #     string = str(num)
    #     n = 0
    #     sum_num = 0

    #     while n < len(string):
    #         sum_num += int(string[n])
    #         n += 1

    #     return sum_num


        # if num == 0:
        #     return 0 

        # return 1 + (num - 1) % 9

        while num >= 10:

            temp = 0 

            while num > 0:
                temp += num % 10
                num //= 10

            num = temp

        return num

