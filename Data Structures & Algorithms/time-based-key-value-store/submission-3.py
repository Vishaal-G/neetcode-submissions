class TimeMap:

    def __init__(self):
        self.timeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.timeMap:
            self.timeMap[key].append((value,timestamp))
        else:
            self.timeMap[key] = [(value, timestamp)]

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap:
            return ""
        
        low = 0
        high = len(self.timeMap[key]) - 1

        temp = ""
        while low <= high:
            
            middle = (low + high) // 2
            
            if self.timeMap[key][middle][1] == timestamp:
                return self.timeMap[key][middle][0]
            
            elif self.timeMap[key][middle][1] > timestamp:
                high = middle - 1
            else:
                temp = self.timeMap[key][middle][0]
                low = middle + 1
        return temp









        
