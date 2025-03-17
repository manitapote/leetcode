class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

# def indentify_all_interval_overlap(int_1, int_2):
#     p_1 = 0
#     p_2 = 0
#     result = []
#     while p_1 < len(int_1) and p_2 < len(int_2):
#         if int_1[p_1].end < int_2[p_2].start:
#             p_1 += 1
#         elif int_1[p_1].start > int_2[p_2].end:
#             p_2 += 1
#             # continue
#         start = max(int_1[p_1].start, int_2[p_2].start)
#         end = min(int_1[p_1].end, int_2[p_2].end)
#
#         result.append(Interval(start, end))
#
#         if int_1[p_1].end < int_2[p_2].end:
#             p_1 += 1
#         else:
#             p_2 += 1
#
#     return result


def indentify_all_interval_overlap(int_1, int_2):
    p_1 = 0
    p_2 = 0
    result = []
    #O(n+m)
    while p_1 < len(int_1) and p_2 < len(int_2):
        #which start first
        if int_1[p_1].start < int_2[p_2].start:
            A, B = int_1[p_1], int_2[p_2]
        else:
            A, B = int_2[p_2], int_1[p_1]

        #overlap
        if A.end >= B.start:
            end = min(A.end, B.end)
            result.append(Interval(B.start, end))

        #moving the pointer
        if A.end < B.end:
            p_1 += 1
        else:
            p_2 += 1

    return result



intervals1 = [[1,4], [5,6], [9, 10]]
intervals2 = [[2,7], [8,9]]

int_1 = []
for x in intervals1:
    int_1.append(Interval(x[0], x[1]))

int_2 = []
for x in intervals2:
    int_2.append(Interval(x[0], x[1]))

results = indentify_all_interval_overlap(int_1, int_2)

for x in results:
    print(x.start, x.end)
