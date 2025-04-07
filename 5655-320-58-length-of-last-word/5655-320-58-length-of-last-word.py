class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # split() without specifying the delimiter will get rid of the space
        string_array = s.split()
        return len(string_array[-1])