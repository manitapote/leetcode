def binary_search(a, k, start, end):
    if end > start:
        length = start + end
        mid = length // 2

        if a[mid] == k:
            return mid
        elif a[mid] > k:
            return binary_search(a, k, start, mid - 1)
        elif a[mid] < k:
            return binary_search(a, k, mid + 1, end)
    else:
        return -1


a = [1,2,3,4,5,6]
k = 0

j = binary_search(a, k , 0, len(a))

print(j)

