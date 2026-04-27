class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for i in strs:
            encoded += i
            encoded += "-"
        return encoded

    def decode(self, s: str) -> List[str]:
        stringList = []
        
        index = 0
        for i in range (len(s)):
            if (s[i] == "-"):
                stringList.append(s[index:i])
                index = i+1
        return stringList
