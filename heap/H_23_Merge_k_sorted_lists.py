# Definition for singly-linked list.

from typing import List, Optional
import  heapq
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeKLists(self,
                    lists: List[Optional[ListNode]]
                    ) -> Optional[ListNode]:

        heap = []
        n = len(lists)
        dummy = ListNode(None)
        current = dummy
        for node in lists:
            if node:
                heapq.heappush(heap, node)

        while heap:
            new_node = heapq.heappop(heap)
            current.next = new_node
            current = current.next

            if new_node.next:
                heapq.heappush(heap, new_node.next)

        return dummy.next


#O(nlog(n)) n => number of linkedlist
#O(nlog(k))

#O(n)


