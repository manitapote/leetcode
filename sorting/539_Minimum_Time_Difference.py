#539 Minimum Time Difference

# Given a list of 24-hour clock time points in "HH:MM" format, return the minimum minutes difference between any two time-points in the list.
import itertools
class Solution:
    def findMinDifference(self, timePoints):
        max_time = 60*24
        if len(timePoints) > max_time: #has exact time period
            return 0

        nums = sorted([int(x[:2])*60 + int(x[3:]) for x in timePoints])
        #this is a trick to handle the case of 00.XX after the 23:59.
        #It only affects the 00.xx case not others
        nums.append(nums[0]+max_time)

        return min([nums[i+1] - nums[i] for i in range(len(nums) - 1)])









timePoints = ["23:59","00:00"]
print(Solution().findMinDifference(timePoints))
timePoints = ["00:00","23:59","00:00"]
print(Solution().findMinDifference(timePoints))