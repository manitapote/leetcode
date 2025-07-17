# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional
class Solution:
    def removeNthFromEnd(self,
                         head: Optional[ListNode],
                         n: int
                         ) -> Optional[ListNode]:

        result = 0
        root = head
        while root:
            result += 1
            root = root.next
        if result == n:
            return head.next

        need = result - n
        i = 1
        root = head
        while root:
            if i == need:
                root.next = root.next.next
            else:
                root = root.next
            i += 1

        return head




a_1 = ListNode(1)
a_2 = ListNode(2)
a_3 = ListNode(3)
a_4 = ListNode(4)
a_5 = ListNode(5)
a_1.next = a_2
a_2.next = a_3
a_3.next = a_4
a_4.next = a_5
n = 1
head = Solution().removeNthFromEnd(a_1, n)
print(head.val)
print(head.next.val)
print(head.next.next.val)
print(head.next.next.next.val)
# while head.next:
#     print(head.val)
#     head = head.next

a_1 = ListNode(1)
n = 1
head = Solution().removeNthFromEnd(a_1, n)
print(head.val)
a_