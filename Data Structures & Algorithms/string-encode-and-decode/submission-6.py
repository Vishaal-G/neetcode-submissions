class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for i in strs:
            encoded += str(len(i)) + "#" + i
        return encoded

    def decode(self, s: str) -> List[str]:
        stringList = []
        num = 0

        while num < len(s):
            j = num
            
            while s[j] != "#":
                j += 1
            strLen = int(s[num:j])
            num = j+1
            j = num + strLen
            stringList.append(s[num:j])
            num = j
        
        return stringList

        
    
        
