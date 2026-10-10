class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidatesLen = len(candidates)

        res = []
        sol = []
        candidates.sort()

        def combinationSum2Helper(i, total):
            if total == target:
                res.append(sol.copy())
                return
            
            if i == candidatesLen or total > target:
                return
            
            sol.append(candidates[i])
            combinationSum2Helper(i+1, total + candidates[i])
            sol.pop()
            while i < candidatesLen-1 and candidates[i] == candidates[i+1]:
                i += 1
            combinationSum2Helper(i+1, total)
        
        combinationSum2Helper(0,0)
       
        return res