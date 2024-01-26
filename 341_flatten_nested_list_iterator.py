from collections import deque

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.data = deque(nestedList)
        self.temp = deque()

    def nested(self):
        print(self.temp)
        if self.temp:
            j = self.temp.popleft()
            if type(j) != int:
                return self.nested()
            else:
                print('j ', j)

                return j

    def next(self):
        """
        :rtype: int
        """
        # for i in self.nestedList:
        if self.hasNext():
            x = self.data.popleft()

            if type(x) != int:
                self.temp = deque(x)
                while self.temp:
                    return self.nested()
            else:
                self.temp = deque()
                return x
        else:
            return False

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.data:
            return True
        else:
            return False


# Your NestedIterator object will be instantiated and called as such:
nestedList = [[1,1],2,[1,[1]]]
i, v = NestedIterator(nestedList), []

while i.hasNext():
    j = i.next()
    v.append(j)
print(v)