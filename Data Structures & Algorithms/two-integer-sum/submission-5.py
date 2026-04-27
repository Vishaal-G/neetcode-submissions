class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        totalSum = {};

        for index, value in enumerate(nums):
            difference = target - value
            if difference in totalSum:
                return [totalSum[difference],index]
            else:
                totalSum[value] = index
                
            
