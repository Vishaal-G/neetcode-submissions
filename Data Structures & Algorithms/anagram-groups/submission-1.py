class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramCheck = defaultdict(list)

        for i in strs:
            count = [0] * 26 

            for c in i:
                count[ord(c) - ord('a')] += 1
            
            anagramCheck[tuple(count)].append(i)
        
        return anagramCheck.values()
        
        


            



                

        
      
            

            
