class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        

        def generateParenthesisHelper(string, close, openB):
            if close == n and openB == n:
                res.append(string)
                return
            
            if openB < n:
                generateParenthesisHelper(string + "(", close, openB + 1)
            
            if openB > close:
                generateParenthesisHelper(string + ")", close + 1, openB)
        
        generateParenthesisHelper("",0,0)
        return res
            
            

