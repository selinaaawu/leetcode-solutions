class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        ## STACK | time: O(n), space: O(n)
        # stack bc most recent numbers are the ones used next
        stack = []
        
        for token in tokens:
            # if operator, pop two numbers, apply operation, push result to stack
            if token in ['+', '-', '*', '/']:
                num2, num1 = stack.pop(), stack.pop()
                if token == '+':
                    stack.append(num1 + num2)
                elif token == '-':
                    stack.append(num1 - num2)
                elif token == '*':
                    stack.append(num1 * num2)
                elif token == '/':
                    stack.append(int(float(num1) / num2))
            # if num, push onto stack
            else:
                stack.append(int(token))

        return stack.pop()
        