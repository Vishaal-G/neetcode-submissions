class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        sol = []

        def permuteHelper():
            if len(sol) == len(nums):
                res.append(sol.copy())
                return
            
            for i in range(len(nums)):
                if nums[i] not in sol:
                    sol.append(nums[i])
                    permuteHelper()
                    sol.pop()
        
        permuteHelper()

        return res
        