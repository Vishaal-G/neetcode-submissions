class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        outputNum = []
        sumNum = 1
        l, r = 0,0
        
        while (l < len(nums)):
            for i in nums:
                if (l != r):
                    sumNum *= i
                r += 1
            outputNum.append(sumNum)
            sumNum = 1
            l += 1
            r = 0
        
        return outputNum
            
        
        

