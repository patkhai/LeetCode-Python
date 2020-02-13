'''
Given an array, data, of data points, write a function findBusiestPeriod that returns the time at which the mall 
reached its busiest moment last year. The return value is the timestamp, e.g. 1480640292. Note that if there is more 
than one period with the same visitor peak, return the earliest one.

Assume that the array data is sorted in an ascending order by the timestamp. Explain your solution and analyze its 
time and space complexities.

Example:

input:  data = [ [1487799425, 14, 1], 
                 [1487799425, 4,  0],
                 [1487799425, 2,  0],
                 [1487800378, 10, 1],
                 [1487801478, 18, 0],
                 [1487801478, 18, 1],
                 [1487901013, 1,  0],
                 [1487901211, 7,  1],
                 [1487901211, 7,  0] ]

output: 1487800378 # since the increase in the number of people
                   # in the mall is the hig

'''

#O(n) O(1)

def find_busiest_period(data):
  ppl = 0 
  maxT = 0 
  maxppl = 0
  length = len(data) - 1
  for val,lists in enumerate(data):
    if lists[2] == 1: 
      ppl += lists[1] # visitors entered the mall  
    else: 
      ppl -= lists[1]# visitors existed the mall
    
    # check for other data points with the same timestamp
    if val < length and data[val][0] == data[val+1][0]: 
      continue 
      
    if ppl > maxppl: 
      maxppl = ppl 
      maxT = lists[0] #update the time 
  return maxT


d = [ [1487799425, 14, 1], 
[1487799425, 4,  0],
[1487799425, 2,  0], 
[1487800378, 10, 1],
[1487801478, 18, 0],
[1487801478, 18, 1],
[1487901013, 1,  0],
[1487901211, 7,  1],
[1487901211, 7,  0] ]

print(find_busiest_period(d))

      
      
  