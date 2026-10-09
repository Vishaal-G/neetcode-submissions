class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        sol = []

        def combinationSumHelper(i):
            if sum(sol) == target:
                res.append(sol.copy())
                return

            if i == len(nums) or sum(sol) > target:
                return
            
            sol.append(nums[i])
            combinationSumHelper(i)
            sol.pop()
            combinationSumHelper(i+1)


        combinationSumHelper(0)
        return res


        