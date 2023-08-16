class Solution:
    def longestCommonPrefix(self, strs):
        if not strs:
            return "" 
        # Find the shortest string in the list
        shortest = min(strs, key=len)

        for i, char in enumerate(shortest):
            for string in strs:
                if string[i] != char:
                    # Return the common prefix up to index i
                    return shortest[:i]

        # If all characters match, return the shortest string
        return shortest