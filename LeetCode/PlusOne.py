
'''

Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.

uppose you have a number in your list/array such that adding 1 would make it a two digit number,
eg: [9]
o/p: [1,0]
Plusone(9) would be [10], but the expected output should be [1,0] such that the most significant digit is on the head



''' 


def plusOne(digits):
    length = len(digits) - 1
    res = list(digits)
    while res[length] == 9:
        res[length] = 0
        length -= 1
    if(length < 0):
        res = [1] + res
    else:
        res[length] += 1
    return res

print(plusOne([9])) #[1,0]
print(plusOne([0])) #[1]
print(plusOne([1,2,3,4])) #[1,2,3,5]