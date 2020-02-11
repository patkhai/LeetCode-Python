


def vowels(strings):
    
    letters = ["a","e","i","o","u"] 
    
    secondString = [] 
    
    
    for char in strings: 
        if char not in letters: 
            secondString += char 
    return secondString
    
        
s = "my name is abc"
    
print(vowels(s))         
 




     
def limitIndex(strings, search): 
    res = [] 
    l = len(strings) 
    index = 0 
    
    while index < l: 
        i = strings.find(search, index) 
        if i == -1: 
            return res 
        res.append(i) 
        index = i + 1 
    return res 
    
    
              

s = "Mya nameis ksjfhskdjhf"
print(limitIndex(s, "ame"))