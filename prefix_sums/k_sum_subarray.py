#Find the number of subarrays in an integer array that sum to k.
#Subarray maintains the order/direction
def subarray_sum_to_k(nums, k):
    count = 0
    prefix_sums_map = {0: 1}
    curr_prefix_sum = 0
    for num in nums:
        curr_prefix_sum += num
        if curr_prefix_sum - k in prefix_sums_map:
            count += prefix_sums_map[curr_prefix_sum - k]

        freq = prefix_sums_map.get(curr_prefix_sum, 0)
        prefix_sums_map[curr_prefix_sum] = freq + 1

    return count

nums = [1, 2, -1, 1, 2]
nums=[1,2,0, -1,1,2,0, -3]
nums=[1,2,0,-1,0,0,1,2,0,-3]
k=3
print(subarray_sum_to_k(nums, k))