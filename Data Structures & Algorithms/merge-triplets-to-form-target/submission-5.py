class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        good = set()
        for t1, t2, t3 in triplets:
            if t1 > target[0] or t2 > target[1] or t3 > target[2]:
                continue
            if t1 == target[0]:
                good.add(0)
            
            if t2 == target[1]:
                good.add(1)

            if t3 == target[2]:
                good.add(2)
        
        return len(good) == 3
            


