# You are given an integer array height of length n. There are n vertical lines drawn such
# that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.


# Example 1:


# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
# Example 2:

# Input: height = [1,1]
# Output: 1

def mostWater(height):
    left, right = 0, len(height)-1
    res = 0

    while left < right:
        area = (right - left) * min(height[left], height[right])
        res = max(res, area)

        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return res


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(mostWater(height))

# We start with two pointers, left at the beginning and right at the end of the array.

# We maintain a variable max_area to keep track of the maximum area found so far.

# Inside the while loop, we calculate the area formed by the two lines at positions left and right. The width of the container is given by width = right - left, and the height is the minimum of the two line heights.

# We update max_area if the current area is greater.

# We then move one of the pointers inward. We move the pointer pointing to the shorter line because moving the taller line inward will not increase the height (and hence the area), but moving the shorter line inward might lead to a greater height and area.

# We continue this process until left is less than right.
