from typing import List
def all_permutations(nums: List[int]) -> List:
    return dfs([], nums, [])

def dfs(result, nums, chosen):
    if len(chosen) == len(nums):
        #O(n)
        result.append(chosen[:])

        return

    #O(n)
    for x in nums:
        #O(n)
        if x in chosen:
            continue

        chosen.append(x)

        #T=O(n!)
        dfs(result, nums, chosen)

        chosen.remove(x)

    return result


nums = [4, 5, 6]
print(all_permutations(nums))
#T= O(n!)*(O(n)*O(n) + O(n))
#T=O(n^2. n!)