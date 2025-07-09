from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self,
                                 s: str
                                 ):
        if s == '':
            return 0
        hashmap = defaultdict(int)
        left = 0
        substring_length = float('-inf')
        for i, chara in enumerate(s):
            if chara in hashmap and hashmap[chara] >= left:
                #important logic,,, to check if the present position
                #is also duplicate
                left = hashmap[chara]+1

            substring_length = max(substring_length, i-left+1)
            #the length can be calculated using difference instead of slicing array

            hashmap[chara] = i
        print(hashmap, left)
        return substring_length


s = "abcabcbb"
print(Solution().lengthOfLongestSubstring(s))
s = "bbbbb"
print(Solution().lengthOfLongestSubstring(s))
s = "pwwkew"
print(Solution().lengthOfLongestSubstring(s))
s = 'abba'
print(Solution().lengthOfLongestSubstring(s))


#duplicate means keep track of when it occured last time