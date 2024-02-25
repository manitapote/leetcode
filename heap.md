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
-Each element insert or delete O(log(n))<br />







