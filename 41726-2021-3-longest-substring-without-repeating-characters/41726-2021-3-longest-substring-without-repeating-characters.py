class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        current_string = ""
        longest = 0

        for c in s:
            # 1) shrink until c is no longer in the window
            while c in current_string:
                current_string = current_string[1:]

            # 2) append the new char
            current_string += c

            # 3) update longest
            longest = max(longest, len(current_string))

        return longest