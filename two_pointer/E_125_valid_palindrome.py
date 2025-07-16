class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0:
            return True
        if len(s) == 1:
            return True
        if set(s) == ' ':
            return True

        s = s.lower()
        s = s.replace(' ', '')

        s = [s[i] for i in range(len(s)) if s[i].isalnum()]
        # s = [s[i] for i in range(len(s)) if not s[i].isdigit()]

        l = 0
        for r in range(len(s) -1, len(s)//2-1, -1):
            if l == r:
                return True
            if s[l] != s[r]:
                return False
            l += 1

        return True



s = "A man, a plan, a canal: Panama"
print(Solution().isPalindrome(s))
s = "race a car"
print(Solution().isPalindrome(s))
s = " "
print(Solution().isPalindrome(s))