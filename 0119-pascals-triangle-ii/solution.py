class Solution:
    def getRow(self, rowIndex: int) -> List[int]:

        row = [1] * (rowIndex + 1)
        
        for i in range(1, rowIndex):

            for j in range(i, 0, -1):
                row[j] = row[j] + row[j-1]

        return row


    #               0  1  2  3 
    #     output = [1, 3, 3, 1]

    #            0  1  2  3
    #     row = [1, 1, 1, 1]

            
    # #  0      1     2
    # # [[1], [1,1], [1, 2, 1], [1, 3, 3, 1]]
