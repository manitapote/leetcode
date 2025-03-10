## Sorting Methods

1) Bubble Sort
- Average worst case time complexity is O(n^2). Best case is O(n) when array is sorted already.
- Practical only for small datasets or nearly sorted datasets because of its simplicity.
- How it works: Repeatedly steps through the list, compare adjacent elements, and swaps them if they are in the wrong
order
- Implementation:
```commandline
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
```
One swap of adjacent elements place the largest element at the end.


2) Selection Sort
- Complexity is always O(n^2) for best, average and worst case.
- Use case: Inefficient on large lists and rarely used in practice, but it has consistent performance regardless of
initital order of items.
- How It Works: Works by repeatedly finding the minimum element from the unsorted part of the list and putting it at the beginning.
```commandline
def selection_sort(arr):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr
```

3) Insertion sort
- Complexity: Average and worst-case time complexity is O(n^2). Best case is O(n).
- Use case: Efficient for small data sets or arrays that are already partially sorted.
- How It Works: Builds the final sorted array one item at a time by inserting each new element into its appropriate 
position within the already sorted part.
- Very good for partially sorted arrays
```commandline
#[3,1,2,4,0]
def insertion_sort(arr):
    for i in range(1, len(arr)):
        #i=1,2
        key = arr[i] #key=1, arr[j]=3
        j = i - 1    #j=0,1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j] #j+1=1
            j -= 1
        arr[j + 1] = key #j+1=0
        #[1,3,2,4,0]
    return arr

```

4) Merge Sort
- Complexity: Always O(nlog(n)) in all cases.
- Use case: Useful for sorting large datasets and linked lists.
- How It Works: A divide and conquer algorithm that divides the input array into two halves, calls itself for the
two halves, and then merges the two sorted halves.
```commandline
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        #two merge 
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

    return arr

```

5) Quick sort
- Complexity: Average-case complexity O(nlog(n)), buta worst-case of O (n^2). However worst case is rare.
- Use case: Preferred for arrays due to its in-place sorting (low memory overhead) and average-case efficiency.
- How It Works: Selects a 'pivot' element and partitions the array around the pivot into two sub-arrays, 
- which are then sorted independently.
```commandline
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr.pop()

    items_greater = []
    items_lower = []

    for item in arr:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)

    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)

```
6) Heap sort
- Complexity: O(nlog(n)) in all cases.
- Use case: Good choice when consistent O(nlog(n)) performance is needed. Not stable which can be drawback if stability
is needed.
- How It Works: Converts the array into a heap data structure, repeatedly removing the largest element from the heap
- and adding it to the end of the sorted array.
```commandline
import heapq

def heap_sort(arr):
    heapq.heapify(arr)
    return [heapq.heappop(arr) for i in range(len(arr))]

```

7) Counting sort
- Complexity: O(n+k) where k is the range of the input data
- Use case: efficient when the range of data is not significantly greater than the number of objects to be sorted. Used
for small integers or objects with a small range of key values.
- How It Works: Counts the number of objects that have distinct key values and uses arithmetic
- to determine the position of each key.
```commandline
def counting_sort(arr):
    max_val = max(arr)
    m = max_val + 1
    count = [0] * m
                
    for a in arr:
        count[a] += 1
    i = 0
    for a in range(m):
        for c in range(count[a]):
            arr[i] = a
            i += 1
    return arr

```
8) Radix sort
- Complexity: O(nk) for n keys which have k digits.
- Use Case: Efficient for sorting large volumes of numbers especially when the size of the keys is large.
- How It Works: Sorts numbers digit by digit starting from the least significant digit to the most significant digit,
- using a stable algorithm like counting sort for each digit.
```commandline
def counting_sort_for_radix(input_array, place):
    size = len(input_array)
    output_array = [0] * size
    count_array = [0] * 10

    for i in range(size):
        index = input_array[i] // place
        count_array[index % 10] += 1

    for i in range(1, 10):
        count_array[i] += count_array[i - 1]

    i = size - 1
    while i >= 0:
        index = input_array[i] // place
        output_array[count_array[index % 10] - 1] = input_array[i]
        count_array[index % 10] -= 1
        i -= 1

    for i in range(size):
        input_array[i] = output_array[i]

def radix_sort(arr):
    max_element = max(arr)
    place = 1
    while max_element // place > 0:
        counting_sort_for_radix(arr, place)
        place *= 10
    return arr

```
9) Bucket sort
- Complexity: Average case O(n+k), worst case O(n^2)
- Useful when the inputs is uniformly distributed over a range.
- How It Works: Distributes elements into buckets, sorts the individual buckets, and then concatenates them.
```commandline
def bucket_sort(arr):
    if not arr:
        return arr
    
    # Find maximum value to determine number of buckets
    max_value = max(arr)
    size = max_value / len(arr)

    buckets = [[] for _ in range(len(arr))]
    for i in range(len(arr)):
        j = int(arr[i] / size)
        if j != len(arr):
            buckets[j].append(arr[i])
        else:
            buckets[len(arr) - 1].append(arr[i])

    for i in range(len(arr)):
        insertion_sort(buckets[i])

    result = []
    for i in range(len(arr)):
        result.extend(buckets[i])
    return result

```