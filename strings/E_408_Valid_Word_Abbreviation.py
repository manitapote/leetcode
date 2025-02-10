# #408 Valid Word Abbreviation
#
# A string can be abbreviated by replacing any number of non-adjacent, non-empty substrings with their lengths. The lengths should not have leading zeros.
#
# For example, a string such as "substitution" could be abbreviated as (but not limited to):
#
# "s10n" ("s ubstitutio n")
# "sub4u4" ("sub stit u tion")
# "12" ("substitution")
# "su3i1u2on" ("su bst i t u ti on")
# "substitution" (no substrings replaced)

import re
class Solution:
    def validWordAbbreviation(self, word, abbr):
        #invalid cases
        #s55n (replaced substring adjacent)
        #s010n (leading zeros)
        #s0ubstitution (replaces an empty string)

        #can not be no substitution

        #length is equal
        #
        # x = re.findall(r'[1-9]\d*', abbr)
        # sum_number = sum([int(i) for i in x])
        # y = re.split(r'[1-9]\d*', abbr)

        word_pointer = abbr_pointer = 0
        while word_pointer < len(word) and abbr_pointer < len(abbr):
            if abbr[abbr_pointer].isdigit():
                steps = 0
                if abbr[abbr_pointer] == 0:
                    return False
                while abbr_pointer < len(abbr) and abbr[abbr_pointer].isdigit():
                    steps = steps * 10 + int(abbr[abbr_pointer])
                    abbr_pointer += 1

                word_pointer += steps
            else:
                if word[word_pointer] != abbr[abbr_pointer]:
                    return False

                word_pointer += 1
                abbr_pointer += 1

        return word_pointer == len(word) and abbr_pointer == len(abbr)


word = "internationalization"
abbr = "i12iz4n"
a = Solution()
print(a.validWordAbbreviation(word, abbr))

word = "apple"
abbr = "a2e"
a = Solution()
print(a.validWordAbbreviation(word, abbr))

word = "abbreviation"
abbr = "a10n"
a = Solution()
print(a.validWordAbbreviation(word, abbr))

word ="dadbaddacbddbbccab"
abbr = "7dc3dcccac"
a = Solution()
print(a.validWordAbbreviation(word, abbr))