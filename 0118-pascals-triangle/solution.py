class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        
        pascal_list = []

        for i in range(numRows):

            row = [1] * (i + 1)

            for j in range(1, i):
                prev_row = pascal_list[i - 1]
                row[j] = prev_row[j] + prev_row[j - 1]

            pascal_list.append(row)

        return pascal_list

            


    








     
