# # 13 Roman to Integer
# # Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
# # For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.
#
# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:


class Solution:
    def romanToInt(self, s):
        lookup = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        #
        # s = s.replace("IV", "IIII").replace("IX", "VIIII")
        # s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        # s = s.replace("CD", "CCCC").replace("CM", "DCCCC")

        total = 0
        i = 0
        while i < len(s):
            current = lookup[s[i]]

            if i < len(s) - 1:
                next = lookup[s[i+1]]
                if next > current:
                    total = total + (next - current)
                    i = i + 2
                    continue

            total = total + current

            i = i + 1

        return total

s = "MCMXCIV"

# M = 1000, CM = 900, XC = 90 and IV = 4.
a = Solution()
print(a.romanToInt(s))

s = "III"
a = Solution()
print(a.romanToInt(s))

s = "LVIII"
a = Solution()
print(a.romanToInt(s))