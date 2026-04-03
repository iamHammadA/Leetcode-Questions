class Solution:
    def reverseWords(s):
        a = s.split()
        a = (a[::-1])
        return " ".join(a)
a = Solution.reverseWords("the sky is blue")
print(a)