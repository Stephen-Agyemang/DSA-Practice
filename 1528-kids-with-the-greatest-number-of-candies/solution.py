class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        # result = [False] * len(candies)
        max_candies = max(candies)
        print(max_candies)
        # print(result)

        for i in range(len(candies)):
            if (candies[i] + extraCandies) >= max_candies:
                candies[i] = True
            
            else:
                candies[i] = False

        return candies
                




        
