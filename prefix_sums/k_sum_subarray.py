#Find the number of subarrays in an integer array that sum to k.
#Subarray maintains the order/direction
# def subarray_sum_to_k(nums, k):
#     count = 0
#     prefix_sums_map = {0: 1}
#     curr_prefix_sum = 0
#     for num in nums:
#         curr_prefix_sum += num
#         if curr_prefix_sum - k in prefix_sums_map:
#             count += prefix_sums_map[curr_prefix_sum - k]
#
#         freq = prefix_sums_map.get(curr_prefix_sum, 0)
#         prefix_sums_map[curr_prefix_sum] = freq + 1
#
#     return count


def subarray_sum_to_k(nums, k):
    prefix_sum = {}
    count = 0
    sum_prefix = 0
    #T=O(n)
    #S=O(m~n)
    for x in nums:
        sum_prefix += x
        remain = sum_prefix - k
        if remain == 0 and remain not in prefix_sum:
            prefix_sum[0] = 1

        if remain in prefix_sum:
            count += prefix_sum[remain]
        else:
            freq = prefix_sum.get(sum_prefix, 0)
            prefix_sum[sum_prefix] = freq + 1

    return count


nums = [1, 2, -1, 1, 2]
k=3
print(subarray_sum_to_k(nums, k))

nums=[1,2,0, -1,1,2,0, -3]
k=3
print(subarray_sum_to_k(nums, k))

nums=[1,2,0,-1,0,0,1,2,0,-3]
k=3
print(subarray_sum_to_k(nums, k))
