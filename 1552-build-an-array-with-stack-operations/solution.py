class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        ## Target is increasing(it is an array of numbers)

        operations = []
        left = 0  # Left here represents the indices of the numbers in target



        for i in range(1, n + 1):   
            
            if len(target) == left:
                break


            if target[left] == i:
                operations.append("Push")
                left += 1

            else: 
                operations.append("Push")
                operations.append("Pop") 
        return operations

        






