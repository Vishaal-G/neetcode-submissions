class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #Key is array, value is words
        outPut = {}
        for i in strs:
            wordList = [0] * 26
            for j in i:
                wordList[ord(j) - ord('a')] += 1
            if (tuple(wordList) not in outPut):
                outPut[tuple(wordList)] = []
            outPut[tuple(wordList)].append(i)

        return outPut.values()
                




        




        