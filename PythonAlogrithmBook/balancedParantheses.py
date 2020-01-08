#check if the parentheses are equal and balance

def balanceCheck(s): 

    stack1 = [] 
    stack2 = [] 

    balance = "" 

    brackets = { 
        "{":"}", 
        "[":"]", 
        "(":")"
    }

    for braces in s: 
        if braces in brackets: 
            stack1.append(braces)
            stack2.append(brackets[braces])
    while stack1: 
        balance += (stack1.pop() + stack2.pop())
    return len(balance) == len(s)

s = "[({})]"
d = "[[({})]"
e = "{({]]})]" 
f = "({[]})"  
print(balanceCheck(s))
print(balanceCheck(d))
print(balanceCheck(e))
print(balanceCheck(f))

