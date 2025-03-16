import heapq

# class Median:
#     def __init__(self):
#         self.data = []
#
#     def add(self, num):
#         heapq.heappush(self.data, num)
#
#     def get_median(self):
#         index = len(self.data) // 2
#         remain = len(self.data) % 2
#
#         if remain == 0:
#             return (self.data[index-1] + self.data[index])/2
#
#         return  self.data[index+1]


#Time complexity: O(nlog(n))
#Space complexity: O(n)


class Median:
    def __init__(self):
        self.left_max_heap = []
        self.right_min_heap = []

    #elements in max heap should be less and equal to min_heap
    #length of max heap should be equal or one more than the min_heap

    #Time complexity: O(log(n))
    def add(self, data):
        if self.left_max_heap and -self.left_max_heap[0] >= data:
            heapq.heappush(self.left_max_heap, -data)

            if len(self.left_max_heap) - len(self.right_min_heap) > 1:
                heapq.heappush(self.right_min_heap,
                               -heapq.heappop(self.left_max_heap)
                               )
        else:
            heapq.heappush(self.right_min_heap, data)

            if self.right_min_heap and len(self.right_min_heap) > len(self.left_max_heap):
                heapq.heappush(self.left_max_heap,
                               -heapq.heappop(self.right_min_heap)
                               )



    def get_median(self):
        if len(self.left_max_heap) == len(self.right_min_heap):
            return (-self.left_max_heap[0] + self.right_min_heap[0])/2

        return -self.left_max_heap[0]

#Space complexity: O(n)

a = Median()
a.add(3)
a.add(6)
print(a.get_median())
a.add(1)
print(a.get_median())




