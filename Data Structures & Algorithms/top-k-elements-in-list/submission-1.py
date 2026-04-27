class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqNum  = {}
        res = []

        for i in nums:
            if i not in freqNum:
                freqNum[i] = 1
            else:
                freqNum[i] += 1
        
        for i in range (0,k):
            res.append(max(freqNum, key=freqNum.get))
            del freqNum[max(freqNum, key=freqNum.get)]
        return res



        