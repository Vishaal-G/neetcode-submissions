class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        sol = []
        total = 0
        def combinationSumHelper(i, total):
            if total == target:
                res.append(sol.copy())
                return

            if i == len(nums) or total > target:
                return
            
            sol.append(nums[i])
            combinationSumHelper(i, total + nums[i])
            sol.pop()
            combinationSumHelper(i+1, total)

        combinationSumHelper(0,0)
        return res


        