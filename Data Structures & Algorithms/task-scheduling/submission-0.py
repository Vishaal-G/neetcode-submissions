class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        
        maxHeap = []

        for frequency in count.values():
            heapq.heappush(maxHeap, frequency * -1)
        
        time = 0
        Q = deque()
        
        while maxHeap or Q:
            time += 1

            if maxHeap:
                letterCount = (heapq.heappop(maxHeap)) + 1 
                if letterCount != 0:
                    Q.append([letterCount, time + n])
            
            if Q and Q[0][1] == time:
                heapq.heappush(maxHeap, Q.popleft()[0])

        return time
