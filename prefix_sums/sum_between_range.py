#Given an integer array, write a function which returns the sum of values between two indexes
class SumBetweenRange:
    def __init__(self, nums):
        self.result = [nums[0]]
        #T=O(n)
        #S=O(n)
        for i in range(1, len(nums)):
            self.result.append(self.result[-1] + nums[i])

    #T=O(1)
    #S=O(1)
    def sum_range(self, start_index, end_index):
        # print(self.result)
        if start_index == 0:
            return self.result[end_index]
        return self.result[end_index] - self.result[start_index - 1]


nums=[3,-7,6,0,-2,5]
a = SumBetweenRange(nums)
print(a.sum_range(0, 3))
print(a.sum_range(2,4))
print(a.sum_range(2,2))
print(a.sum_range(0, 4))