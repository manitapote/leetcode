#56 Merge Intervals

# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

#56 Merge Intervals

# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

class Solution:
    def merge(self, intervals):
        right = 1
        results = []
        new_interval = intervals[0]
        while right < len(intervals):
            #keep on adding until condition apply
            if new_interval[1] >= intervals[right][0]:
                #take minimum of the first element as first element of new array
                #take maximum of the second element as second element of new array
                new_interval = [min(new_interval[0], intervals[right][0]),
                                max(intervals[right][1], new_interval[1])
                                ]
                right += 1
                continue

            #store result
            else:
                results.append([new_interval[0],new_interval[1]])

                #start with new index
                new_interval = [intervals[right][0],
                                intervals[right][1]
                                ]

                right += 1

        #add the last result
        results.append([new_interval[0],new_interval[1]])

        return results



intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]

a = Solution()

print(a.merge(intervals))


intervals = [[1,4], [0,4]]
a = Solution()
print(a.merge(intervals))

