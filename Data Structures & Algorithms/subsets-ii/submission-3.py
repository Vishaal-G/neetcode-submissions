class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        sol = []
        nums.sort()
        def subsetsWithDupHelper(i):
            if sol not in res:
                res.append(sol.copy())
            
            if i == len(nums):
                return
            
            sol.append(nums[i])
            subsetsWithDupHelper(i+1)
            sol.pop()
            subsetsWithDupHelper(i+1)
        
        subsetsWithDupHelper(0)
        return res