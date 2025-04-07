class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # .find() return the index of the first occurrence of the substring within the string
        return haystack.find(needle)