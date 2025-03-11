def find_height(heights, k):
    left = 0
    right = max(heights)

    while left < right:
        mid = (left + right) // 2

        #total wood is in descending order
        if cut_wood(mid, heights) >= k:
            left = mid + 1
        else:
            right = mid - 1

    return right
def cut_wood(h, heights):
    total = 0
    for x in heights:
        if x > h:
            total = total + (x - h)
    return total


heights = [2,6,3,8]
k=2
print(find_height(heights, k))