#10th Jun

#169 Majority Element
# Given an array nums of size n, return the majority element.

# The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element
# always exists in the array.

from typing import List
# def majority_element(nums: List):
#     nums.sort()
#     return nums[len(nums)//2]

#The above has O(nlog(n)) and O(1) time and space complexity.

def majority_element(nums: List):
    count = m = 0
    for x in nums:
        if count == 0:
            m = x
            count += 1
        else:
            if x == m:
                count += 1
            else:
                count -= 1

    return m

#This is Boyer-Moore algorithm and has O(n) and O(1) time complexity.

nums = [3,2,3]
print(majority_element(nums))

nums = [2,2,1,1,1,2,2]
print(majority_element(nums))


