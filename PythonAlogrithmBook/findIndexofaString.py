

def find(astring, achar):
    """
    Find and return the index of achar in astring.
    Return -1 if achar does not occur in astring.
    """
    found = False
    index = 0
    for i in astring:
        if i == achar: 
            found = True
            return index 
        else: 
            index += 1
        
    if found: 
        return index
    else: 
        return -1
        
    


print(find("Compsci", "p"))
print(find("Compsci", "C"))
print(find("Compsci", "i"))
print(find("Compsci", "x"))
