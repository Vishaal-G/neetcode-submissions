class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        mapping = {"2": ["a","b","c"], "3": ["d","e","f"], "4": ["g", "h", "i"], "5" : ["j", "k", "l"], "6": ["m", "n", "o"], "7": ["p", "q", "r", "s"], "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"]}
        
        def letterCombinationsHelper(string, i):
            if not digits:
                return 
            if len(string) == len(digits):
                res.append(string)
                return
            
            
            for letter in mapping[digits[i]]:
                letterCombinationsHelper(string + letter, i + 1)
            
        letterCombinationsHelper("", 0)
        return res

            

                
                

                
            



        