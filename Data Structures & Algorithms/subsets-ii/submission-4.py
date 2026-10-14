class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        sol = []
        nums.sort()
        def subsetsWithDupHelper(i):
            if i == len(nums):
                res.append(sol.copy())
                return
            
            sol.append(nums[i])
            subsetsWithDupHelper(i+1)
            sol.pop()
            while i < len(nums)-1 and nums[i] == nums[i+1]:
                i += 1
            subsetsWithDupHelper(i+1)
        
        subsetsWithDupHelper(0)
        return res