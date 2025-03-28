def reach_to_end(nums):
    return dfs(0, nums)

def dfs(i, nums):
    if i >= len(nums):
        return True

    if nums[i] == 0:
        return False

    for j in range(1, nums[i]):
        new_index = i + j

        if new_index >= (len(nums) - 1):
            return True

        i = nums[new_index]

        if dfs(i, nums) == True:
            return True

    return False

nums = [3, 2, 0, 2, 5]
print(reach_to_end(nums))

nums = [2, 1, 0, 3]
print(reach_to_end(nums))