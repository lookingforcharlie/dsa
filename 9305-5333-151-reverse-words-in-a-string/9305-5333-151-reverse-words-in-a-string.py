class Solution:
    def reverseWords(self, s: str) -> str:
        words_arr = s.split() 
        new_words_arr = words_arr[::-1]
        return " ".join(new_words_arr)
        