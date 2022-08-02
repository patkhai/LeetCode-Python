'''
Given reverse polish notation, return the integer value of the expression. 
aka "5,3,+,2,/" would be 5 + 3 = 8 and then 8 / 2 = 4.

'''


def evalRPN(tokens):

    stack = []

    ops = {"+", "-", "*", "/"}

    for x in tokens:
        if x in ops:

            opr1 = stack.pop()
            opr2 = stack.pop()

            val = eval(opr2 + x + opr1)

            stack.append(str(int(val)))

        else:
            stack.append(x)
 
    return int(stack[0])

tokens = ["2","1","+","3","*"]
print(evalRPN(tokens))