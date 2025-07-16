from typing import List
class Solution:
    def twoSum(self,
               numbers: List[int],
               target: int
               ) -> List[int]:
        for l in range(len(numbers)):
            subtract = target - numbers[l]
            for r in range(l+1,len(numbers)):
                if subtract == numbers[r]:
                    return [l+1, r+1]

        return [l+1, r+1]


class Solution:
    def twoSum(self,
               numbers: List[int],
               target: int
               ) -> List[int]:
        left, right = 0, len(numbers) -1
        while left < right:
            current_sum = numbers[left] + numbers[right]
            if current_sum < target:
                left += 1
            elif current_sum == target:
                return [left+1, right+1]
            else:
                right -= 1


numbers = [2, 7, 11, 15]
target = 9
print(Solution().twoSum(numbers, target))
numbers = [2,3,4]
target = 6
print(Solution().twoSum(numbers, target))
numbers = [-1,0]
target = -1
print(Solution().twoSum(numbers, target))
numbers = [0,1,2,3,4,5]
target = 9
print(Solution().twoSum(numbers, target))
numbers = [0,0,3,4]
target=0
print(Solution().twoSum(numbers, target))
numbers = [3,24,50,79,88,150,345]
target = 200
print(Solution().twoSum(numbers, target))
