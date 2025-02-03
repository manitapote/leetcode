# # 146 LRU Cache
#
# Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.
#
# Implement the LRUCache class:
#
# LRUCache(int capacity) Initialize the LRU cache with positive size capacity.
# int get(int key) Return the value of the key if the key exists, otherwise return -1.
# void put(int key, int value) Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
# The functions get and put must each run in O(1) average time complexity

# Design question

class Node:
    def __init__(self, key, val):
        self.val = val
        self.key = key
        self.prev = None
        self.next = None
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left = Node(0,0)
        self.right = Node(0, 0)

        self.left.next = self.right
        self.right.prev = self.left

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        #get the node
        node = self.cache[key]

        #fix the pointers
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev

        print(self.read_values())

        prev = self.right.prev
        node.next = self.right
        self.right.prev = node
        node.prev = prev
        prev.next = node

        self.cache[key] = node

        print(self.read_values())

        #return the value
        return node.val
    def put(self, key: int, value: int) -> None:
        #if key already present
        if key in self.cache:
            node = self.cache[key]
            # fix the left pointers
            prev = self.right.prev
            node.prev = prev
            prev.next = node

            # fix the right pointers
            node.next = self.right
            self.right.prev = node

            print(self.read_values())
            print('Cache lenght :', len(self.cache))
            self.cache[key] = node
            print(self.cache)
            return
        # else:
            #create a node
        node = Node(key, value)

        #fix the left pointers
        prev = self.right.prev
        node.prev = prev
        prev.next = node

        # fix the right pointers
        node.next = self.right
        self.right.prev = node

        print(self.read_values())
        print('Cache lenght :', len(self.cache))
        self.cache[key] = node
        print(self.cache)

        # #check the length of cache and remove
        if len(self.cache) > self.capacity:
            #remove from left
            to_be_removed = self.left.next
            next_toberemoved = to_be_removed.next
            self.left.next = next_toberemoved
            next_toberemoved.prev = self.left
            # print(to_be_removed.val)
            del self.cache[to_be_removed.key]

        # put in the cache
        print(self.read_values())
        print(self.cache)

    def read_values(self):
        values = [0]
        current = self.left.next
        while current is not None:
            values.append(current.val)
            current = current.next
        return values



# Your LRUCache object will be instantiated and called as such:
capacity = 2
obj = LRUCache(capacity)
obj.put(2,1)
obj.put(1,1)
obj.put(2,3)
# obj.put(4,1)
# print(obj.get(1))
# # obj.put(3,3)
# print(obj.get(2))
# obj.put(4, 4)
# print(obj.get(1))
# print(obj.get(3))
# print(obj.get(4))

# param_1 = obj.get(key)
# obj.put(key,value)