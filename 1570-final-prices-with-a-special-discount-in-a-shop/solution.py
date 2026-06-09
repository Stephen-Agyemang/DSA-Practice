class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        answers = list(prices)
        stack = []

        for i in range(len(prices)):

            while stack and prices[i] <= prices[stack[-1]]:
                popped_index = stack.pop()
                answers[popped_index] = prices[popped_index] - prices[i]
        
            stack.append(i)

        return answers
        
