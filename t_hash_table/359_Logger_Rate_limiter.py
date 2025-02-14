# #359 Logger Rate Limiter
#
# # Design a logger system that receives a stream of messages along with their timestamps. Each unique message should only be printed at most every 10 seconds (i.e. a message printed at timestamp t will prevent other identical messages from being printed until timestamp t + 10).
#
# # All messages will come in chronological order. Several messages may arrive at the same timestamp.
# Implement the Logger class:
#
# Logger() Initializes the logger object.
# bool shouldPrintMessage(int timestamp, string message) Returns true if the message should be printed in the given timestamp, otherwise returns false.


class Logger:

    def __init__(self):
        self.map = {}
    def shouldPrintMessage(self, timestamp, message):
        if message in self.map and timestamp < self.map[message]:
            return False

        self.map[message] = timestamp + 10
        return True



# Your Logger object will be instantiated and called as such:
obj = Logger()
timestamp = 1
message='foo'
param_1 = obj.shouldPrintMessage(timestamp, message)
print(param_1)
timestamp = 2
message='bar'
param_1 = obj.shouldPrintMessage(timestamp, message)
print(param_1)
timestamp = 3
message='foo'
param_1 = obj.shouldPrintMessage(timestamp, message)
print(param_1)
timestamp = 8
message='bar'
param_1 = obj.shouldPrintMessage(timestamp, message)
print(param_1)
timestamp = 10
message='foo'
param_1 = obj.shouldPrintMessage(timestamp, message)
print(param_1)
timestamp = 11
message='foo'
param_1 = obj.shouldPrintMessage(timestamp, message)
print(param_1)