

def duplicateLetter(w):
    l = [] 
    for word in w: 
        for letter in word: 
            if letter not in l: 
                l.append(letter)
    return l


w = ['cat','dog','rabbit']
print(duplicateLetter(w))



