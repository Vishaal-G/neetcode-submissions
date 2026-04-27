class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if (s == t):
            return t
        if (len(s) < len(t)):
            return ""
        
        window = {}
        freqCountT = {}

        for i in t:
            freqCountT[i] = freqCountT.get(i,0)+1

        l,r = 0,0
        need = len(freqCountT)
        have = 0
        minLen = float('inf')
        bestL, bestR = 0,0
        
        for r in range(len(s)):
            window[s[r]] = window.get(s[r],0) + 1
            if s[r] in freqCountT and window[s[r]] == freqCountT[s[r]]:
                have += 1
            
            while have == need:
                if minLen > r-l+1:
                    minLen = r-l+1
                    bestL = l
                    bestR = r+1
                window[s[l]] -= 1
                if s[l] in freqCountT and window[s[l]] < freqCountT[s[l]]:
                    have -= 1
                l += 1
        return s[bestL:bestR]
            

              

               
            
                
            
                
            

        