# # 346 Moving Average from Data Stream
#
# Given a stream of integers and a window size, calculate the moving average of all integers in the sliding window.
#
# Implement the MovingAverage class:
#
# MovingAverage(int size) Initializes the object with the size of the window size.
# double next(int val) Returns the moving average of the last size values of the stream.


class MovingAverage:

    def __init__(self, size: int):
        self.stack = [0]*size
        self.sum = 0
        self.ele = 0
    def next(self, val: int) -> float:
        past = self.stack.pop(0)
        self.stack.append(val)

        self.sum = self.sum - past + val

        if self.ele < len(self.stack):
            self.ele += 1

        return self.sum/self.ele

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)

# ["MovingAverage", "next", "next", "next", "next"]
# [[3], [1], [10], [3], [5]]


a = MovingAverage(3)
print(a.next(1))
print(a.next(10))
print(a.next(3))
print(a.next(5))
print(a.next(8))