# 680. Valid Palindrome II

# Given a string s, return true if the s can be palindrome after deleting at most one character from it.


#Palindrome is two pointer problem
class Solution:
    def validPalindrome(self, s):
        #palindrome : same from front and back
        #remove each word and check if remaining word is same

        if s == s[::-1]:
            return True

        if len(s) <= 1:
            return True

        # for i in range(len(s)):
        #     temp = s[:i] + s[i+1:]
        #
        #     if temp == temp[::-1]:
        #         return True
        #
        # return False
        #above will have memory problem

        left_pointer = 0
        right_pointer = len(s) - 1

        while left_pointer < right_pointer:
            if s[left_pointer] != s[right_pointer]:
                #when we move left
                #when we move right
                skipL = s[left_pointer+1: right_pointer+1]
                skipR = s[left_pointer:right_pointer]

                return skipR == skipR[::-1] or skipL == skipL[::-1]

            left_pointer += 1
            right_pointer -= 1

        return True







s = 'aba'
a = Solution()
print(a.validPalindrome(s))

s = "abca"
a = Solution()
print(a.validPalindrome(s))

s = "abc"
a = Solution()
print(a.validPalindrome(s))

s = "aaab"
a = Solution()
print(a.validPalindrome(s))