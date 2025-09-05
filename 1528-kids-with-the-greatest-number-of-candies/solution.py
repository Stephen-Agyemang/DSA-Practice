class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        max_candies = max(candies)
        grtst_candies = []

        for n in range(len(candies)):
            if candies[n] + extraCandies >= max_candies:
                grtst_candies.append(True)
            else:
                grtst_candies.append(False)
        return grtst_candies
        




        
