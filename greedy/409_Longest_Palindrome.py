# Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.
#
# Letters are case sensitive, for example, "Aa" is not considered a palindrome.

from collections import defaultdict
from collections import Counter
def longestPalindrome(s):
    hash_map = Counter(s)
    odd = 0
    for key, value in hash_map.items():
        if value % 2 != 0:
            odd += 1

    return len(s) if odd == 0 else len(s) - odd + 1


### Properties of palindrome is they have even characters or
### 1 odd character







s = 'abccccdd'
print(longestPalindrome(s))
s = 'a'
print(longestPalindrome(s))