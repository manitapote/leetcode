#506 Relative Ranks

# You are given an integer array score of size n, where score[i] is the score of the ith athlete in a competition. All the scores are guaranteed to be unique.
from typing import List
def relative_ranks(scores: List) -> List:
    temp = sorted(scores, reverse=True)
    map_temp = {}
    for i, x in enumerate(temp):
        if i + 1 ==  1:
            map_temp[x] = 'Gold Medal'
        elif i + 1 == 2:
            map_temp[x] = 'Silver Medal'
        elif i + 1 == 3:
            map_temp[x] = 'Bronze Medal'
        else:
            map_temp[x] = i + 1

    return [map_temp[x] for x in scores]

scores = [5,4,3,2,1]
print(relative_ranks(scores))

scores = [10,3,8,9,4]
print(relative_ranks(scores))
