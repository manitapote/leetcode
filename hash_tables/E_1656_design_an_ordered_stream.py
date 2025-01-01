# 1656. Design an Ordered Stream
# There is a stream of n (idKey, value) pairs arriving in an arbitrary order, where idKey is an integer between 1
# and n and value is a string. No two pairs have the same id.
#
# Design a stream that returns the values in increasing order of their
# IDs by returning a chunk (list) of values after each insertion. The concatenation of all
# the chunks should result in a list of the sorted values.
#
# Implement the OrderedStream class:
#
# OrderedStream(int n) Constructs the stream to take n values.
# String[] insert(int idKey, String value) Inserts the pair (idKey, value)
# into the stream, then returns the largest possible chunk of currently inserted values that appear next in the order.


class OrderedStream(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.stream = [None]*(n+1)
        self.index = 1

    def insert(self, idKey, value):
        """
        :type idKey: int
        :type value: str
        :rtype: List[str]
        """
        self.stream[idKey] = value
        print('inpute ', idKey, ' value ', value)
        print('stream ', self.stream)

        if self.index < idKey:
            self.index = idKey
            return []
        else:
            result = []
            for i in range(idKey, self.index+1):
                if self.stream[i] == None:
                    break
                result.append(self.stream[i])

            return result




# Your OrderedStream object will be instantiated and called as such:
steps = [[9],[9,"nghbm"],[7,"hgeob"],[6,"mwlrz"],[4,"oalee"],[2,"bouhq"],[1,"mnknb"],[5,"qkxbj"],[8,"iydkk"],[3,"oqdnf"]]
for step in steps:
    if len(step) == 1:
        obj = OrderedStream(step[0])
    else:
        idKey = step[0]
        value = step[1]
        param_1 = obj.insert(idKey, value)
        print(param_1)

