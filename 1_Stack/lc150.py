# Reverse Polish Notation.
# Input: tokens = ["2","1","+","3","*"]
# Output: 9
# Explanation: ((2 + 1) * 3) = 9

# BYME
def evalRPN(tokens):
    stack = [] 
    for i in tokens:
        if i.lstrip("-").isdigit() :
            stack.append(int(i))
        else : 
            nb2 = int(stack.pop())
            nb1 = int(stack.pop())
            if i == "+":
                stack.append(nb1+nb2)
            elif i == "-":
                stack.append(nb1-nb2)
            elif i == "*":
                stack.append(nb1*nb2)
            elif i == "/":
                stack.append(int(nb1/nb2))
    return stack[0]