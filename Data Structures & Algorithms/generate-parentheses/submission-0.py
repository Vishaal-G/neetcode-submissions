class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = [("", n, n)]
        res = []

        while stack:
            string, open_left, open_right = stack.pop()

            if open_left > 0:
                stack.append((string + "(", open_left-1, open_right))
            if open_right > open_left:
                stack.append((string + ")",open_left,open_right-1))
            if open_left == 0 and open_right == 0:
                res.append(string)
        return res
