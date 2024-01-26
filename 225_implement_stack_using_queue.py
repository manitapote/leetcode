class MyStack():

    def __init__(self):
        self.data = []
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.data.insert(0, x)

    def pop(self):
        """
        :rtype: int
        """
        return self.data.pop(0)

    def top(self):
        """
        :rtype: int
        """
        return self.data[0]

    def empty(self):
        """
        :rtype: bool
        """
        return not self.data


myStack = MyStack()
myStack.push(1)
myStack.push(2)
print(myStack.top()) # return 2
print(myStack.pop()) # return 2
print(myStack.empty()) # return False


#implementation using deque

#Following implementation is faster compared to above
from collections import deque

class DequeImplement():

    def __init__(self):
        self.data = deque()
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.data.insert(0, x)

    def pop(self):
        """
        :rtype: int
        """
        return self.data.popleft()

    def top(self):
        """
        :rtype: int
        """
        return self.data[0]

    def empty(self):
        """
        :rtype: bool
        """
        return not self.data

myStack = DequeImplement()
myStack.push(1)
myStack.push(2)
print(myStack.top())  # return 2
print(myStack.pop())  # return 2
print(myStack.empty())  # return False
