class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        lowK = 1
        highK = max(piles)
        minK = float('inf')

        while lowK <= highK:
            middleK = (lowK + highK) // 2
            hours = 0
            for i in piles:
                hours += math.ceil(i/middleK)
            if hours > h:
                lowK = middleK + 1
            else:
               minK = min(minK,middleK) 
               highK = middleK - 1
        return minK

      

        