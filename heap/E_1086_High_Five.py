# Given a list of the scores of different students, items, where items[i] = [IDi, scorei] represents one score from a student with IDi, calculate each student's top five average.
#
# Return the answer as an array of pairs result, where result[j] = [IDj, topFiveAveragej] represents the student with IDj and their top five average. Sort result by IDj in increasing order.
#
# A student's top five average is calculated by taking the sum of their top five scores and dividing it by 5 using integer division.
#

from collections import defaultdict


# class Solution:
#     def highFive(self, items):
#         items.sort()
#         students = defaultdict(list)
#         for i in items:
#             students[i[0]].append(i[1])
#
#         return [[i, int(sum(j[-5:])/5)] for i, j in students.items()]


#Time complexity: O(nlog(n)) n= number of scores
#Space complexity: O(n)

import heapq
class Solution:
    def highFive(self, items):
        max_heap = defaultdict(list) #O(s)
        for i in items: #O(n)
            heapq.heappush(
                max_heap[i[0]], i[1]
            ) #push every element #O(5log(5)) constant

            if len(max_heap[i[0]]) > 5:
                heapq.heappop(max_heap[i[0]])
                #remove the low priority element from
                #heap #O(5log(5)) constant

        return sorted([[i, sum(value)//5]for i, value in max_heap.items()])
        #O(slog(s))
#Time complexity: O(n +slog(s)) s = number of student
#O(s)
#More efficient for large n








items = [[1, 91], [1, 92], [2, 93], [2, 97], [1, 60], [2, 77], [1, 65], [1, 87], [1, 100], [2, 100], [2, 76]]
print(Solution().highFive(items))