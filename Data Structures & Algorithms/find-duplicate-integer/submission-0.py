class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        count = {}
        
        for i in range (len(nums)):
            count[nums[i]] = count.get(nums[i],0) + 1
        
        for key in count:
            if count[key] > 1:
                return key
        