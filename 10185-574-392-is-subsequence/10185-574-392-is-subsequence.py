class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # create a pointer to save index in t
        # create another pointer in the for loop
        # use str.find() to find the index
        pointer_t = 0
        for letter in s: 
            pos = t.find(letter, pointer_t)
            if pos == -1: 
                return False
            pointer_t = pos + 1
        return True 