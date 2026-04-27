class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [(temperatures[len(temperatures)-1], len(temperatures)-1)]
        res = []

        for i in range (len(temperatures)-1,-1,-1):
            while stack and temperatures[i] >= stack[-1][0]:
                stack.pop()
            if not stack:
                res.append(0)
            else:
                res.append(stack[-1][1] - i)
            stack.append((temperatures[i],i))
        return list(reversed(res))
            

            


           
        
      

            
            
        


            
