# Definition for singly-linked list.
class ListNode:
    def __init__(self,
                 val=0,
                 next=None
                 ):
        self.val = val
        self.next = next


a_2 = ListNode(2)
a_4 = ListNode(4)
a_3 = ListNode(3)
a_2.next = a_4
a_4.next = a_3
a_3.next = None

a_5 = ListNode(5)
a_6 = ListNode(6)
a_4 = ListNode(4)
a_5.next = a_6
a_6.next = a_4
a_4.next = None


from typing import List, Optional
import copy
class Solution:

    def extractNumber(self, l: ListNode):
        number_1 = 0
        power = 0
        while l:
            number_1 += l.val*(10**power)
            power += 1
            l = l.next

        return number_1
    def addTwoNumbers(self,
                      l1: Optional[ListNode],
                      l2: Optional[ListNode]) -> Optional[ListNode]:

        number1 = self.extractNumber(l1)
        number2 = self.extractNumber(l2)
        total = number1 + number2
        newNode = ListNode()
        root = newNode
        while total != 0:
            remainder = total%10
            total = total//10

            # new_num = new_num*10 + remainder
            newNext = ListNode(remainder)
            newNode.next = newNext
            newNode = newNext

        return root.next


a = Solution().addTwoNumbers(a_2, a_5)
print(a.next.val)

def print_list(node):
    while node:
        print(node.val, end=" -> ")
        node = node.next
    print("None")

print_list(a)



