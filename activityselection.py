def activity_selection(intervals):
    intervals.sort(key=lambda x: x[1])  # sort by end time
    count = 0
    end = -1

    for start, finish in intervals:
        if start >= end:
            count += 1
            end = finish
    return count

# Test
intervals = [(1, 3), (2, 4), (3, 5), (0, 6)]
print("Max Activities:", activity_selection(intervals))  # Output: 2
