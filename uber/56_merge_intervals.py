#56 Merge Intervals

# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

#56 Merge Intervals

# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

class Solution:
    def merge(self, intervals):
        if len(intervals) == 0:
            return []

        intervals.sort(key=lambda x: x[0])

        output = [intervals[0]]
        for start, end in intervals[1:]:
            last = output[-1][1]
            if start <= last:
                output[-1][1] = max(end, last)
            else:
                output.append([start, end])

        return output

#Possible edge case
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]

a = Solution()

print(a.merge(intervals))


intervals = [[0,0], [0,6]]
a = Solution()
print(a.merge(intervals))
intervals = [[1,6],[0,2]]
a = Solution()
print(a.merge(intervals))
intervals = [[1,1],[0,6]]
a = Solution()
print(a.merge(intervals))
intervals = [[0,6],[1,1]]
a = Solution()
print(a.merge(intervals))
intervals = [[1,4],[0,0]]
a = Solution()
print(a.merge(intervals))
intervals = [[2,3],[4,5],[6,7],[8,9],[1,10]]
a = Solution()
print(a.merge(intervals))





