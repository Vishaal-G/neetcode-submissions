class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        res = []
        adjList = defaultdict(list)
        for course, prereq in prerequisites: 
            adjList[course].append(prereq)
        
        seen = set()
        def findOrderHelper(course):
            if course in seen:
                return False
            if adjList[course] == "Done":
                return True
            
            seen.add(course)

            for pre in adjList[course]:
                if not findOrderHelper(pre):
                    return False
            
            seen.remove(course)
            adjList[course] = "Done"
            res.append(course)
            return True

        for i in range (numCourses):
            if not findOrderHelper(i):
                return []
        
        return res
        
        




        
        