class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for i in strs:
            res += i + "-"
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        temp = 0
        for i in range(len(s)):
            if s[i] == "-":
                res.append(s[temp:i])
                temp = i + 1
        return res

    
    
