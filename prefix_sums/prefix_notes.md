Advantages of prefix sum array:
1) Efficient for multiple queries:
2) Time complexity:
- Summing over a range of index and over multiple times can be
O(mxn).
- Building the prefix sum takes O(n) time initially. Each query thereafter
takes O(1) for each query therefore O(n+m) for m queries.


