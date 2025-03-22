from typing import List
def lonely_integer(x: List[int]) -> List:
    res = 0
    for i in x:
        res ^= i
    return res


n = [1, 3, 3, 2, 1]
#This only works if the number of repetition is multiple of 2
print(lonely_integer(n))



# def find_lonely_pixel(matrix):
#     total = 0
#     res = 0
#     for row in matrix:
#         for x in row:
#             res ^= ord(x)
#         if res == ord('B'):
#             total += 1
#         res = 0
#
#     return total
#
# matrix = [["W","W","B"],["W","B","W"],["B","W","W"]]
# print(find_lonely_pixel(matrix))
# matrix = [["B","B","B"],["B","B","W"],["B","B","B"]]
# print(find_lonely_pixel(matrix))

