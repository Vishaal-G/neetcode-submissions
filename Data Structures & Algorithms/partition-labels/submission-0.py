class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        res = []
        size = 0
        end = 0
        count = {}
        
        for i in range (len(s)):
            count[s[i]] = max(count.get(s[i], 0), i)

        print(count)
        for i in range(len(s)):
            size += 1
            end = max(end, count[s[i]])

            if i == end:
                res.append(size)
                size = 0
        
        return res
            

            
            

            
