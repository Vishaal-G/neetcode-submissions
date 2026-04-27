class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        beforeIndex = [1] * len(nums)
        afterIndex = [1] * len(nums)
        res= [1] * len(nums)

        for i in range (1, len(nums)):
            beforeIndex[i] = beforeIndex[i-1] * nums[i-1]
        
        for j in range (len(nums)-2, -1, -1):
            afterIndex[j] = afterIndex[j+1] * nums[j+1]
        
        for i in range(len(nums)):
            res[i] = beforeIndex[i] * afterIndex[i]
        
        return res





