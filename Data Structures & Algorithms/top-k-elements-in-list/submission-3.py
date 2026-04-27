class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        output = {}
        ans =[]
        for i in nums:
            if i not in output:
                output[i] = 1
            else:
                output[i] += 1
        
        for i in range (0,k):
            key = max(output, key=output.get)
            ans.append(key)
            del output[key]
        
        return ans



        

