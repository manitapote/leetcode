from collections import deque
class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        self.students = deque(students)
        self.sandwiches = deque(sandwiches)

        self.call()

    def call(self):
        if len(self.sandwiches) == 0:
            return len(self.students)

        if self.sandwiches[0] == self.students[0]:
            self.sandwiches.popleft()
            self.students.popleft()
        else:
            a = self.students.popleft()
            self.students.appendleft(a)

        self.call()

        # while sandwich in self.sandwiches:
        #     while student in self.students:
        #         if student == sandwich:
        #             self.sandwiches.popleft()
        #         else:
        #             a = self.students.popleft()
        #             self.students.appendleft(a)

        # return len(self.students)

students = [1,1,0,0]
sandwiches = [0,1,0,1]

a = Solution()
print(a.countStudents(students, sandwiches))