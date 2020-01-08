
def reverseString(s): 
    stacks = [] 
    rev = ""
    for char in s: 
        stacks.append(char)
    while len(stacks) != 0: 
        rev = rev + stacks.pop()
    return rev

s = "apple"

print(reverseString(s))
                