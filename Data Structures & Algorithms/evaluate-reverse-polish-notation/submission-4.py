class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        a = 0
        b = 0
        symbolList = ["+", "-", "*", "/"]

        for i in tokens:
            if i not in symbolList:
                stack.append(int(i))
            elif i == "+":
                a = stack.pop()
                b = stack.pop()
                stack.append(a+b)
            elif i == "*":
                a = stack.pop()
                b = stack.pop()
                stack.append(a*b)
            elif i == "-":
                a = stack.pop()
                b = stack.pop()
                stack.append(b-a)
            elif i == "/":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b/a))
        return stack[-1]

                

            


        