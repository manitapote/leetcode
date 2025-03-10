def find_index(nums, target):
    left = 0
    right = len(nums)

    if right == 0:
        return None

    return search(nums, target, left, right)


def search(nums, target, left, right):
    while left < right:
        mid = left + (right - left) // 2

        ### Lower bound of the problem
        if nums[mid] > target:
            right = mid
        else:
            left = mid + 1

        search(nums, target, left, right)

    return left

#ESPDN
# nums = []
# nums = [1]
# nums = [-2,1]
# nums = [2,2]
# nums = [1,2]
# target = 3

nums = [1,2,4,5,7,8,9]
target = 4
print(find_index(nums, target))

nums = [-1,2,4,5,7,8,9]
target = -6
print(find_index(nums, target))

nums = [1,2,4,5, 7,8,9]
target = 6
print(find_index(nums, target))