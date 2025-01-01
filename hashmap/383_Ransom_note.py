# 383. Ransom Note
#
# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.
#
# Each letter in magazine can only be used once in ransomNote.
#
# Example 1:
#
# Input: ransomNote = "a", magazine = "b"
# Output: false
#
# Example 2:
#
# Input: ransomNote = "aa", magazine = "ab"
# Output: false
#
#
# Example 3:
#
# Input: ransomNote = "aa", magazine = "aab"
# Output: true
#
# Constraints:
#
# 1 <= ransomNote.length, magazine.length <= 105
# ransomNote and magazine consist of lowercase English letters.

# class Solution(object):
#     def canConstruct(self, ransomNote, magazine):
#         """
#         :type ransomNote: str
#         :type magazine: str
#         :rtype: bool
#         """
#         total_index = len(ransomNote)
#         if len(ransomNote) > len(magazine):
#             return False
#
#         magazine_hash = {}
#         ransomNote_hash = {}
#         for index, character in enumerate(magazine):
#             if character in magazine_hash:
#                 magazine_hash[character] += 1
#             else:
#                 magazine_hash[character] = 1
#
#             if index < total_index:
#                 if ransomNote[index] in ransomNote_hash:
#                     ransomNote_hash[ransomNote[index]] += 1
#                 else:
#                     ransomNote_hash[ransomNote[index]] = 1
#
#         for key in ransomNote_hash:
#             if key not in magazine_hash:
#                 return False
#
#             if ransomNote_hash[key] > magazine_hash[key]:
#                 return False
#
#         return True

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        total_index = len(ransomNote)
        if len(ransomNote) > len(magazine):
            return False

        magazine_hash = {}
        for index, character in enumerate(magazine):
            if character in magazine_hash:
                magazine_hash[character] += 1
            else:
                magazine_hash[character] = 1

        for key in ransomNote:
            if key not in magazine_hash:
                return False

            if magazine_hash[key]<= 0 :
                return False

            magazine_hash[key] -= 1

        return True



ransomNote = 'a'
magazine = 'b'
a = Solution()
print(a.canConstruct(ransomNote, magazine))


#Space complexity
#Time complexity = O(n)