class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        count = 0

        if len(s) == 1:
            return 1
        
        for r in range (1, len(s)):
            while s[r] in s[l:r]:
                l += 1 
            count = max(count, r - l + 1)
        return count
            

        

        