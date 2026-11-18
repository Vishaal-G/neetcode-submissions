class Solution:
    def checkValidString(self, s: str) -> bool:
        minOpen = 0
        maxOpen = 0

        for i in s:
            if i == "(":
                minOpen += 1
                maxOpen += 1
            elif i == ")":
                minOpen -= 1
                maxOpen -= 1
            else:
                maxOpen += 1
                minOpen -= 1
            if maxOpen < 0:
                return False
            if minOpen < 0:
                minOpen = 0
        
        return minOpen == 0


                

            
                
            


        