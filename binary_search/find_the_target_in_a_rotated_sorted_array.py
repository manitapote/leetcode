#A rotated sorted array is an array of numbers sorted in ascending order, in which a portion of the array is moved from
#the beginning to the end. For example, a possible rotation of [1,2,3,4,5] is [3,4,5,1,2], where the first two numbers
#are moved to the end.

#Given a rotated array of unique numbers, return the index of a target value. If the target value is not present
#return -1.

def find_index(nums, target):
    left = 0
    right = len(nums) - 1
    print('Right :', right, ' Left :', left)
    while left < right:
        mid = (left + right) // 2
        print('Right :', right, ' Left :', left, ' Mid: ', mid, ' Nums mid: ', nums[mid], ' Nums right: ', nums[right],
              ' Nums left: ', nums[left])

        if nums[mid] == target:
            return mid
        elif nums[mid] <= nums[right]:
            if nums[mid] <= target < nums[right]:
                left = mid + 1
            else:
                right = mid - 1
        else:
            if nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = left + 1

        print('Right :', right, ' Left :', left)

    return left if nums[left] == target else -1

nums = [8,9,1,2,3,4,5,6,7]
target = 1
print(find_index(nums, target))