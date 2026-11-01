class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        maxHeap = []
        
        for x,y in points:
            distance = math.sqrt((x ** 2) + (y ** 2))
            heapq.heappush(maxHeap, (distance * -1, x, y))

            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
        
        return [[x,y] for distance, x,y in maxHeap]




        
        