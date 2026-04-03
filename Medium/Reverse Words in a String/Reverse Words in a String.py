class Solution:
    def reverseWords(self, s: str) -> str::
        word = s.split()
        word = (word::-1])
        return " ".join(word)
