class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        
        minHeap = list(set(hand))
        heapq.heapify(minHeap)
        count = {}
        
        for i in hand:
            count[i] = count.get(i,0) + 1
        
        while minHeap:
            initialVal = minHeap[0]
            for i in range(0, groupSize):
                if count.get(initialVal + i, 0) == 0:
                    return False
                else:
                    count[initialVal + i] -= 1
                    if count[initialVal + i] == 0:
                        if initialVal + i != minHeap[0]:
                            return False
                        heapq.heappop(minHeap)
        return True



        
