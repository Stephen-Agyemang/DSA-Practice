class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        for token in tokens:
            
            if token not in ("+", "/", "-", "*"):
                stack.append(int(token))

            else:
                if token == "+":
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(b + a)

                elif token == "-":
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(b - a)

                elif token == "*":
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(b * a)

                else:
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(int(b / a))

        if stack:
            return stack[0]

        else:
            return 0

