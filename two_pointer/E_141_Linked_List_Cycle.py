# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

from typing import Optional
class Solution:
    def hasCycle(self,
                 head: Optional[ListNode]
                 ) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True


        return False


a_3 = ListNode(3)
a_2 = ListNode(2)
a_0 = ListNode(0)
a_4 = ListNode(-4)
a_3.next = a_2
a_2.next = a_0
a_0.next = a_4
a_4.next = a_2

print(Solution().hasCycle(a_3))
