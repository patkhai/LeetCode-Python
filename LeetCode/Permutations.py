'''
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]

First we have the main driver permute function
• We create a visited variable
• A result variable
• And call the recursive backtracking function (arguments - results, visited, empty subset and given collection)
• Then return the result

Then the backtracking recursive function
• Checks if the length of our current running subset is equal to the length of the collection given
○ If yes we append our results variable with the subset (e.g. [1,3,2])
• Then we iterate over the range of the length of the collection
○ If the current number of the collection[i] is not already in our visited set:
§ Add it to visited
§ call the recursive function, the same as before but this time with the subset + the current number we are iterating over in the collection, such that each iteration has an increasing amount of digits in the subset until we reach the same length as the original collection - where it will be added to our results list
We then remove the current number from visited in order to allow for the creation of new permutations
'''
#O(n!)

def permute(nums):
        visited = set()
        res = []
        backtracking(res,visited,[],nums)
        return res
def backtracking(res,visited,subset,nums):
    if len(subset) == len(nums):
        res.append(subset)
    for i in range(len(nums)):
        if i not in visited:
            visited.add(i)
            backtracking(res,visited,subset+[nums[i]],nums)
            visited.remove(i)


