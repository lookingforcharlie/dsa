class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ''
        for i in s.lower():
            if i.isalnum():
                new_s += i
        return new_s == new_s[::-1]