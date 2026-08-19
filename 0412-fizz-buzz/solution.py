class Solution:
    def fizzBuzz(self, n: int) -> List[str]:

        fizz_lst = []

        for i in range(1, n + 1):
            if i % 5 == 0 and i % 3 == 0:
                fizz_lst.append("FizzBuzz")

            elif i % 5 == 0:
                fizz_lst.append("Buzz")

            elif i % 3 == 0:
                fizz_lst.append("Fizz")

            else:
                fizz_lst.append(str(i))

        return fizz_lst


        
