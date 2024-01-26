# 35. Search Insert Position Easy Topics Companies
# Given asorted array of distinct integers and a target value, return the index if the target is found.
# If not, return the index where it would be if it were inserted in order.
#
# You must write an algorithm with O(log n) runtime complexity.
#
# Example
# 1:
#
# Input: nums = [1, 3, 5, 6], target = 5
# Output: 2
# Example
# 2:
#
# Input: nums = [1, 3, 5, 6], target = 2
# Output: 1
# Example
# 3:
#
# Input: nums = [1, 3, 5, 6], target = 7
# Output: 4


def binary_search(a, k, start, end):
    print('Start :', start)
    print('End :', end)

    if end > start:
        length = start + end
        mid = length // 2

        print('mid ', mid)
        if a[mid] == k:
            return mid
        elif a[mid] > k:
            return binary_search(a, k, start, mid - 1)
        elif a[mid] < k:
            return binary_search(a, k, mid + 1, end)
    else:
        index = (end+start) // 2
        if index < 0:
            return 0
        if index > len(a) - 1:
            return index
        if a[index] >= k:
            return index
        else:
            return index + 1


a = [1,3,5,6]

print(len(a))
k = 0

j = binary_search(a, k , 0, len(a))

print(j)

