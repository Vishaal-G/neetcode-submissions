class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output = {}
        ans =[[] for i in range (len(nums)+1)]
        for i in nums:
            if i not in output:
                output[i] = 1
            else:
                output[i] += 1
        
        for key, value in output.items():
            ans[value].append(key)
        
        res = []
        for i in range ((len(ans))-1,-1,-1):
            for j in ans[i]:
                res.append(j)
            if len(res) == k:
                return res

        
        



        

