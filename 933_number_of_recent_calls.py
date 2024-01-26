#933 Number of recent calls
#220 ms, 16.81 mb
from collections import deque

class RecentCounter:
    def __init__(self):
        self.request = deque()

    def ping(self, t: int) -> int:
        # Add the new call time to the deque
        self.request.append(t)

        # Remove calls that are older than 3000 time units from 't'
        while self.request[0] < t - 3000:
            self.request.popleft()

        # Return the number of calls in the last 3000 time units
        return len(self.request)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)



# Your RecentCounter object will be instantiated and called as such:
obj = RecentCounter()
param_1 = obj.ping(1)
# print(1, ' ', param_1)
param_1 = obj.ping(100)
# print(100, ' ', param_1)

param_1 = obj.ping(3001)
# print(3001, ' ', param_1)

x = obj.ping(3002)
print(3002, ' ', x)