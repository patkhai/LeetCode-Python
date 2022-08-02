'''
Given a list of the scores of different students, items, where items[i] = [IDi, scorei] represents one score from a student with IDi, calculate each student’s top five average.

Return the answer as an array of pairs result, where result[j] = [IDj, topFiveAveragej] represents the student with IDj and their top five average. Sort result by IDj in increasing order.

A student’s top five average is calculated by taking the sum of their top five scores and dividing it by 5 using integer division.

Example 1:

Input: items = [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
Output: [[1,87],[2,88]]
Explanation: 
The student with ID = 1 got scores 91, 92, 60, 65, 87, and 100. Their top five average is (100 + 92 + 91 + 87 + 65) / 5 = 87.
The student with ID = 2 got scores 93, 97, 77, 100, and 76. Their top five average is (100 + 97 + 93 + 77 + 76) / 5 = 88.6, but with integer division their average converts to 88.
Example 2:

Input: items = [[1,100],[7,100],[1,100],[7,100],[1,100],[7,100],[1,100],[7,100],[1,100],[7,100]]
Output: [[1,100],[7,100]]
Constraints:

1 <= items.length <= 1000
items[i].length == 2
1 <= IDi <= 1000
0 <= scorei <= 100
For each IDi, there will be at least five scores.
Explanation
Use a heap to maintain the scores in order.
'''

'''
# Takes the input and sorts it so all of a students'
        # scores are grouped together
        # Ex:
        # In : [[1,100],  [2, 60], [1,80], [1,90], [2,60]]
        # Out: [[2,80], [2,60], [1,100], [1, 90], [1,80]]
        items.sort(reverse=True)
        
        # Holds the result
        res = []

        # Holds the data for the student currently being processed
        curr = []

        # Gets the id of the first item of the first item of the input
        # Ex. items = [[2,80], [2,60], [1,100], [1, 90], [1,80]]  
        # items[0] = [2,80]
        # items[0][0] = 2
        idx = items[0][0]

        # Create a loop that goes over the items array
        # Because each item in the items array is itself an array, 
        # we can 'destructure' it so that 'i' is the first element
        # and val is the second. (see below for more on destructuring)
        # Ex. items = [[2,80], [2,60], [1,100], [1, 90], [1,80]]
        # loop 1: i = 2, val = 80
        # loop 2: i = 2, val = 60
        # loop 3: i = 1, val = 100
        # etc...
 
        for i, val in items:
            # If the currently processing id is equal to the stored id
            # we append the score to the curr list. Otherwise, drop into 
            # the else block and start processing the next student
            if i == idx:
                if len(curr) < 5:
                    curr.append(val)
            # If we are here, it means the current student id has changed
            # Calculate the average for the previous student and store it
            else:
                res.append([idx, sum(curr) // len(curr)])
                curr = [val]
                idx = i
        # Once we get here, we have all of the students processed 
        # except the last one. store it. 
        res.append([idx, sum(curr) // len(curr)])
        
        # reverse the list
        res = res[::-1]
        
        # return the result
        return res

'''


def highFive(items):
    items.sort(reverse=True)
    res = []
    curr = []
    idx = items[0][0]

    for i, val in items:
        if i == idx:
            if len(curr) < 5:
                curr.append(val)
        else:
            res.append([idx, sum(curr) // len(curr)])
            curr = [val]
            idx = i
    res.append([idx, sum(curr) // len(curr)])
    res = res[::-1]
    return res


items = [[1, 91], [1, 92], [2, 93], [2, 97], [1, 60], [
    2, 77], [1, 65], [1, 87], [1, 100], [2, 100], [2, 76]]
print(highFive(items))
