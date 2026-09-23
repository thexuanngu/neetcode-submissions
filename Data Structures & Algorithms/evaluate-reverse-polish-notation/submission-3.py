class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
        # operators follow operands
        operands = ['+', '-', '*', '/']
        stack = []
        for token in tokens:
            if token not in operands:
                stack.append(int(token))
            else:
                top = stack.pop()
                second = stack.pop()
                if token == "+":
                    stack.append(second + top)
                elif token == "-":
                    stack.append(second - top)
                elif token == '*':
                    stack.append(second * top)
                else:
                    stack.append(int(float(second) / top)) # // for flooring
        return stack[0]