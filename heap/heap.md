## Heaps

Binary tree: <br />
if a node is at index i: <br />
its left child is at -- 2*i <br />
its right child is at -- 2*i + 1 <br />
its parent is at -- int(i/2) +1 if i == odd <br />
if any of the node do not have child, then fill with empty space to make to follow 
the formula. <br /><br />

Complete Full Binary Tree <br />
Height of a binary tree has all elements no space remaining. <br />
The number of nodes: (2^(n+1) - 1) <br />
No missing element or empty gaps between elements <br />
Height of complete binary tree is minimum and log(n) <br /><br />

Max Heap: A complete binary tree where elements are arranged in 
descending order starting with the
largest one. Duplicates are allowed<br />
Insert in max heap: Add element as leaf, check the parent and swap. 
The max time is O(log(n)) and min O(1). <br />
Delete operation: Only root element can be removed. Complete binary tree property should be preserved.
Start from the right most child node, swap that child to root and adjust from root to 
all child to maintain the max heap. Max time O(log(n)) <br />
The elements removed from the heap can be filled in the last empty spot. This process will
sort the elements and this is heap sort. <br /><br />


Min Heap: Complete binary tree with elements arranged in ascending order starting with largest
one. <br />

Heap sort: 
- Create a heap Time complexity O(nlog(n)), Adjustment of element is from leaf to parent
- Delete elements one by one , Time complexity O(nlog(n)) <br /><br />

Heapify: 
- Creating a heap by comparing to children starting from right side of array.
- Time complexity O(n)<br /><br />

Priority Queues: <br />
-Each element insert or delete O(log(n))<br /><br />

Python heapq: Each parent node is small or equal to any of its children. It is a min-heap.<br />
Functions: <br />
**heapq.heappush(heap, item)** => Adds new item to heap maintaining the heap invariant <br />
**heapq.heappop(heap)** => returns the smallest item from the heap maintaining heap property. If heap is empty, 
'IndexError' is raised <br />
**heapq.heappushpop(heap, item)** => Pushes new item on the heap, then pops and returns the smallest item from
the heap. This is more efficient than heappush() AND heappop(). <br />
**heapq.heapify()** => transforms x list into heap. <br />
**heapq.heapreplace(heap, item)** => Pop and returns the smallest item from the heap and also pushes the new item.
The heap size does not change. If empty, 'IndexError' is raised. The function is more efficient than 'heappop()' and 
'heappush()', and can be more appropriate when using a fixed-size heap. <br />
**heapq.merge(\*iterables, key=None, reverse=False)** =>  The iterables is multiple list, not
list of list. All the lists need to be sorted either in ascending or descending,
else error is thrown. If the list is a dictionary element,
key name can be specified like this: key=lambda x: x['age'].
Reverse to order in descending order<br />
**heapq.nlargest(n, iterable, key=None)** =>  Returns the largest 'n' elements from iterable. If the key is
provided specified that specific key is used to compare the elements. The iterable do not have to be
sorted in first place. It is memory efficient and convenient to handle multiple sorted data structures.<br />
**heapq.nsmallest(n, iterable, key=None)** =>  Returns the smallest 'n' elements from iterable. If the key is
provided specified that specific key is used to compare the elements. The iterable do not have to be
sorted in first place.<br /><br />

ShiftUp: h*n/2 + (h-1)*n/4 +... + (0*1) = O(nlog(n)) <br />
ShiftDown: Time complexity O(n) => 0*n/2 + 1*n/8 .... h*1 = h*n/(2^(n+1)) ~ n <br />
ShiftUp is needed to perform inserts into an existing heap. <br />
ShiftDown is more efficient for building heap (this is not same as sorting)
and it can be O(n). <br />
sorting heap is O(nlog(n))<br />








