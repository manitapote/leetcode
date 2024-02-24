from collections import deque
class MyQueue(object):

    def __init__(self):
        self.stack = deque()
    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        return  self.stack.appendleft(x)

    def pop(self):
        """
        :rtype: int
        """
        return self.stack.pop()

    def peek(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def empty(self):
        """
        :rtype: bool
        """

        if self.stack:
            return False
        else:
            return True