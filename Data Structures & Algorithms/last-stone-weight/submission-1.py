class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = []
        for stone in stones:
            heapq.heappush(maxHeap, stone * -1)


        while len(maxHeap) > 1:
            val1 = heapq.heappop(maxHeap) * -1 
            val2 = heapq.heappop(maxHeap) * -1

            if val1 == val2:
                continue
            else:
                heapq.heappush(maxHeap, (val1 - val2)*-1)
        
        if len(maxHeap) == 1:
            return maxHeap[0] * -1
        return 0

        