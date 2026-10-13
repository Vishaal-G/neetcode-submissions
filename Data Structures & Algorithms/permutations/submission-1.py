class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        sol = []
        used = set()

        def permuteHelper():
            if len(sol) == len(nums):
                res.append(sol.copy())
                return
            
            for i in range(len(nums)):
                if nums[i] not in used:
                    sol.append(nums[i])
                    used.add(nums[i])
                    permuteHelper()
                    removed = sol.pop()
                    used.remove(removed)
        
        permuteHelper()

        return res
        