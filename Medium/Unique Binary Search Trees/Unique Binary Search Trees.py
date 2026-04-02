class Solution:
    def numTrees(self, n: int) -> int:
        a = 1
        b = 1
        c = 1
        def f(n):
            if n == 1:
                return 1
            return n * (f(n-1))
        a = f(2*n)
        b = f(n+1)
        c = f(n)
        a = int(a/(b*c))
        return a
a = Solution()
print(a.numTrees(5))