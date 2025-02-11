#796 Rotate String

# Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.
#
# A shift on s consists of moving the leftmost character of s to the rightmost position.
#
# For example, if s = "abcde", then it will be "bcdea" after one shift.

class Solution:
    def rotateString(self, s, goal):
        #length not equal
        if len(s) != len(goal):
            return False

        if s == goal:
            return True

        right_pointer = 1
        while right_pointer < len(s):
            if s[right_pointer:] + s[:right_pointer] == goal:
                return True
            right_pointer += 1

        return False


s = "abcde"
goal = "cdeab"
a = Solution()
print(a.rotateString(s, goal))

s = "abcde"
goal = "abced"
a = Solution()
print(a.rotateString(s, goal))