# 11 Container with most water

class Solution:
    def maxArea(self, height):
        max_area = 0
        left = 0
        right = len(height)-1

        while left != right:
            area = (height[right] - height[left])*(right - left)
            if max_area < area:
                max_area = area

            if height[left] < height[right]:
                left +=1
            else:
                right-=1

        return max_area


height = [1,8,6,2,5,4,8,3,7]
a = Solution()
print(a.maxArea(height))


