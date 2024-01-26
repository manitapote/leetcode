def binary_search(a, k):
    start = 0
    end = len(a)

    while start <= end:

        print('Start ,', start, ' end ', end)
        mid = (start + end) // 2

        if mid > len(a) - 1:
            return -1
        if a[mid] == k:
            return mid
        elif a[mid] > k:
            end = mid -1
        elif a[mid] < k:
            start = mid + 1
    return -1



a = [1,2,3,4]
k = 0
print(binary_search(a, k))
