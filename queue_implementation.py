#Queue as list
queue = []
queue.append('a')
queue.append('b')
queue.append('c')

print(queue)
print(queue.pop(0))
print(queue.pop(0))
print(queue.pop(0))

print(queue)

#deque implementation, benefit is that quicker append and pop operations
# from both end of container
from collections import deque
q = deque()
q.append('a')
q.append('b')
q.append('c')

print(q)
print(q.popleft())
print(q.popleft())
print(q.popleft())
print(q)

from queue import Queue
q = Queue(maxsize=3)
# q = queue(maxsize = 3)
print(q.qsize())
q.put('a')
q.put('b')
q.put('c')
print("\nFull: ", q.full())
print("\nElements dequeued from the queue")
print(q.get())
print(q.get())
print(q.get())
print("\nEmpty: ", q.empty())
q.put(1)
print("\nEmpty: ", q.empty())
print("Full: ", q.full())


print(q.empty())
print(q.full())


