''' 
check if string is palindrome or not with using Deque
''' 

class Deque: 
    def __init__(self):
        self.items = []
    
    def isEmpty(self): 
        return self.items == [] 
    
    def addRear(self,item): 
        self.items.insert(0,item)
    
    def addFront(self,item): 
        self.items.append(item)
    
    def removeRear(self):
        return self.items.pop(0)
    
    def removeFront(self): 
        return self.items.pop()
    
    def size(self): 
        return len(self.items)
    
#O(n)
def isPalindrome(s): 
    charDeque = Deque() 
    
    for char in s: 
        charDeque.addFront(char)
    
    isEqual = True 
    
    while charDeque.size() > 1 and isEqual: 
        first = charDeque.removeFront()
        last =  charDeque.removeRear() 
        
        if first != last: 
            isEqual = False 
    
    return isEqual


s = "radar"
p = "dapsdasdds"

print(isPalindrome(s))        
print(isPalindrome(p))     