def next_largest_number_to_right(nums):
    stack = []
    result = [0]*len(nums)
    for i, x in enumerate(nums[::-1]):
        while stack and x >= stack[-1]:
            stack.pop()

        result[i] = stack[-1] if stack else -1
        stack.append(x)

    return result


#Directional property:
#It is not window problem, as it is not fixed window and we need result for each element, not a single combination
#Not a pointer problem as we have a directional property
#monotonic descreasing order
#Time complexity: O(n)
#Space complexity: O(n)
nums = [5,2,4,6,1]
print(next_largest_number_to_right(nums))