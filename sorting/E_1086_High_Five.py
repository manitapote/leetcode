#1086 High Five

# Given a list of the scores of different students, items, where items[i] = [IDi, scorei] represents one score from a student with IDi, calculate each student's top five average.
#
# Return the answer as an array of pairs result, where result[j] = [IDj, topFiveAveragej] represents the student with IDj and their top five average. Sort result by IDj in increasing order.
#
# A student's top five average is calculated by taking the sum of their top five scores and dividing it by 5 using integer division.

class Solution:
    def highFive(self, items):
        output = {}
        items.sort()

        for i, x in items:
            if i in output:
                output[i].append(x)
            else:
                output[i] = [x]

        return [[key, int(sum(item[-5:])/5)] for key, item in output.items()]




items = [[1,91],[1,92],[2,93],[2,97],[1,60],[2,77],[1,65],[1,87],[1,100],[2,100],[2,76]]
print(Solution().highFive(items))
items = [[1,100],[7,100],[1,100],[7,100],[1,100],[7,100],[1,100],[7,100],[1,100],[7,100]]
print(Solution().highFive(items))