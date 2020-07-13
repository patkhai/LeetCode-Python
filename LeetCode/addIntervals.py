'''
Given a set of non-overlapping & sorted intervals, insert a new interval into the intervals (merge if necessary).

Example 1:
Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].

Example 2:
Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16].

This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].
'''


def add_interval(intervals, new_interval):
    result = []
    interval_to_merge = new_interval
    for i in range(len(intervals)):
        
        curr_interval = intervals[i]
        if curr_interval[1] < interval_to_merge[0]:
            result.append(curr_interval)
        elif interval_to_merge[1] < curr_interval[0]:
            result.append(interval_to_merge)
            interval_to_merge = curr_interval
        elif curr_interval[1] >= interval_to_merge[0] or curr_interval[0] <= interval_to_merge[1]:
            interval_to_merge = [min(curr_interval[0], interval_to_merge[0]), max(curr_interval[1], interval_to_merge[1])]

    result.append(interval_to_merge)
    return result


print(add_interval([[1, 5], [6, 12], [14, 15]], [3, 6]))
