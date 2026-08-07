class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:

        op = {"*", "+", "-"}
        

        def dfs(expr):
            
            resulting_lst = []

            if not any(c in op for c in expr):
                return [int(expr)]

            for i, char in enumerate(expr):
                if char in op:
                    left = dfs(expr[:i])
                    right = dfs(expr[i+1:])

                    for l in left:
                        for r in right:
                            if char == "*":
                                resulting_lst.append(l*r)
                            elif char == "-":
                                resulting_lst.append(l-r)

                            else:
                                resulting_lst.append(l+r)

            return resulting_lst

        return dfs(expression)

                            


            

            
        
