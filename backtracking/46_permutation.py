def permutation(nums):
    result = []
    path = []
    def backtrack(nums, result, path):
        if len(path) == len(nums):
            result.append(path[:])
            return

        for index in range(0, len(nums)):
            if nums[index] in path:
                continue

            path.append(nums[index])
            backtrack(nums, result, path)
            path.pop()

    backtrack(nums, result, path)
    return result


nums = [1, 2, 3]
print(permutation(nums))