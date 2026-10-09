class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        numsLen = len(nums)
        res = []
        sol = []
        
        def subsetsHelper(i):
            if i == numsLen:
                res.append(sol.copy())
                return 
            
            sol.append(nums[i])
            subsetsHelper(i+1)
            sol.pop()
            subsetsHelper(i+1)

        subsetsHelper(0)
        return res





        








            
            


        