from typing import List
def product_array_without_current_element(
        nums: List[int]
):
    left_result = [1]
    #T=O(n)
    #S=O(n)
    for x in range(len(nums)-1):
        left_result.append(left_result[-1] * nums[x])

    #T=O(n)
    #Space complexity is O(1) because only memory we are using is for result.
    right_multiply = 1
    for i in range(len(nums)-1, -1, -1):
        left_result[i] = left_result[i]*right_multiply
        right_multiply *= nums[i]

    return left_result

nums = [2, 3, 1, 4, 5]
print(product_array_without_current_element(nums))
