class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        numCounts = {};

        for i in nums:
            if(i in numCounts):
                return True
            else:
                numCounts[i] = 1;
        return False
            
            

         