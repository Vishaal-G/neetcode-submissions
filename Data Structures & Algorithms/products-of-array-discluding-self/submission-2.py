class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        outputNum = [1] * len(nums)
        
        addSum = 1
        for i in range (len(nums)):
            outputNum[i] = addSum
            addSum *= nums[i]
            
        
        addSum2 = 1
        for i in range (len(nums)-1, -1, -1):
            outputNum[i] *= addSum2
            addSum2 *= nums[i]
        return outputNum

        

            
            
        
        

