#9 Palindrome Number

# Given an integer x, return true if x is a
# palindrome, and false otherwise.

# class Solution:
#     def isPalindrome(self, x):
#         if x == 0:
#             return True
#
#         pal = ''
#
#         sign = 1
#         if x * -1 > 0:
#             sign = -1
#
#         j = x * sign
#
#         while j > 0:
#             t = j % 10
#             j = j // 10
#
#             pal+= str(t)
#
#         if x == int(pal):
#             return True
#         else:
#             return False

class Solution:
    def isPalindrome(self, x):
        if str(x) == str(x)[::-1]:
            return True
        else:
            return False

x = 121
a = Solution()
print(a.isPalindrome(x))

x = -121
a = Solution()
print(a.isPalindrome(x))

x = 10
a = Solution()
print(a.isPalindrome(x))

x = 0
a = Solution()
print(a.isPalindrome(x))