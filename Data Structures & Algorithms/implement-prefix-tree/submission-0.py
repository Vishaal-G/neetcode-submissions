class Node:
    def __init__(self):
        self.neighbours = {} 
        self.is_end = False

class PrefixTree:
    def __init__(self):
        self.tree = Node()
        
    def insert(self, word: str) -> None:
        prev = self.tree
        for i in word:
            if i not in prev.neighbours:
                valInsert = Node()
                prev.neighbours[i] = valInsert
            prev = prev.neighbours[i]
        prev.is_end = True

    def search(self, word: str) -> bool:
        prev = self.tree
        for i in word:
            if i not in prev.neighbours:
                return False
            prev = prev.neighbours[i]
        
        return prev.is_end
    def startsWith(self, prefix: str) -> bool:
        prev = self.tree
        for i in prefix:
            if i not in prev.neighbours:
                return False
            prev = prev.neighbours[i]
        return True
