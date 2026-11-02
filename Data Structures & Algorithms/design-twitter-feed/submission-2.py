class Twitter:

    def __init__(self):
        self.tweetIds = defaultdict(list)
        self.followers = defaultdict(set)
        self.counter = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweetIds[userId].append((self.counter * -1, tweetId))
        self.counter += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        maxHeap = []

        for person in self.followers[userId] | {userId}:
            if self.tweetIds[person]:
                index = len(self.tweetIds[person]) - 1                        
                time, tweetId = self.tweetIds[person][index]
                maxHeap.append((time, tweetId, person, index))

        heapq.heapify(maxHeap)

        while maxHeap and len(res) < 10:
            time, tweetId, person, index = heapq.heappop(maxHeap)
            res.append(tweetId)
            index -= 1
            if index >= 0:
                time, tweetId = self.tweetIds[person][index]
                heapq.heappush(maxHeap, (time, tweetId, person, index))
                
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].discard(followeeId)
        
