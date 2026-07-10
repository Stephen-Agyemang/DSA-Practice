class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        list_to_int = int("".join(map(str, digits))) 

        list_to_int = list_to_int + 1


        return [int(digit) for digit in str(list_to_int)]

        """

        result = []
        for digit in str(list_to_int):
            result.append(int(digi))
        
        return result
        """
