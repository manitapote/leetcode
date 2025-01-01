
# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists into one sorted list. 
# The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self,
                      list1: Optional[ListNode], 
                      list2: Optional[ListNode]
                      ) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        # Attach the remainder of list1 or list2
        tail.next = list1 if list1 else list2

        return dummy.next
    
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
    
list1 = [1,2,4]
list2 = [2,3,4]

a = Solution()
list1 = Solution().create(list1)
list2 = Solution().create(list2)


start_node = a.mergeTwoLists(list1, list2)
print('here :')
while start_node:
    print(start_node.val)
    start_node = start_node.next