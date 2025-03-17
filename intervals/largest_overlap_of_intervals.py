#Given an array of intervals, determine the maximum number of intervals that overlap at any point.
#Each interval is half-open, meaning it includes the start point but excludes the end point.
class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

#Intervals are half open
def largest_overlap(input):
    result = []
    #T=O(n)
    #S=O(2n)
    for x in input:
        result.append((x.start, 'S'))
        result.append((x.end, 'E'))

    #T=O(nlog(n))
    #S=O(2n)
    result.sort(key=lambda x: (x[0], x[1]))

    active_interval = 0
    max_interval = 0

    #T=O(n)
    for point, point_type in result:
        if point_type == 'S':
            active_interval += 1
        else:
            active_interval -= 1

        max_interval = max(max_interval, active_interval)

    return max_interval


#Time=O(nlog(n))
#Space=O(n)
intervals = [[1,3], [2,6], [4,8], [6,7],[5,7]]
input = []
for x in intervals:
    input.append(Interval(x[0], x[1]))

print(largest_overlap(input))
