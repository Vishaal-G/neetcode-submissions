class Solution:
    def climbStairs(self, n: int) -> int:
        self.res = 0
        cache = {0:1, 1:1, 2: 2}
        
        for i in range (0,n+1):
            if i in cache:
                continue
            cache[i] = cache[i-1] + cache[i-2]

        return cache[n]
    

        
        