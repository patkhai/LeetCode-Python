'''
For an undirected graph with tree characteristics, we can choose any node as the root. The result graph is then a rooted tree. Among all possible rooted trees, those with minimum height are called minimum height trees (MHTs). Given such a graph, write a function to find all the MHTs and return a list of their root labels.

Format
The graph contains n nodes which are labeled from 0 to n - 1. You will be given the number n and a list of undirected edges (each edge is a pair of labels).

You can assume that no duplicate edges will appear in edges. Since all edges are undirected, [0, 1] is the same as [1, 0] and thus will not appear together in edges.

Example 1 :

Input: n = 4, edges = [[1, 0], [1, 2], [1, 3]]

        0
        |
        1
       / \
      2   3 

Output: [1]
Example 2 :

Input: n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]

     0  1  2
      \ | /
        3
        |
        4
        |
        5 

Output: [3, 4]
'''

def findMinHeightTrees(n, edges):
        tree = [set() for _ in range(n)]
        
        for x, y in edges:
            tree[x].add(y)
            tree[y].add(x)
            
        queue = []
        for i in range(n):
            if len(tree[i]) <= 1:
                queue.append(i)
        
        while queue:
            new_queue = []
            
            for node in queue:
                for nxt in tree[node]:
                    tree[nxt].remove(node)
                    if len(tree[nxt]) == 1:
                        new_queue.append(nxt)
            
            if not new_queue:
                return queue
            
            queue = new_queue
n = 6 
edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]
print(findMinHeightTrees(n , edges))