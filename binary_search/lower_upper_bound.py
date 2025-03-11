def lower_bound(nums, target, left, right):
    while left < right:
        mid = (left + right) //2
        if nums[mid] >= target:
            right = mid
        else:
            left = mid + 1
        lower_bound(nums, target, left, right)

    return left

def upper_bound(nums, target, left, right):

    while left < right:
        mid = (left + right) // 2

        if nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

        upper_bound(nums, target, left, right)

    return left
def index(nums, target):
    if target > nums[-1] or target < nums[0]:
        return [-1,-1]

    return [lower_bound(nums, target, 0 , len(nums)),
            upper_bound(nums, target, 0, len(nums))
            ]
    # return lower_bound(nums, target, 0 , len(nums))
nums = [1, 2, 3, 4, 4, 4, 5, 6, 7, 8, 9, 10, 11]
target = 2
print(index(nums, target))