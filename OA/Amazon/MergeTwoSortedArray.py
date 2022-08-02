'''
Given 2 sorted arrays, merge them. 
Follow up, ensure only 1 of each element is saved in the merged array aka no duplicates.
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
'''


def mergeArray(nums1, m, nums2, n):
    sortA = sorted(nums1+nums2)
    for i in range(len(sortA)-m-n):
        sortA.remove(0)

    for i in range(m, m+n):
        nums1[i] = nums2[i-m]

    nums1.sort()

    res = list(set(sortA))

    return res


nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
print(mergeArray(nums1, m, nums2, n))
