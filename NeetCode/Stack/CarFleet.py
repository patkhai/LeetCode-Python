# There are n cars going to the same destination along a one-lane road. The destination is target miles away.

# You are given two integer array position and speed, both of length n, where position[i] is the position of the ith car and speed[i] is the speed of the ith car (in miles per hour).

# A car can never pass another car ahead of it, but it can catch up to it and drive bumper to bumper at the same speed. The faster car will slow down to match the slower car's speed. The distance between these two cars is ignored (i.e., they are assumed to have the same position).

# A car fleet is some non-empty set of cars driving at the same position and same speed. Note that a single car is also a car fleet.

# If a car catches up to a car fleet right at the destination point, it will still be considered as one car fleet.

# Return the number of car fleets that will arrive at the destination.


# Example 1:

# Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
# Output: 3
# Explanation:
# The cars starting at 10 (speed 2) and 8 (speed 4) become a fleet, meeting each other at 12.
# The car starting at 0 does not catch up to any other car, so it is a fleet by itself.
# The cars starting at 5 (speed 1) and 3 (speed 3) become a fleet, meeting each other at 6. The fleet moves at speed 1 until it reaches target.
# Note that no other cars meet these fleets before the destination, so the answer is 3.


def carFleet(target, position, speed):
    pair = [[p, s] for p, s in zip(position, speed)]
    stack = []
    for p, s in sorted(pair)[::-1]:
        time_to_target = (target-p)/s
        stack.append(time_to_target)
        if len(stack) >= 2 and stack[-1] <= stack[-2]:
            stack.pop()
    return len(stack)


target = 12
position = [10, 8, 0, 5, 3]
speed = [2, 4, 1, 1, 3]

print(carFleet(target, position, speed))

# The code first creates a list of pairs, pair, where each pair contains the position and speed of a car. This is done using a list comprehension that zips together the position and speed lists.

# It initializes an empty stack, stack, which will be used to keep track of the time it takes for each car to reach the destination.

# The code then iterates over the pairs of cars sorted in descending order based on their positions (position) using sorted(pair)[::-1]. Sorting in descending order ensures that cars closest to the target are considered first.

# For each car, it calculates the time it takes to reach the target using the formula (target - p) / s, where p is the car's position and s is its speed.

# The calculated time is then appended to the stack.

# After adding the time for each car, it checks if there are at least two times in the stack (i.e., len(stack) >= 2). If so, it compares the times of the last two cars in the stack (stack[-1] and stack[-2]).

# If the time of the current car (stack[-1]) is less than or equal to the time of the car just before it (stack[-2]), it means that the current car can form a fleet with the car ahead of it. In this case, the car ahead is removed from the stack using stack.pop(), as they will arrive at the destination together.

# Finally, the code returns the length of the stack, which represents the number of car fleets that will arrive at the destination.