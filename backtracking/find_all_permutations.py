from typing import List
def all_permutations(nums: List[int]) -> List:
    return dfs([], nums, [])

def dfs(result, nums, chosen):
    if len(chosen) == len(nums):
        result.append(chosen[:])

        return

    for x in nums:
        if x in chosen:
            continue

        chosen.append(x)

        dfs(result, nums, chosen)

        chosen.remove(x)

    return result


nums = [4, 5, 6]
print(all_permutations(nums))