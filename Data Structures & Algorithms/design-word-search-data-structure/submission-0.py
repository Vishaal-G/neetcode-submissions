class Node:
    def __init__(self):
        self.neighbours = {}
        self.is_end = False
class WordDictionary:

    def __init__(self):
        self.tree = Node()

    def addWord(self, word: str) -> None:
        prev = self.tree
        for i in word:
            if i not in prev.neighbours:
                val = Node()
                prev.neighbours[i] = val
            prev = prev.neighbours[i]
        prev.is_end = True
        
    def search(self, word: str) -> bool:
        prev = self.tree

        def searchHelper(prev, i):
            if i == len(word):
                return prev.is_end
            
            if word[i] == ".":
                for nei in prev.neighbours:
                    if searchHelper(prev.neighbours[nei], i+1):
                        return True
                return False
            
            if word[i] not in prev.neighbours:
                return False
            else:
                return searchHelper(prev.neighbours[word[i]], i+1)
        
        return searchHelper(prev,0)


        
        
