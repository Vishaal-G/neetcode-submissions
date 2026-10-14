class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        sol = []

        def subsetsWithDupHelper(i):
            if sorted(sol) not in res:
                res.append((sorted(sol).copy()))
            
            if i == len(nums):
                return
            
            sol.append(nums[i])
            subsetsWithDupHelper(i+1)
            sol.pop()
            subsetsWithDupHelper(i+1)
        
        subsetsWithDupHelper(0)
        return res