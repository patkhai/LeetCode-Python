'''
Input:
[dog, poodle],
[mammal, dog],
pmammal, cat],
pdog, bulldog],
[dog, terrier]


Output:
mammal
	dog
		poodle
		bulldog
		terrier
	cat

'''

from collections import defaultdict
def heirarchy(arr):
    toplevel = set()
    nottop = set()
    hei = defaultdict(list) 
    
    for x, y in arr:
        if x not in nottop:
            toplevel.add(x)
        if y in toplevel:
            toplevel.remove(y)
            nottop.add(y)
        
        hei[x].append(y)  
    
    for x in toplevel:
        dfs(x, hei, 0)
    
def dfs(x, hei, level):
    print('\t'*level + x)
    for child in hei[x]:
        dfs(child, hei, level + 1)

print(heirarchy([('dog', 'poodle'),
           ('mammal', 'dog'),
           ('mammal', 'cat'),
           ('dog', 'bulldog'),
           ('dog', 'terrier')]))