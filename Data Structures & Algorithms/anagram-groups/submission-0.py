class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagramCheck = {}

        for i in strs:
            if tuple(sorted(i)) in anagramCheck:
                anagramCheck[tuple(sorted(i))].append(i)
            else:
                anagramCheck[tuple(sorted(i))] = [i]
        
        return anagramCheck.values()
        
        


            



                

        
      
            

            
