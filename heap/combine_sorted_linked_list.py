class Node:
    def __init__(self, data):
        self.next = None
        self.data = data


    def __lt__(self, other):
        return self.data < other.data
class linked_list():
    def __init__(self):
        self.head = None
    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node

    def display(self):
        current = self.head

        while current:
            print(current.data)
            current = current.next

        # print(current.next)


one = [1, 6]
two = [1, 4, 6]
three = [3, 7]

one_link = linked_list()
for x in one:
    one_link.append(x)

print(one_link.display())

two_link = linked_list()
for x in two:
    two_link.append(x)
print(two_link.display())

three_link = linked_list()
for x in three:
    three_link.append(x)
print(three_link.display())

import heapq
from typing import List
def combine_sorted_linked_lists(lists):
    x = []
    k = 3
    result = []

    for node in lists:
        x.append(node.head)

    head = Node(None)
    curr = head
    while x:
        heapq.heapify(x)
        min_x = heapq.heappop(x)

        result.append(min_x.data)

        curr.next = min_x
        curr = curr.next

        if min_x.next:
            heapq.heappush(x, min_x.next)

    return result

lists = [one_link, two_link, three_link]
result = combine_sorted_linked_lists(lists)
print(result)






