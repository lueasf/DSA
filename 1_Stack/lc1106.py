# Parse bool expre


class Solution:
    def parseBoolExpr(self, expression: str) -> bool:
        expression = expression.replace(',','')
        stack = []

        def is_op(c):
            return (c=='|' or c=='&' or c=='!')
        def perform_and(l):
            return False not in l # si l contient un False, renvoie False
        def perform_or(l):
            return True in l
        
        for i in expression:
            if(i=='('):
                stack.append(i)
            elif(is_op(i)):
                stack.append(i)
            elif(i == 'f'):
                stack.append(False)
            elif(i == 't'):
                stack.append(True)
            elif(i == ')'):
                l = []
                while (stack[-1] != '('):
                    l.append(stack.pop())
                stack.pop() # on enlève la (
                op = stack.pop()
                if (op =='&'):
                    stack.append(perform_and(l))
                elif (op=='|'):
                    stack.append(perform_or(l))
                else:
                    stack.append(not l[0])
                    
        return stack[0]