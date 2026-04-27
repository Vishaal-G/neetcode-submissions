class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        longestSum = 0
    
        for i in nums:
            if i-1 not in numSet:
                sumNum = 1
                num = i
                while num + 1 in numSet:
                    sumNum += 1
                    num +=1 
                
                longestSum = max(longestSum, sumNum)
        
        return longestSum 

            

        