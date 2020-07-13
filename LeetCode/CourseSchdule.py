'''There are a total of numCourses courses you have to take, labeled from 0 to numCourses-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
'''

def canFinish(numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        graph = [[] for _ in range(numCourses)]
        visited = [0 for _ in range(numCourses)]
        # create graph
        for pair in prerequisites:
            x, y = pair
            graph[x].append(y)
        # visit each node
        for i in range(numCourses):
            if not dfs(graph, visited, i):
                return False
        return True

def dfs(graph, visited, i):
    # if ith node is marked as being visited, then a cycle is found
    if visited[i] == -1:
        return False
    # if it is done visted, then do not visit again
    if visited[i] == 1:
        return True
    # mark as being visited
    visited[i] = -1
    # visit all the neighbours
    for j in graph[i]:
        if not dfs(graph, visited, j):
            return False
    # after visit all the neighbours, mark it as done visited
    visited[i] = 1
    return True

numCourses = 2
prerequisites = [[1,0]]
print(canFinish(numCourses,prerequisites))