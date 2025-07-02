def jumpToEnd(nums):
    destination = len(nums) - 1

    for i in range(len(nums)-1, -1, -1):
        #value of index >= (destination index - current index)
        if i + nums[i] >= destination:
            destination = i

    return destination == 0

nums = [3, 2, 0, 2, 5]
print(jumpToEnd(nums))
nums = [2, 1, 0, 3]
print(jumpToEnd(nums))
