# class Solution:
#     def __init__(self):
#         self.text = 'balloon'

#     def maxNumberOfBalloons(self, text: str) -> int:
#         count = {}
#         for character in text:
#             if character in count:
#                 count[character] += 1
#             else:
#                 count[character] = 1
        
#         number = 0
#         while True:
#             for i, key in enumerate(self.text):
#                 if (key in count) and count[key] != 0:
#                     count[key] -= 1
#                 else:
#                     return number
            
#             number += 1

#Time complexity: O(n)
#space complexity: O(1)
            
#Short solution
# from collections import Counter

#Time complexity: cO(n)
# class Solution:
#     def maxNumberOfBalloons(self, text: str) -> int:
#         cnt = Counter(text)
       
#         return min(cnt['b'], 
#                    cnt['a'],
#                     cnt['l'] // 2, 
#                     cnt['o'] //2,
#                     cnt['n']
#                     )

#Shorter solution
#Time complexity: O(n)
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        return min(text.count('b'),
                   text.count('a'),
                   text.count('l')//2,
                   text.count('o')//2,
                   text.count('n')
                   )

obj = Solution()
text = "loonbalxballpoon"
text = 'nlaebolko'
print(obj.maxNumberOfBalloons(text))