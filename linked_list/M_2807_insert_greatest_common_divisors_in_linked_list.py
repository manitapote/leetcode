# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

import math
from typing import Optional, List
class Solution:
    def insertGreatestCommonDivisors(self, 
                                     head: Optional[ListNode]
                                     ) -> Optional[ListNode]:
        dummy  = head
        while dummy and dummy.next:
            #gcd
            current = dummy.val
            next_val = dummy.next.val

            gcd = math.gcd(current, next_val)

            #new node
            new_node = ListNode()
            new_node.val = gcd
            new_node.next = dummy.next

            #save
            dummy.next = new_node
            dummy = dummy.next.next

        return head

    def create(self, list1: List[any]):
        all_obj = []
        for i in list1:
            obj = ListNode(i, next=None)
            all_obj.append(obj)

        for i, obj in enumerate(all_obj):
            if i == (len(all_obj) - 1):
                break
            obj.next = all_obj[i+1]
        return all_obj[0]

list1 = [18,6,10,3]
list2 = [2,3,4]

a = Solution()
list1 = Solution().create(list1)
list2 = Solution().create(list2)

# while list1:
#     print(list1.val)
#     list1 = list1.next

start_node = a.insertGreatestCommonDivisors(list1)
print('here :')
while start_node:
    print(start_node.val)
    start_node = start_node.next
