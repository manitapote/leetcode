#7 Reverse Integer

# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
#
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
#


# class Solution:
#     def reverse(self, x):
#         if x % 10 == x:
#             return x
#
#         sign_x = '+'
#         if x * (-1) >= 0:
#             sign_x = '-'
#             x = x * (-1)
#
#         result = []
#         while x > 0:
#             t = x % 10
#             x = x // 10
#
#             result.append(t)
#
#         reverse = 0
#         total = len(result) -1
#         for i in result:
#             reverse+= i*pow(10,total)
#             total = total -1
#
#         if reverse >= pow(2, 31):
#             return False
#
#         if sign_x == '-':
#             reverse = reverse * -1
#
#         return reverse


class Solution:
    def reverse(self, x):
        sign_x = '+'
        if x * (-1) >= 0:
            sign_x = '-'
            x = x * (-1)

        result = ''
        while x > 0:
            t = x % 10
            x = x // 10

            result = result + str(t)

        if int(result) >= pow(2, 31):
            return 0

        if result[0] == '0':
            result = result.replace('0',
                                    '',
                                    1
                                    )

        if sign_x == '-':
            result = '-' + result

        return int(result)


x =-123

a = Solution()
print(a.reverse(x))

x = 120
a = Solution()
print(a.reverse(x))

x = 1534236469
a = Solution()
print(a.reverse(x))


x = 5000000000000000000000000000000005
a = Solution()
print(a.reverse(x))


# Comments:
# Yes, above solution works but this qns seems to be more about memory vs. time
# usage. String takes more memory than integers.
# Similarly, a list of integer occupies a fixed memory of 32 bit compared to
# string of character of integers. Each character occupies a byte of memory.
# For time efficient, using string to reverse the number is more efficient than using
# list to store and again running loop to multiply by 10^xx.