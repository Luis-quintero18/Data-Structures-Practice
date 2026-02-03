"""
Input: tokens = ["1","2","+","3","*","4","-"]

Output: 5

Explanation: ((1 + 2) * 3) - 4 = 5
"""
def evalRPN(tokens: list) -> int:
        stack = []
        ops = {'+', '-', '/', '*'}

        for token in tokens:
            if token not in ops:
                stack.append(int(token))
            else:
                right = stack.pop()
                left = stack.pop()

                if token == '+':
                    stack.append(left + right)
                if token == '-':
                    stack.append(left - right)
                if token == '/':
                    stack.append(left / right)
                if token == '*':
                    stack.append(left * right)
    
        return stack[0]

    
    
print(evalRPN(["1","2","+","3","*","4","-"]))