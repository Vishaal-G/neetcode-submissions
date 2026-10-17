class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        sol = []

        def isPalindrome(s, l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        def partitionHelper(i):
            if i >= len(s):
                res.append(sol.copy())
                return
            for j in range(i, len(s)):
                if isPalindrome(s, i, j):
                    sol.append(s[i:j+1])
                    partitionHelper(j + 1)
                    sol.pop()

        partitionHelper(0)
        return res