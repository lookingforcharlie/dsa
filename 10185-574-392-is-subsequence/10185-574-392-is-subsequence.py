class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # create a pointer to save index in t
        # loop through s, check if letter in s exist in t
        # if the letter exists in t, get the index of letter and save it in the pointer
        pointer_t = 0
        for letter in s: 
            pos = t.find(letter, pointer_t)
            if pos == -1: 
                return False
            pointer_t = pos + 1
        return True 