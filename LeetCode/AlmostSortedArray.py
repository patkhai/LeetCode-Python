'''
Given an almost sorted array, in which each number is less than m spots away from its 
correctly sorted positions, and the value m , write an algorithm
that will return an array with the elements properly sorted. 

An example input would be the list[3,2,1,4,6,5] and m = 3. In this example, 
each element in the array is less than 3 spots away from its position in a sorted array. 

''' 
import heapq


def sort_list(almost_sorted_list, m):
    min_heap, result = [], []
    for elem in almost_sorted_list[:m]:
        heapq.heappush(min_heap, elem)

    for elem in almost_sorted_list[m:]:
        heapq.heappush(min_heap, elem)
        result.append(heapq.heappop(min_heap))

    for i in range(len(min_heap)):
        result.append(heapq.heappop(min_heap))

    return result


a = [3, 2, 1, 4, 6, 5]
m = 3

print(sort_list(a, m))
