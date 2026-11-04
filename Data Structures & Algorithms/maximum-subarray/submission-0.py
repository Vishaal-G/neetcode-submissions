class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        runningSum = nums[0]
        res = runningSum
        for i in range (1, len(nums)):
            if runningSum < 0:
                runningSum = nums[i]
            else:
                runningSum += nums[i]
            
            res = max(res, runningSum)
        return res
                
        