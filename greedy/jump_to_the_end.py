def canJump(nums):
    destination = len(nums) - 1
    for i in range(len(nums) - 2, -1, -1):
        if i+nums[i] >= destination:
            destination = i

    return destination == 0


#this can be solved like a two pointer problem
nums = [3, 2, 0, 2, 5]
print(canJump(nums))

nums = [2, 1, 0, 3]
print(canJump(nums))