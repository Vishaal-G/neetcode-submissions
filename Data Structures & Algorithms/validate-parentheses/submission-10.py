class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dictSymbols = {')' : '(', '}' : '{', ']':'['}
       
        for i in s:
            if i in dictSymbols:
                if stack and dictSymbols[i] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False
            
            
                
                   
                   

        


                
            



        