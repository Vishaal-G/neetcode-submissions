class Twitter:

    def __init__(self):
        self.tweetIds = defaultdict(list)
        self.followers = defaultdict(set)
        self.counter = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetIds[userId].append((self.counter * -1, tweetId))
        self.counter += 1

        

    def getNewsFeed(self, userId: int) -> List[int]:
        maxHeap = []
        res = []
        for key, value in self.tweetIds.items():
            if key == userId or key in self.followers[userId]:
                for val in value:
                    maxHeap.append(val)
        
        heapq.heapify(maxHeap)

        for i in range (0,10):
            if not maxHeap:
                return res
            res.append(heapq.heappop(maxHeap)[1])
        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].discard(followeeId)
        
